# --------------------------------------------------------------------------
# tldr_parser.py
#
# A script to parse a TLDR newsletter .eml file, scrape the full content
# of each linked article, and generate a structured Markdown file for use
# with AI tools like NotebookLM.
#
# Author: Gemini, based on a specification by the user.
# Date: 2025-07-06
#
# Instructions:
# 1. Make sure you have the required libraries:
#    pip install beautifulsoup4 lxml newspaper3k
#
# 2. Run the script from your terminal:
#    python tldr_parser.py "/path/to/your/newsletter.eml"
# --------------------------------------------------------------------------

import sys
import email
from email.policy import default
from bs4 import BeautifulSoup
from newspaper import Article, Config
from datetime import datetime

# --- Configuration for Newspaper3k ---
# We'll use a standard user-agent to avoid being blocked by some sites.
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10 # Set a 10-second timeout for requests

def parse_eml_to_html(file_path):
    """
    Opens an .eml file and extracts the HTML content.
    Returns the HTML content as a string, or None if not found.
    """
    print(f"1. Parsing EML file: {file_path}")
    try:
        with open(file_path, 'rb') as f:
            msg = email.message_from_binary_file(f, policy=default)

        # Walk through the email parts to find the HTML content
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                return part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore')
        print("Error: No HTML part found in the .eml file.")
        return None
    except Exception as e:
        print(f"Error parsing .eml file: {e}")
        return None

def parse_newsletter_html(html_content):
    """
    Parses the newsletter's HTML to extract article categories, titles,
    URLs, and the TLDR summaries.
    """
    print("2. Parsing HTML for article summaries...")
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'lxml')
    articles = []
    current_category = "Uncategorized"

    # All content seems to be within tables. We iterate through them.
    # This is a bit simplistic but works for the current TLDR format.
    all_tables = soup.find_all('table')

    for table in all_tables:
        # Check for a category header (<h1> inside the table)
        header = table.find('h1')
        if header and header.find('strong'):
            current_category = header.get_text(strip=True)
            continue

        # Check for an article block
        # The title is a link with bolded text inside a <td> with specific padding.
        container_td = table.find('td', class_='container', style=lambda s: 'padding: 15px 15px' in s if s else False)
        if container_td:
            title_link = container_td.find('a')
            
            if title_link and title_link.find('strong'):
                title = title_link.get_text(strip=True)
                url = title_link.get('href')

                # The description is in a span tag that follows the title link's block
                description_span = container_td.find('span', style=lambda s: 'Helvetica Neue' in s if s else False)
                if description_span and url:
                    # Clean up the description text
                    description = ' '.join(description_span.get_text(separator=' ', strip=True).split())

                    articles.append({
                        'category': current_category,
                        'title': title,
                        'url': url,
                        'summary': description,
                    })

    print(f"   Found {len(articles)} articles in the newsletter.")
    return articles

def fetch_full_article_content(url):
    """
    Scrapes the full text of an article from its URL using newspaper3k.
    Returns the cleaned text or a failure message.
    """
    try:
        article = Article(url, config=config)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        # If scraping fails for any reason (paywall, 404, etc.), return the failure message.
        return f"[Scraping failed for this URL. Error: {e}]"

def generate_markdown_file(articles_data, newsletter_date):
    """
    Generates the final Markdown file from the processed article data.
    """
    filename = f"tldr_summary_{newsletter_date}.md"
    print(f"\n4. Generating Markdown file: {filename}")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# TLDR Newsletter Summary: {newsletter_date}\n\n")

        last_category = ""
        for article in articles_data:
            # Print category header if it's a new one
            if article['category'] != last_category:
                f.write(f"## {article['category']}\n\n")
                last_category = article['category']

            # Write the article content
            f.write(f"### {article['title']}\n")
            f.write(f"**URL:** {article['url']}\n")
            f.write(f"**TLDR Summary:** {article['summary']}\n")
            f.write(f"**Full Article Content:**\n{article.get('full_content', '[Content not fetched]')}\n\n")
            f.write("---\n\n")
            
    print("   Markdown file generated successfully.")


def main():
    """
    Main function to orchestrate the parsing and generation process.
    """
    # --- 1. Get EML file path from command-line arguments ---
    if len(sys.argv) != 2:
        print("Usage: python tldr_parser.py \"/path/to/your/newsletter.eml\"")
        sys.exit(1)
    eml_file_path = sys.argv[1]

    # --- 2. Parse EML to get HTML ---
    html = parse_eml_to_html(eml_file_path)
    if not html:
        print("Something went wrong while parsing the .eml file. Exiting.")
        sys.exit(1)

    # --- 3. Parse HTML to get article summaries ---
    articles_list = parse_newsletter_html(html)
    if not articles_list:
        print("Could not find any articles to process. Exiting.")
        sys.exit(0)
    
    # Try to get the date from the newsletter for the filename
    try:
        soup = BeautifulSoup(html, 'lxml')
        date_str = soup.find('span', id='date').get_text(strip=True)
    except:
        date_str = datetime.now().strftime('%Y-%m-%d')


    # --- 4. Fetch full content for each article ---
    print("\n3. Fetching full article content from URLs...")
    for i, article in enumerate(articles_list):
        print(f"   ({i+1}/{len(articles_list)}) Scraping: {article['title'][:50]}...")
        full_content = fetch_full_article_content(article['url'])
        article['full_content'] = full_content

    # --- 5. Generate the final Markdown file ---
    generate_markdown_file(articles_list, date_str)
    
    print("\nProcess complete!")


if __name__ == "__main__":
    main()