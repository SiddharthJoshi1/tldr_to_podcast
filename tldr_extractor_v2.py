# --------------------------------------------------------------------------
# tldr_parser.py (Version 3 - Handles forwarded email HTML)
# --------------------------------------------------------------------------

import sys
from bs4 import BeautifulSoup
from newspaper import Article, Config
from datetime import datetime

# --- Configuration for Newspaper3k ---
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10 

def read_html_file(file_path):
    print(f"1. Reading HTML file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return None

def parse_newsletter_html(html_content):
    print("2. Parsing HTML for article summaries...")
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'lxml')
    articles = []
    current_category = "Uncategorized"

    all_tables = soup.find_all('table')

    for table in all_tables:
        header = table.find('h1')
        if header and header.find('strong'):
            current_category = header.get_text(strip=True)
            continue

        # --- THE FIX IS HERE: We now check for BOTH forwarded and original class names ---
        # First, try to find the prefixed class name from forwarded emails (e.g., "x_container")
        container_td = table.find('td', class_='x_container', style=lambda s: 'padding:15px 15px' in s if s else False)
        # If that fails, fall back to the original class name
        if not container_td:
             container_td = table.find('td', class_='container', style=lambda s: 'padding: 15px 15px' in s if s else False)

        if container_td:
            title_link = container_td.find('a')
            if title_link and title_link.find('strong'):
                title = title_link.get_text(strip=True)
                url = title_link.get('href')

                description_span = container_td.find('span', style=lambda s: 'Helvetica Neue' in s if s else False)
                if description_span and url:
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
    try:
        article = Article(url, config=config)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"[Scraping failed for this URL. Error: {e}]"

def generate_markdown_file(articles_data, newsletter_date):
    filename = f"tldr_summary_{newsletter_date}.md"
    print(f"\n4. Generating Markdown file: {filename}")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# TLDR Newsletter Summary: {newsletter_date}\n\n")
        last_category = ""
        for article in articles_data:
            if article['category'] != last_category:
                f.write(f"## {article['category']}\n\n")
                last_category = article['category']
            f.write(f"### {article['title']}\n")
            f.write(f"**URL:** {article['url']}\n")
            f.write(f"**TLDR Summary:** {article['summary']}\n")
            f.write(f"**Full Article Content:**\n{article.get('full_content', '[Content not fetched]')}\n\n")
            f.write("---\n\n")
    print("   Markdown file generated successfully.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python tldr_parser.py \"/path/to/your/newsletter.html\"")
        sys.exit(1)
    html_file_path = sys.argv[1]

    html = read_html_file(html_file_path)
    if not html:
        sys.exit(1)

    articles_list = parse_newsletter_html(html)
    if not articles_list:
        print("Could not find any articles to process. Exiting.")
        sys.exit(0)
    
    # --- THE FIX IS HERE: We now find the date span with a flexible ID selector ---
    try:
        # This lambda function finds a span whose ID contains the word "date" (like "date" or "x_date")
        soup = BeautifulSoup(html, 'lxml')
        date_str = soup.find('span', id=lambda x: x and 'date' in x).get_text(strip=True)
    except:
        date_str = datetime.now().strftime('%Y-%m-%d')

    print("\n3. Fetching full article content from URLs...")
    for i, article in enumerate(articles_list):
        print(f"   ({i+1}/{len(articles_list)}) Scraping: {article['title'][:50]}...")
        full_content = fetch_full_article_content(article['url'])
        article['full_content'] = full_content

    generate_markdown_file(articles_list, date_str)
    
    print("\nProcess complete!")

if __name__ == "__main__":
    main()