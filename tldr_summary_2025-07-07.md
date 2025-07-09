# TLDR Newsletter Summary: 2025-07-07

## TLDR2025-07-07

### Stop
 shipping slop (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fdevin.ai%2F%3Futm_medium=newsletter%26utm_source=tldr-flagship%26utm_campaign=20250707/2/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/6OIdEmaAG2BMVhn0NwDwS--iJkHv0Z4HDFKm5RUMWSs=412
**TLDR Summary:** Ever tried using coding agents on large, complex codebases? You've probably noticed they often miss key details or misunderstand critical parts of your code. That's where Devin comes in — the SWE agent built for real-world work. Devin analyzes your codebase to craft context-grounded plans before implementing and testing its changes. > Built for serious engineers , not vibe coders. > Integrates with Jira , Linear , Slack , and more. > Secure, private, and SOC 2 compliant . Crush your backlog with Devin, starting from $20. Or, find out why Ramp, Bilt, and Gumroad are already on board.
**Full Article Content:**
How Nubank refactors millions of lines of code to improve engineering efficiency with Devin

8x engineering time efficiency gain 20x cost savings

Overview

One of Nubank’s most critical, company-wide projects for 2023-2024 was a migration of their core ETL — an 8 year old, multi-million lines of code monolith — to sub-modules. To handle such a large refactor, their only option was a multi-year effort that distributed repetitive refactoring work across over one thousand of their engineers. With Devin, however, this changed: engineers were able to delegate Devin to handle their migrations and achieve a 12x efficiency improvement in terms of engineering hours saved, and over 20x cost savings. Among others, Data, Collections, and Risk business units verified and completed their migrations in weeks instead of months or years.

The Problem

Nubank was born into the tradition of centralized ETL FinServ architectures. To date, the monolith architecture had worked well for Nubank — it enabled the developer autonomy and flexibility that carried them through their hypergrowth phases. After 8 years, however, Nubank’s sheer volume of customer growth, as well as geographic and product expansion beyond their original credit card business, led to an entangled, behemoth ETL with countless cross-dependencies and no clear path to continuing to scale.

For Nubankers, business critical data transformations started taking increasingly long to run, with chains of dependencies as deep as 70 and insufficient formal agreements on who was responsible for maintaining what. As the company continued to grow, it became clear that the ETL would be a primary bottleneck to scale.

Nubank concluded that there was an urgent need to split up their monolithic ETL repository, amassing over 6 million lines of code, into smaller, more flexible sub-modules.

Nubank’s code migration was filled with the monotonous, repetitive work that engineers dread. Moving each data class implementation from one architecture to another while tracing imports correctly, performing multiple delicate refactoring steps, and accounting for any number of edge cases was highly tedious, even to do just once or twice. At Nubank’s scale, however, the total migration scope involved more than 1,000 engineers moving ~100,000 data class implementations over an expected timeline of 18 months.

In a world where engineering resources are scarce, such large-scale migrations and modernizations become massively expensive, time-consuming projects that distract from any engineering team’s core mission: building better products for customers. Unfortunately, this is the reality for many of the world’s largest organizations.

The Decision: an army of Devins to tackle subtasks in parallel

At project outset in 2023, Nubank had no choice but to rely on their engineers to perform code changes manually. Migrating one data class was a highly discretionary task, with multiple variations, edge cases, and ad hoc decision-making — far too complex to be scriptable, but high-volume enough to be a significant manual effort.

Within weeks of Devin’s launch, Nubank identified a clear opportunity to accelerate their refactor at a fraction of the engineering hours. Migration or large refactoring tasks are often fantastic projects for Devin: after investing a small, fixed cost to teach Devin how to approach sub-tasks, Devin can go and complete the migration autonomously. A human is kept in the loop just to manage the project and approve Devin’s changes.

The Solution: Custom ETL Migration Devin

A task of this magnitude, with the vast number of variations that it had, was a ripe opportunity for fine-tuning. The Nubank team helped to collect examples of previous migrations their engineers had done manually, some of which were fed to Devin for fine-tuning. The rest were used to create a benchmark evaluation set. Against this evaluation set, we observed a doubling of Devin’s task completion scores after fine-tuning, as well as a 4x improvement in task speed. Roughly 40 minutes per sub-task dropped to 10, which made the whole migration start to look much cheaper and less time-consuming, allowing the company to devote more energy to new business and new value creation instead.

Devin contributed to its own speed improvements by building itself classical tools and scripts it would later use on the most common, mechanical components of the migration. For instance, detecting the country extension of a data class (either ‘br’, ‘co’, or ‘mx’) based on its file path was a few-step process for each sub-task. Devin’s script automatically turned this into a single step executable — improvements from which added up immensely across all tens of thousands of sub-tasks.

There is also a compounding advantage on Devin’s learning. In the first weeks, it was common to see outstanding errors to fix, or small things Devin wasn’t sure how to solve. But as Devin saw more examples and gained familiarity with the task, it started to avoid rabbit holes more often and find faster solutions to previously-seen errors and edge cases. Much like a human engineer, we observed obvious speed and reliability improvements with every day Devin worked on the migration.

Results: Delivering an 8-12x faster migration, lifting a burden from every engineer, and slashing migration costs by 20x.

“Devin provided an easy way to reduce the number of engineering hours for the migration, in a way that was more stable and less prone to human error. Rather than engineers having to work across several files and complete an entire migration task 100%, they could just review Devin’s changes, make minor adjustments, then merge their PR” Jose Carlos Castro, Senior Product Manager

8-12x efficiency gains This is calculated by comparing the typical engineering hours required to complete a data class migration task against the total engineering hours spent prompting and reviewing Devin’s work on the same task.

Over 20x cost savings on scope of the migration delegated to Devin This is calculated by comparing the cost of running Devin versus the hourly cost of an engineer completing that task. The significant savings are heavily driven by speed of task execution and cost effectiveness of Devin relative to human engineering time – it does not even consider the value captured by completing the entire project months ahead of schedule!

---

## Big Tech & Startups

### TikTok's
 ‘ban' problem could end soon with a new app and a sale (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.theverge.com%2Fnews%2F698999%2Ftiktok-ban-sale-rumor-new-app-oracle%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/k1t5PX6AYuknXGXdkb7H-lLf_tPsp9b4C8W0lBW22RM=412
**TLDR Summary:** The Trump administration says it's close to an agreement for a TikTok sale that satisfies the law's requirements, but it involves a new, separate version of the app. The deal still needs approval from the Chinese government. TikTok staff are reportedly working on a new version of the app for release in app stores on September 5. Under the current timeline, the original TikTok app will leave app stores as the new one launches, and the old one will stop working entirely in March 2026.
**Full Article Content:**
is a senior editor following news across tech, culture, policy, and entertainment. He joined The Verge in 2021 after several years covering news at Engadget.

Even with the TikTok divest-or-ban law officially in effect since January, the app has only shut down service in the US for one day. Now, The Information reports that an agreement for a sale satisfying the law’s requirements is close and would come with a new, separate version of the app.

Any deal, however, would need approval from the Chinese government, which is also still wrangling with the Trump administration over tariffs.

The outlet reports that the Trump administration says it’s close to working out a sale to a group of “non-Chinese” investors, including Oracle, with current majority owner ByteDance maintaining a minority stake that would satisfy the terms of the Protecting Americans from Foreign Adversary Controlled Applications Act.

Earlier today, the Wall Street Journal reported that the General Services Administration says Oracle has reached a new agreement with the federal government that “is the first of its kind that provides the entire government with a discount on cloud infrastructure,” with a 75 percent discount on licensed software.

TikTok’s staff is reportedly working on a new version of the app — dubbed M2, to the current app’s internal M designation — for release in app stores on September 5th. Trump issued a third legally questionable extension of the deadline to ban TikTok from US app stores last month, which is set to expire in mid-September. According to The Information’s unnamed source, under the current timeline, the original TikTok app would leave app stores as the new one launches and then stop working entirely in March 2026.

---

### TikTok's
 ‘ban' problem could end soon with a new app and a sale (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.theverge.com%2Fnews%2F698999%2Ftiktok-ban-sale-rumor-new-app-oracle%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/k1t5PX6AYuknXGXdkb7H-lLf_tPsp9b4C8W0lBW22RM=412
**TLDR Summary:** The Trump administration says it's close to an agreement for a TikTok sale that satisfies the law's requirements, but it involves a new, separate version of the app. The deal still needs approval from the Chinese government. TikTok staff are reportedly working on a new version of the app for release in app stores on September 5. Under the current timeline, the original TikTok app will leave app stores as the new one launches, and the old one will stop working entirely in March 2026.
**Full Article Content:**
is a senior editor following news across tech, culture, policy, and entertainment. He joined The Verge in 2021 after several years covering news at Engadget.

Even with the TikTok divest-or-ban law officially in effect since January, the app has only shut down service in the US for one day. Now, The Information reports that an agreement for a sale satisfying the law’s requirements is close and would come with a new, separate version of the app.

Any deal, however, would need approval from the Chinese government, which is also still wrangling with the Trump administration over tariffs.

The outlet reports that the Trump administration says it’s close to working out a sale to a group of “non-Chinese” investors, including Oracle, with current majority owner ByteDance maintaining a minority stake that would satisfy the terms of the Protecting Americans from Foreign Adversary Controlled Applications Act.

Earlier today, the Wall Street Journal reported that the General Services Administration says Oracle has reached a new agreement with the federal government that “is the first of its kind that provides the entire government with a discount on cloud infrastructure,” with a 75 percent discount on licensed software.

TikTok’s staff is reportedly working on a new version of the app — dubbed M2, to the current app’s internal M designation — for release in app stores on September 5th. Trump issued a third legally questionable extension of the deadline to ban TikTok from US app stores last month, which is set to expire in mid-September. According to The Information’s unnamed source, under the current timeline, the original TikTok app would leave app stores as the new one launches and then stop working entirely in March 2026.

---

### OpenAI
 experiments with new "Study together" tool on ChatGPT (1 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.testingcatalog.com%2Fopenai-experiments-with-new-study-together-tool-on-chatgpt%2F%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/LcmkUY_t8u0XzDgmWpwM5Jl4Y2VpKmIvP64KSTGjcVY=412
**TLDR Summary:** 'Study together' is a new tool in ChatGPT that guides users through the study process step-by-step. It creates a more interactive, guided study environment by posing more questions and breaking down topics, helping users actively learn rather than just receive explanations. It checks answers and adapts by offering follow-ups or clarifying explanations as needed. There is currently no official timeline for the rollout of the feature - a growing number of users are reporting access, indicating a limited A/B test or pre-release trial.
**Full Article Content:**
What we know so far: Some users got access to a new tool called "Study together", which acts differently and guides you through the study process step by step.

OpenAI is preparing a new feature called "Study together", which has started appearing in system hints for some users within ChatGPT’s main prompt, alongside familiar tools like web search and image generation. This new feature appears to create a more interactive, guided study environment. According to user reports, when enabled, ChatGPT shifts its style by posing more questions and breaking down topics step by step, helping users actively learn rather than just receive explanations. It not only checks answers but also adapts by offering follow-ups or clarifying explanations as needed.

The main audience for "Study together" would likely be students and educators, particularly those using ChatGPT for structured learning or revision. The feature’s design, offering active guidance, question-based review, and adaptive feedback, suggests it could play a role in classrooms or university settings, possibly as part of an education-focused ChatGPT subscription or deployment plan.

I have it too, it doesn't do anything yet pic.twitter.com/5UoRndqj4n — Quiveron (@quiveron_x) July 6, 2025

The rollout details remain unclear. Some suspect it might be an internal test or a temporary mistake, while others note a growing number of users reporting access, indicating a limited A/B test or pre-release trial. There’s currently no official timeline, but the breadth of these reports points to a possible wider launch or at least a formal announcement in the coming week. If officially adopted, this feature could mark a new direction for OpenAI in education, fitting into its broader strategy of expanding ChatGPT’s practical applications, especially in professional and academic contexts, while further distinguishing its offering from general AI chat tools.

---

## Science & Futuristic Technology

### Tesla
 launches Oasis Supercharger with solar farm and off-grid batteries (3 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Felectrek.co%2F2025%2F07%2F03%2Ftesla-launches-oasis-supercharger-with-solar-farm-off-grid-batteries%2F%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/aRW-2vTg-RYAJ7YcFM4QHshoT9Q-mH_Kx490UzqHmZQ=412
**TLDR Summary:** Tesla's Oasis Supercharger, an EV charging station with a solar farm and off-grid batteries, is now open in Lost Hills, California. The project consists of 168 chargers, half of which are currently operational. It is equipped with 11 MW of ground-mounted solar panels and canopies. Spanning 30 acres of land, it has 10 Tesla Megapacks with a total energy storage capacity of 39 MWh. The charging station can be operated off-grid. The rest of the stalls and a lounge will be open later this year.
**Full Article Content:**
Tesla has launched its new Oasis Supercharger, the long-promised EV charging station of the future, with a solar farm and off-grid batteries.

Early in the deployment of the Supercharger network, Tesla promised to add solar arrays and batteries to the Supercharger stations, and CEO Elon Musk even said that most stations would be able to operate off-grid.

While Tesla did add solar and batteries to a few stations, the vast majority of them don’t have their own power system or have only minimal solar canopies.

Back in 2016, I asked Musk about this, and he said that it would now happen as Tesla had the “pieces now in place” with Supercharger V3, Powerpack V2, and SolarCity:

Advertisement - scroll for more content

All of these pieces have been in place for years, and Tesla has now discontinued the Powerpack in favor of the Megapack. The Supercharger network is also transitioning to V4 stations.

Yet, solar and battery deployment haven’t accelerated much in the decade since Musk made that comment, but it is finally happening.

Last year, Tesla announced a new project called ‘Oasis’, which consists of a new model Supercharger station with a solar farm and battery storage enabling off-grid operations in Lost Hills, California.

Tesla has now unveiled the project and turned on most of the Supercharger stalls:

The project consists of 168 chargers, with half of them currently operational, making it one of the largest Supercharger stations in the world. However, that’s not even the most notable aspect of it.

The station is equipped with 11 MW of ground-mounted solar panels and canopies, spanning 30 acres of land, and 10 Tesla Megapacks with a total energy storage capacity of 39 MWh.

It can be operated off-grid, which is the case right now, according to Tesla.

With off-grid operations, Tesla was about to bring 84 stalls online just in time for the Fourth of July travel weekend. The rest of the stalls and a lounge are going to open later this year.

Electrek’s Take

This is awesome. A bit late, but awesome. This is what charging stations should be like: fully powered by renewable energy.

Unfortunately, it will be much harder to open those stations in the future due to legislation that Trump and the Republican Party have just passed, which removes incentives for solar and energy storage, adds taxes on them, and removes incentives to build batteries – all things that have helped Tesla considerably over the last few years.

The US is likely going to have a few tough years for EV adoption and renewable energy deployment.

---

### Tesla
 launches Oasis Supercharger with solar farm and off-grid batteries (3 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Felectrek.co%2F2025%2F07%2F03%2Ftesla-launches-oasis-supercharger-with-solar-farm-off-grid-batteries%2F%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/aRW-2vTg-RYAJ7YcFM4QHshoT9Q-mH_Kx490UzqHmZQ=412
**TLDR Summary:** Tesla's Oasis Supercharger, an EV charging station with a solar farm and off-grid batteries, is now open in Lost Hills, California. The project consists of 168 chargers, half of which are currently operational. It is equipped with 11 MW of ground-mounted solar panels and canopies. Spanning 30 acres of land, it has 10 Tesla Megapacks with a total energy storage capacity of 39 MWh. The charging station can be operated off-grid. The rest of the stalls and a lounge will be open later this year.
**Full Article Content:**
Tesla has launched its new Oasis Supercharger, the long-promised EV charging station of the future, with a solar farm and off-grid batteries.

Early in the deployment of the Supercharger network, Tesla promised to add solar arrays and batteries to the Supercharger stations, and CEO Elon Musk even said that most stations would be able to operate off-grid.

While Tesla did add solar and batteries to a few stations, the vast majority of them don’t have their own power system or have only minimal solar canopies.

Back in 2016, I asked Musk about this, and he said that it would now happen as Tesla had the “pieces now in place” with Supercharger V3, Powerpack V2, and SolarCity:

Advertisement - scroll for more content

All of these pieces have been in place for years, and Tesla has now discontinued the Powerpack in favor of the Megapack. The Supercharger network is also transitioning to V4 stations.

Yet, solar and battery deployment haven’t accelerated much in the decade since Musk made that comment, but it is finally happening.

Last year, Tesla announced a new project called ‘Oasis’, which consists of a new model Supercharger station with a solar farm and battery storage enabling off-grid operations in Lost Hills, California.

Tesla has now unveiled the project and turned on most of the Supercharger stalls:

The project consists of 168 chargers, with half of them currently operational, making it one of the largest Supercharger stations in the world. However, that’s not even the most notable aspect of it.

The station is equipped with 11 MW of ground-mounted solar panels and canopies, spanning 30 acres of land, and 10 Tesla Megapacks with a total energy storage capacity of 39 MWh.

It can be operated off-grid, which is the case right now, according to Tesla.

With off-grid operations, Tesla was about to bring 84 stalls online just in time for the Fourth of July travel weekend. The rest of the stalls and a lounge are going to open later this year.

Electrek’s Take

This is awesome. A bit late, but awesome. This is what charging stations should be like: fully powered by renewable energy.

Unfortunately, it will be much harder to open those stations in the future due to legislation that Trump and the Republican Party have just passed, which removes incentives for solar and energy storage, adds taxes on them, and removes incentives to build batteries – all things that have helped Tesla considerably over the last few years.

The US is likely going to have a few tough years for EV adoption and renewable energy deployment.

---

### UK
 firm achieves tritium breakthrough, could boost nuclear fusion fuel supply (3 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Finterestingengineering.com%2Fenergy%2Fuk-firm-commercial-tritium-breakthrough%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/w_iicQjMsf7kDr87MtqFWxGdXVjv47xNzPmb44sK1EQ=412
**TLDR Summary:** UK-based private commercial fusion company Astral Systems claims to be the first firm to successfully breed tritium, a vital fusion fuel, using a fusion reactor. The achievement addresses a significant hurdle in the development of fusion energy. It clearly demonstrates a potential path to scalable tritium production, which could unlock a wide range of applications and capabilities. The ability to generate tritium within the reactor is crucial - a sustainable fusion energy system needs to produce more fuel than it consumes.
**Full Article Content:**
Astral Systems, a UK-based private commercial fusion company, has claimed to have become the first firm to successfully breed tritium, a vital fusion fuel, using its own operational fusion reactor.

This achievement, made with the University of Bristol, addresses a significant hurdle in the development of fusion energy.

The milestone came during a 55-hour Deuterium-Deuterium (DD) fusion irradiation campaign conducted in March. Scientists from Astral Systems and the University of Bristol produced and detected tritium in real-time from an experimental lithium breeder blanket within Astral’s multi-state fusion reactors.

---

## Programming, Design & Data Science

### Software
 engineering with LLMs in 2025: reality check (31 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fnewsletter.pragmaticengineer.com%2Fp%2Fsoftware-engineering-with-llms-in-2025%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/Udfgauco7DNILisc7h8lP90zO_CxoonxVC_beyG2QRc=412
**TLDR Summary:** Executives at AI infrastructure companies have made bold claims about the technology, but developers often find these claims to fall spectacularly flat. This article looks at how AI is used within the tech industry to see why founders/CEOs are more bullish than devs about AI tools, how widespread usage is among developers, how much time AI tools really save, and more. Many seasoned software engineers were skeptical about AI tools until very recently - now, most are surprisingly enthusiastic and see these tools as a change that will reshape software development.
**Full Article Content:**
Hi – this is Gergely with the monthly, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover challenges at Big Tech and startups through the lens of engineering managers and senior engineers. If you’ve been forwarded this email, you can subscribe here.

Two weeks ago, I gave a keynote at LDX3 in London, “Software engineering with GenAI.” During the weeks prior, I talked with software engineers at leading AI companies like Anthropic and Cursor, in Big Tech (Google, Amazon), at AI startups, and also with several seasoned software engineers, to get a sense of how teams are using various AI tools, and which trends stand out.

If you have 25 minutes to spare, check out an edited video version, which was just published on my YouTube channel. A big thank you to organizers of the LDX3 conference for the superb video production, and for organizing a standout event – including the live podcast recording (released tomorrow) and a book signing for The Software Engineer’s Guidebook.

Watch the recording of the keynote

My keynote at LDX3, in London

This article covers:

Twin extremes. Executives at AI infrastructure companies make bold claims, which developers often find fall spectacularly flat. AI dev tooling startups. Details from Anthropic, Anysphere, and Codeium, on how their engineers use Claude Code, Cursor, and Windsurf. Big Tech. How Google and Amazon use the tools, including how the online retail giant is quietly becoming an MCP-first company. AI startups. Oncall management startup, incident.io, and a biotech AI, share how they experiment with AI tools. Some tools stick and others are disappointments. Seasoned software engineers. Observations from experienced programmers, Armin Ronacher (creator of Flask), Peter Steinberger (founder of PSPDFKit), Birgitta Böckeler (Distinguished Engineer at Thoughtworks), Simon Willison (creator of Django), Kent Beck (creator of XP), and Martin Fowler (Chief Technologist at Thoughtworks). Open questions. Why are founders/CEOs more bullish than devs about AI tools, how widespread is usage among developers, how much time do AI tools really save, and more.

The bottom of this article could be cut off in some email clients. Read the full article uninterrupted, online.

Read the full article online

1. Twin extremes

There’s no shortage of predictions that LLMs and AI will change software engineering – or that they already have done. Let’s look at the two extremes.

Bull case: AI execs. Headlines about companies with horses in the AI race:

“Anthropic’s CEO said all code will be AI-generated in a year.” (Inc Magazine, March 2025).

“Microsoft's CEO reveals AI writes up to 30% of its code — some projects may have all code written by AI” (Tom’s Hardware, April 2025)

“Google chief scientist predicts AI could perform at the level of a junior coder within a year” (Business Insider, May 2025)

These are statements of confidence and success – and as someone working in tech, the last two might have some software engineers looking over their shoulders, worrying about job security. Still, it’s worth remembering who makes such statements: companies with AI products to sell. Of course they pump up its capabilities.

Bear case: disappointed devs. Two amusing examples about AI tools not exactly living up to the hype: the first from January, when coding tool Devin generated a bug that cost a team $733 in unnecessary costs by generating millions of PostHog analytics events:

While responsibility lies with the developer who accepted a commit without closer inspection, if an AI tool’s output is untrustworthy, then that tool is surely nowhere near to taking software engineers’ work.

Another case enjoyed with self-confessed schadenfreude by those not fully onboard with tech execs’ talk of hyper-productive AI, was the public preview of GitHub Copilot Agent, when the agent kept stumbling in the .NET codebase.

Fumbles included the agent adding tests that failed, with Microsoft software engineers needing to tell the agent to restart:

Microsoft deserves credit for not hiding away the troubles with its agent: the .NET repository has several pull requests opened by the agent which were closed because engineers gave up on getting workable results from the AI.

We cover more on this incident in the deepdive, Microsoft is dogfooding AI dev tools’ future.

So between bullish tech executives and unimpressed developers, what’s the truth? To get more details, I reached out to engineers at various types of companies, asking how they use AI tools now. Here’s what I learned…

2. AI dev tools startups

It’s harder to find more devs using AI tools for work than those at AI tooling companies which build tools for professionals, and dogfood their products.

Anthropic

The Anthropic team told me:

“When we gave Claude Code to our engineers and researchers, they all started using it every day, which was pretty surprising.”

Today, 90% of the code for Claude Code is written by Claude Code(!), Anthropic’s Chief Product Officer Mike Krieger says. And usage has risen sharply since 22 May – the launch day of Claude Sonnet 4 and Claude Code:

40%: how much Claude Code usage increased by on the launch day of Claude Sonnet 4

160%: Userbase growth in the month after launch

These numbers suggest Claude Code and Claude Sonnet 4 are hits among developers. Boris Cherny, creator of Claude Code, said this on the Latent Space podcast:

"Anecdotally for me, it's probably doubled my productivity. I think there are some engineers at Anthropic for whom it's probably 10x-ed their productivity."

MCP (Model Context Protocol) was created by Anthropic in November 2024. This is how it works:

MCP is gaining popularity and adoption across the industry:

November 2024 : Anthropic open sources MCP

December 2024 – February 2025 : Block, Replit, Windsurf, and Sourcegraph, adopt the protocol

March, April : OpenAI, Google, Microsoft also adopt it

Today: Thousands of active MCP servers operate, and adoption continues

We cover more about the protocol and its importance in MCP Protocol: a new AI dev tools building block.

Windsurf

Asked how they use their own product to build Windsurf, the team told me:

“~95% of our code is written using Windsurf’s agent Cascade and the passive coding feature, Windsurf Tab.”

Some non-engineers at the company also use Windsurf. Gardner Johnson, Head of Partnerships, used it to build his own quoting system, and replace an existing B2B vendor.

We previously covered How Windsurf is built with CEO Varun Mohan.

Cursor

~40-50% of Cursor’s code is written from output generated by Cursor, the engineering team at the dev tools startup estimated, when I asked. While this number is lower than Claude Code and Windsurf’s numbers, it’s still surprisingly high. Naturally, everyone at the company dogfoods Cursor and uses it daily.

We cover more on how Cursor is built in Real-world engineering challenges: building Cursor.

3. Big Tech

After talking with AI dev tools startups, I turned to engineers at Google and Amazon.

Google

From talking with five engineers at the search giant, it seems that when it comes to developer tooling, everything is custom-built internally. For example:

Borg : the Google version of Kubernetes. It predates Kubernetes, which was built by Google engineers, with learnings from Borg itself. We cover more on the history of Kubernetes with Kat Cosgrove.

Cider : the Google version of their IDE. Originally, it started off as a web-based editor. Later, a VS Code fork was created (called Cider-v). Today, this VS Code version is the “main” one and is simply called “Cider.”

Critique : in-house version of GitHub’s code review

Code Search: the internal Sourcegraph, which Code Search predates. Sourcegraph was inspired by Code Search. We previously covered Sourcegraph’s engineering culture.

The reason Google has “custom everything” for its tooling is because the tools are integrated tightly with each other. Among Big Tech, Google has the single best development tooling: everything works with everything else, and thanks to deep integrations, it’s no surprise Google added AI integrations to all of these tools:

Cider : Multi-line code completion Chat with LLM inside IDE for prompting Powered by Gemini As a current engineer told me: “Cider suggests CL [changelist – Google’s version of pull requests] descriptions, AI input on code reviews, AI auto complete. It has a chat interface like Cursor, but the UX is not as good.”

Critique : AI code review suggestions

CodeSearch: AI also integrated

An engineer told me that Google seems to be taking things “slow and steady” with developer tools:

“Generally, Google is taking a very cautious approach here to build trust. They definitely want to get it right the first time, so that software engineers (SWEs) can trust it.”

Other commonly-used tools:

Gemini: App and Gemini in Workspace features are usually dogfooded internally, and are available with unlimited usage for engineers

LLM prompt playground : works very similarly to OpenAI’s dev playground, and predates it

Internal LLM usage : various Gemini models are available for internal use: big and small, instruction-tuned, and more creative ones, thinking models and experimental ones.

MOMA search engine : knowledge base using LLMs. This is a chatbot fine-tuned with Google’s inside knowledge. The underlying model is based on some version of the Gemini model, but what it provides is pretty basic: answers to direct questions. Devs tell me MOMA is promising, but not as useful as some hoped, likely due to how dependent it is on internal documentation. For example, if a team’s service is badly documented and lacks references, the model wouldn’t do well on questions about it. And since all Google’s services are custom, the generic model knowledge doesn’t help (e.g., details about Kubernetes don’t necessarily apply to Borg!)

NotebookLM: heavily used. One use case is to feed in all product requirement documents / user experience researcher documents, and then ask questions about the contents. NotebookLM is a publicly available product.

Google keeps investing in “internal AI islands.” A current software engineer told me:

“There are many org-specific and team-specific GenAI tooling projects happening everywhere. This is because it’s what leadership likes to see, these days! Cynically: starting an AI project is partly how you get more funding these days. As to how effective this tooling is, who knows!”

I’d add that Google’s strategy of funding AI initiatives across the org might feel wasteful at first glance, but it’s exactly how successful products like NotebookLM were born. Google has more than enough capacity to fund hundreds of projects, and keep doubling down on those that win traction, or might generate hefty revenue.

Google is preparing for 10x more code to be shipped. A former Google Site Reliability Engineer (SRE) told me:

“What I’m hearing from SRE friends is that they are preparing for 10x the lines of code making their way into production.”

If any company has data on the likely impact of AI tools, it’s Google. 10x as much code generated will likely also mean 10x more:

Code review

Deployments

Feature flags

Source control footprint

… and, perhaps, even bugs and outages, if not handled with care

Amazon

I talked with six current software development engineers (SDEs) at the company for a sense of the tools they use.

Amazon Q Developer is Amazon’s own GitHub Copilot. Every developer has free access to the Pro tier and is strongly incentivized to use it. Amazon leadership and principal engineers at the company keep reminding everyone about it.

What I gather is that this tool was underwhelming at launch around two years ago because it only used Amazon’s in-house model, Nova. Nova was underwhelming, meaning Q was, too.

This April, that changed: Q did away with the Nova dependency and became a lot better. Around half of devs I spoke with now really like the new Q; it works well for AWS-related tasks, and also does better than other models in working with the Amazon codebase. This is because Amazon also trained a few internal LLMs on their own codebase, and Q can use these tailored models. Other impressions:

Limited to files. Amazon Q can currently only understand one file at a time — a limitations SDEs need to work around.

Works well with Java. If Amazon runs on one thing, it’s Java, so this is a great fit.

Finetuned models are only marginally better. Even models trained on Amazon’s own codebase feel only moderately better than non-trained models, surprisingly.

Cline hooked up to Bedrock is a popular alternative: A lot of SDEs prefer to use Cline hooked up to AWS Bedrock where they run a model (usually Sonnet 4)

Q CLI: the command line interface (CLI) is becoming very popular very quickly internally, thanks to this tool using the AWS CLI being able to directly hook up to MCP servers, of which Amazon has hundreds already (discussed below)

Q Transform: used for platform migrations internally, migrating from one language version (e.g. Java 8) to another (e.g. Java 11). It’s still hit-and-miss, said engineers: it works great with some internal services, and not others. Q transform is publicly available.

Amazon Q is a publicly available product and so far, the feedback I’m hearing from non-Amazon devs is mixed: it works better for AWS context, but a frequent complaint is how slow autocomplete is, even for paying customers. Companies paying for Amazon Q Pro are exploring snappier alternatives, like Cursor.

Claude Sonnet is another tool most Amazon SDEs use for any writing-related work. Amazon is a partner to Anthropic, which created these models, and SDEs can access Sonnet models easily – or just spin up their own instance on Bedrock. While devs could also use the more advanced Opus model, I’m told this model has persistent capacity problems – at least at present.

What SDEs are using the models for:

Writing PR/FAQ documents (also called “working backwards” documents). These documents are a big part of the culture, as covered in Inside Amazon’s engineering culture.

Writing performance review feedback for peers, and to generate self-reviews

Writing documentation

…any writing task which feels like a chore!

It’s worth considering what it would mean if more devs used LLMs to generate “mandatory” documents, instead of their own capabilities. Before LLMs, writing was a forcing function of thinking; it’s why Amazon has its culture of “writing things down.” There are cases where LLMs are genuinely helpful, like for self-review, where an LLM can go through PRs and JIRA tickets from the last 6 months to summarize work. But in many cases, LLMs generate a lot more text with much shorter prompts, so will the amount of time spent thinking about problems reduce with LLMs doing the writing?

Amazon to become “MCP-first?”

In 2002, Amazon founder and CEO Jeff Bezos introduced an “API mandate.” As former Amazon engineer Steve Yegge recalled:

“[Jeff Bezos’] Big Mandate went something along these lines: 1. All teams will henceforth expose their data and functionality through service interfaces. 2. Teams must communicate with each other through these interfaces. 3. There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another team's data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over the network. (...) 6. Anyone who doesn't do this will be fired. 7. Thank you; have a nice day! Ha, ha! Ex-Amazon folks will of course realize immediately that #7 was a little joke I threw in, because Bezos most definitely does not give a s**t about your day. #6 was real, so people went to work.”

Since the mid-2000s, Amazon has been an “API-first” company. Every service a team owned offered APIs for any other team to use. Amazon then started to make several of its services available externally, and we can see many of those APIs as today’s AWS services. In 2025, Amazon is a company with thousands of teams, thousands of services, and as many APIs as services.

Turning an API into an MCP server is trivial, which Amazon does at scale. It’s simple for teams that own APIs to turn them into MCP servers, and these MCP servers can be used by devs with their IDEs and agents to get things done. A current SDE told me:

“Most internal tools and websites already added MCP support. This means it’s trivial to hook up automation with an agent and the ticketing agent, email systems, or any other internal service with an API. You can chain pretty much everything!”

Another engineer elaborated:

“There’s even an internal amazon MCP server that hooks into our wiki, ticketing system, and Quip. The internal MCP also works with Q CLI. This integration steadily increased in popularity internally.”

Developers are often selectively lazy, and some have started to automate previously tedious workflows.

Amazon is likely the global leader in adopting MCP servers at scale, and all of this can be traced back to that 2002 mandate from Bezos pushing everyone to build APIs.

4. AI startups

Next, I turned to engineers working at startups building AI products, but not AI developer tools. I was curious about how much cutting-edge companies use LLMs for development.

incident .io

The startup is a platform for oncall, incident response, and status pages, and became AI-first in the past year, given how useful LLMs are in this area. (Note: I’m an investor in the company.)

Software engineer Lawrence Jones said:

“Our team is massively into using AI tools to accelerate them. Over the last couple of years we’ve… Seen many engineers adopt IDEs like Cursor and use them for both writing code and understanding it

Built Claude Code 'Projects' which contain our engineering documentation, so people can draft code in our style, according to our conventions and architecture preferences

Lots of the team use Granola to track notes from calls, sometimes grabbing a room to just talk to their phone about plans which they’ll later reformat into a doc Claude Code has been the biggest change, though. Our entire team are regular users. Claude Code is the interactive terminal app that runs an Anthropic agent to explore and modify your codebase.”

The team has a Slack channel where team members share their experience with AI tools for discussion. Lawrence shared a few screenshots of the types of learnings shared:

Using Linear MCP: sharing learnings with the team

Using Claude for research: sharing what worked with the rest of the team

Asking Claude for options: a few things that worked for an engineer

The startup feels like it’s in heavy experimentation mode with tools. Sharing learnings internally surely helps devs get a better feel for what works and what doesn’t.

Biotech AI startup

One startup asked not to be named because no AI tools have “stuck” for them just yet, and they’re not alone. But there’s pressure to not appear “anti-AI”, especially as theirs is a LLM-based business.

The company builds ML and AI models to design proteins, and much of the work is around building numerical and automated ML pipelines. The business is doing great, and has raised multiple rounds of funding, thanks to a product gaining traction within biology laboratories. The company employs a few dozen software engineers.

The team uses very few AI coding tools. Around half of devs use Vim or Helix as editors. The rest use VS Code or PyCharm – plus the “usual” Python tooling like Jupyter Notebooks. Tools like Cursor are not currently used by engineers, though they were trialled.

The company rolled out an AI code review tool, but found that 90% of AI comments were unhelpful. Despite the other 10% being good, the feedback felt too noisy. Here’s how an engineer at the company summarized things:

“We've experimented with several options with LLMs, but little has really stuck. It's still faster to just write correct code than to review LLM code and fix its problems, even using the latest models. Given the hype around LLMs, I speculate that we might just be in a weird niche.”

An interesting detail emerged when I asked how they would compare the impact of AI tools to other innovations in the field. This engineer said that for their domain, the impact of the uv project manager and ruff linter has been greater than AI tools, since uv made their development experience visibly faster!

Ruff is 10-100x faster than existing Python linters. Moving to this linter created a noticeable developer productivity gain for the biotech AI startup

It might be interesting to compare the impact of AI tools to other recent tools like ruff/uv. These have had a far greater impact.

This startup is a reminder that AI tools are not one-size-fits-all. The company is in an unusual niche where ML pipelines are far more common than at most companies, so the software they write will feel more atypical than at a “traditional” software company.

The startup keeps experimenting with anything that looks promising for developer productivity: they’ve found moving to high-performance Python libraries is a lot more impactful than using the latest AI tools and models; for now, that is!

5. Seasoned software engineers

Finally, I turned to a group of accomplished software engineers, who have been in the industry for years, and were considered standout tech professionals before AI tools started to spread.

Armin Ronacher: from skeptic to believer

Armin is the creator of Flask, a popular Python library, and was the first engineering hire at application monitoring scaleup, Sentry. He has been a developer professionally for 17 years, and was pretty unconvinced by AI tooling, until very recently. Then, a month ago he published a blog post, AI changes everything:

“If you would have told me even just six months ago that I'd prefer being an engineering lead to a virtual programmer intern over hitting the keys myself, I would not have believed it. I can go and make a coffee, and progress still happens. I can be at the playground with my youngest while work continues in the background. Even as I'm writing this blog post, Claude is doing some refactorings.”

I asked what changed his mind about the usefulness of these tools.

“A few things changed in the last few months: Claude Code got shockingly good. Not just in the quality of the code, but in how much I trust it. I used to be scared of giving it all permissions, now it's an acceptable risk to me – with some hand holding.

I learned more. I learned from others, and learned myself, about how to get it to make productivity gains

Clearing the hurdle of not accepting it, by using LLMs extensively. I was very skeptical; in particular, my usage of Cursor and similar code completion actually went down for a while because I was dissatisfied. The agentic flow, on the other hand, went from being not useful at all, to indispensable.

Agents change the game. Tool usage, custom tool usage, and agents writing their own tools to iterate, are massive game changers. The faults of the models are almost entirely avoided because they can run the code and see what happens. With Sonnet 3.7 and 4, I noticed a significant step up in the ability to use tools, even if the tools are previously unknown or agent created.”

Peter Steinberger: rediscovering a spark for creation

Peter Steinberger has been an iOS and Mac developer for 17 years, and is founder of PSPDFKit. In 2021, he sold all his shares in the company when PSPDFKit raised €100M in funding. He then started to tinker with building small projects on the side. Exactly one month ago, he published the post The spark returns. He writes:

“Right now, we are at an incredible crossroads in technology. AI is moving so fast and is changing the way we work in software development, but furthermore, it’s going to change the world. I haven’t been as excited, astounded, and amazed by any technology in a very long time.”

Indeed, something major did change for Pete: for the first time in ages he started to code regularly.

I asked what the trigger was that got him back to daily coding. Peter’s response:

“Tools got better. Models reached a stage where they are really capable, pricing went down: we're at this inflection point where suddenly things "just work", and especially with Cursor and Claude Code they became easy. Everyone can just open that thing on their project, type in what they want and it just happens. I see more and more folks getting infected by it. Once they see how capable this new generation of tools is, it doesn't take long before their excitement is through the roof. These tools fundamentally change how we build software. Suddenly, every side project is just a few sentences away, code becomes cheap, languages and frameworks matter less because it got incredibly simple to just switch. Combine that power with a capable engineer, and you easily create 10-20x the output. I see people left and right quitting their jobs to dedicate all their time to AI. My friend just said "it's the most exciting time since I started to learn programming”. Suddenly, I feel I can build anything I want.”

Pete emphasized:

“I’m telling you, [agentic AI tools] are the biggest shift, ever. Been talking to a bunch of engineers who wanna quit their job just because they wanna go all in on doing stuff with AI!”

Birgitta Böckeler: a new “lateral move” in development

Birgitta is a Distinguished Engineer at Thoughtworks, and has been writing code for 20 years. She has been experimenting with and researching GenAI tools for the last two years, and last week published Learnings from two years of using AI tools for software engineering in The Pragmatic Engineer. Talking with me, she summarized the state of GenAI tooling:

“We should embrace that GenAI is a lateral move and opportunity for something new, not a continuation of how we've abstracted and automated, previously. We now have this new tool that allows us to specify things in an unstructured way, and we can use it on any abstraction level. We can create low code applications with it, framework code, even Assembly. I find this lateral move much more exciting than thinking of natural language as "yet another abstraction level". LLMs open up a totally new way in from the side, which brings so many new opportunities.”

Simon Willison: “coding agents” actually work now

Simon has been a developer for 25 years, is the creator of Django, and works as an independent software engineer. He writes an interesting tech blog, documenting learnings from working with LLMs, daily. He was also the first-ever guest on The Pragmatic Engineer Podcast in AI tools for software engineers, but without the hype. I asked how he sees the current state of GenAI tools used for software development:

“Coding agents are a thing that actually work now: run an LLM in a loop, let it execute compilers and tests and linters and other tools, give it a goal, and watch it do the work for you. The models’ improvement in the last six months have tipped them over from fun toy demos, to being useful on a daily basis.”

Kent Beck: Having more fun than ever

Kent Beck is the creator of Extreme Programming (XP), an early advocate of Test Driven Development (TDD), and co-author of the Agile Manifesto. In a recent podcast episode he said:

“I’m having more fun programming than I ever had in 52 years.”

AI agents revitalized Kent, who says he feels he can take on more ambitious projects, and worry less about mastering the syntax of the latest framework being used. I asked if he’s seen other “step changes” for software engineering in the 50 years of his career, as what LLMs seem to provide. He said he has:

“I saw similar changes, impact-wise: Microprocessors (1970s) : the shift from mainframe computing

The internet (2000s): changed the digital economy

iPhone and Android (2010s): suddenly things like live location sharing is possible, and the percentage of time spent online sharply increased”

Martin Fowler: LLMs are a new nature of abstraction

Martin Fowler is Chief Scientist at Thoughworks, author of the book Refactoring, and a co-author of the Agile Manifesto. This is what he told me about LLMs:

“I think the appearance of LLMs will change software development to a similar degree as the change from assembler to the first high-level programming languages did. The further development of languages and frameworks increased our abstraction level and productivity, but didn't have that kind of impact on the nature of programming. LLMs are making the same degree of impact as high-level languages made versus the assembler. The distinction is that LLMs are not just raising the level of abstraction, but also forcing us to consider what it means to program with non-deterministic tools.”

Martin expands on his thoughts in the article, LLMs bring a new nature of abstraction.

6. Open questions

There are plenty of success stories in Big Tech, AI startups, and from veteran software engineers, about using AI tools for development. But many questions also remain, including:

#1: Why are founders and CEOs much more excited?

Founders and CEOs seem to be far more convinced of the breakthrough nature of AI tools for coding, than software engineers are. One software engineer-turned-founder and executive who runs Warp, an AI-powered command line startup, posted for help in convincing devs to stop dragging their feet on adopting LLMs for building software:

#2: How much do devs use AI?

Developer intelligence platform startup DX recently ran a study with 38,000 participants. It’s still not published, but I got access to it (note: I’m an investor at DX, and advise them). They asked developers whether they use AI tools at least once a week:

5 out of 10 devs use AI tools weekly across all companies (50%)

6 out of 10 devs use them weekly at “top” companies (62%)

On one hand, that is incredible adoption. GitHub Copilot launched with general availability 3 years ago, and Cursor launched just 2 years ago. For 50% of all developers to use AI-powered dev tools in such a short time feels like faster adoption than any tool has achieved, to date.

On the other hand, half of devs don’t even use these new tools once a week. It’s safe to assume many devs gave them a try, but decided against them, or their employer hasn’t invested.

#3: How much time does AI save devs, really?

In the same study, DX asked participants to estimate how much time these tools saved for them. On the median, it’s around 4 hours per week:

Source: a study by DX. Study yet to be published

Is four hours lots? It’s 10% of a 40-hour workweek, which is certainly meaningful. But it is nowhere near the amounts reported in the media: like Sam Altman’s claim that AI could make engineers 10x as productive.

Google CEO Sundar Pichai also estimated that the company is seeing 10% productivity increase thanks to AI tools on a Lex Fridman podcast episode, which roughly matches the DX study.

This number feels grounded to me: devs don’t spend all their time coding, after all! There’s a lot of thinking and talking with others, admin work, code reviews, and much else to do.

#4: Why don’t AI tools work so great for orgs?

Laura Tacho, CTO at DX told me:

“These GenAI tools are great for the individual developer right now, but not yet that good at the organizational level.”

This observation makes sense: increasing coding output will not lead to faster software production, automatically; not without increasing code review throughout, deployment frequency, doing more testing (as more code likely means more bugs), and adapting the whole “software development pipeline” to make use of faster coding.

Plus, there’s the issue that some things simply take time: planning, testing, gathering feedback from users and customers, etc. Even if code is generated in milliseconds, other real-world constraints don’t just vanish.

#5: Lack of buzz among devs

I left this question to last: why do many developers not believe in LLMs’ usefulness, before they try it out? It’s likely to do with the theory that LLMs are less useful in practice, then they theoretically should be.

Simon Willison has an interesting observation, which he shared on the podcast:

“Right now, if you start with the theory, it will hold you back. With LLMs, it's weirdly harmful to spend too much time trying to understand how they actually work, before you start playing with them, which is very unintuitive. I have friends who say that if you're a machine learning researcher, if you've been training models and stuff for years, you're actually more disadvantaged when starting to use these tools, than if you come in completely fresh! That’s because LLMs are very weird; they don't react like you expect from other machine learning models.”

Takeaways

Summarizing the different groups which use LLMs for development, there’s surprising contributions from each:

I’m not too surprised about the first three groups:

AI dev tools startups: their existence depends on selling tools to devs, so it’s only natural they’d “eat their own dogfood”

Big Tech: companies like Google and Amazon are very profitable and want to protect their technology advantage, so will invest heavily in any technology that could disrupt them, and incentivize engineers to use these tools; especially home grown ones, like Google’s Gemini and Amazon’s Q.

AI startups: these are innovative companies, so it’s little surprise they experiment with AI dev tools. I found it refreshing to talk to a startup where the new tools don’t work that well, yet.

The last one is where I pay a lot more attention. For seasoned software engineers: most of these folks had doubts, and were sceptical about AI tools until very recently. Now, most are surprisingly enthusiastic, and see AI dev tools as a step change that will reshape how we do software development.

LLMs are a new tool for building software that us engineers should become hands-on with. There seems to have been a breakthrough with AI agents like Claude Code in the last few months. Agents that can now “use” the command line to get feedback about suggested changes: and thanks to this addition, they have become much more capable than their predecessors.

As Kent Beck put it in our conversation:

“The whole landscape of what's ‘cheap’ and what's ‘expensive’ has shifted. Things that we didn't do because we assumed they were expensive or hard, just got ridiculously cheap. So, we just have to be trying stuff!”

It’s time to experiment! If there is one takeaway, it would be to try out tools like Claude Code/OpenAI Codex/Amp/Gemini CLI/Amazon Q CLI (with AWS CLI integration), editors like Cursor/Windsurf/VS Code with Copilot, other tools like Cline, Aider, Zed – and indeed anything that looks interesting. We’re in for exciting times, as a new category of tools are built that will be as commonplace in a few years as using a visual IDE, or utilizing Git as a source control, is today.

---

### Software
 engineering with LLMs in 2025: reality check (31 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fnewsletter.pragmaticengineer.com%2Fp%2Fsoftware-engineering-with-llms-in-2025%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/Udfgauco7DNILisc7h8lP90zO_CxoonxVC_beyG2QRc=412
**TLDR Summary:** Executives at AI infrastructure companies have made bold claims about the technology, but developers often find these claims to fall spectacularly flat. This article looks at how AI is used within the tech industry to see why founders/CEOs are more bullish than devs about AI tools, how widespread usage is among developers, how much time AI tools really save, and more. Many seasoned software engineers were skeptical about AI tools until very recently - now, most are surprisingly enthusiastic and see these tools as a change that will reshape software development.
**Full Article Content:**
Hi – this is Gergely with the monthly, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover challenges at Big Tech and startups through the lens of engineering managers and senior engineers. If you’ve been forwarded this email, you can subscribe here.

Two weeks ago, I gave a keynote at LDX3 in London, “Software engineering with GenAI.” During the weeks prior, I talked with software engineers at leading AI companies like Anthropic and Cursor, in Big Tech (Google, Amazon), at AI startups, and also with several seasoned software engineers, to get a sense of how teams are using various AI tools, and which trends stand out.

If you have 25 minutes to spare, check out an edited video version, which was just published on my YouTube channel. A big thank you to organizers of the LDX3 conference for the superb video production, and for organizing a standout event – including the live podcast recording (released tomorrow) and a book signing for The Software Engineer’s Guidebook.

Watch the recording of the keynote

My keynote at LDX3, in London

This article covers:

Twin extremes. Executives at AI infrastructure companies make bold claims, which developers often find fall spectacularly flat. AI dev tooling startups. Details from Anthropic, Anysphere, and Codeium, on how their engineers use Claude Code, Cursor, and Windsurf. Big Tech. How Google and Amazon use the tools, including how the online retail giant is quietly becoming an MCP-first company. AI startups. Oncall management startup, incident.io, and a biotech AI, share how they experiment with AI tools. Some tools stick and others are disappointments. Seasoned software engineers. Observations from experienced programmers, Armin Ronacher (creator of Flask), Peter Steinberger (founder of PSPDFKit), Birgitta Böckeler (Distinguished Engineer at Thoughtworks), Simon Willison (creator of Django), Kent Beck (creator of XP), and Martin Fowler (Chief Technologist at Thoughtworks). Open questions. Why are founders/CEOs more bullish than devs about AI tools, how widespread is usage among developers, how much time do AI tools really save, and more.

The bottom of this article could be cut off in some email clients. Read the full article uninterrupted, online.

Read the full article online

1. Twin extremes

There’s no shortage of predictions that LLMs and AI will change software engineering – or that they already have done. Let’s look at the two extremes.

Bull case: AI execs. Headlines about companies with horses in the AI race:

“Anthropic’s CEO said all code will be AI-generated in a year.” (Inc Magazine, March 2025).

“Microsoft's CEO reveals AI writes up to 30% of its code — some projects may have all code written by AI” (Tom’s Hardware, April 2025)

“Google chief scientist predicts AI could perform at the level of a junior coder within a year” (Business Insider, May 2025)

These are statements of confidence and success – and as someone working in tech, the last two might have some software engineers looking over their shoulders, worrying about job security. Still, it’s worth remembering who makes such statements: companies with AI products to sell. Of course they pump up its capabilities.

Bear case: disappointed devs. Two amusing examples about AI tools not exactly living up to the hype: the first from January, when coding tool Devin generated a bug that cost a team $733 in unnecessary costs by generating millions of PostHog analytics events:

While responsibility lies with the developer who accepted a commit without closer inspection, if an AI tool’s output is untrustworthy, then that tool is surely nowhere near to taking software engineers’ work.

Another case enjoyed with self-confessed schadenfreude by those not fully onboard with tech execs’ talk of hyper-productive AI, was the public preview of GitHub Copilot Agent, when the agent kept stumbling in the .NET codebase.

Fumbles included the agent adding tests that failed, with Microsoft software engineers needing to tell the agent to restart:

Microsoft deserves credit for not hiding away the troubles with its agent: the .NET repository has several pull requests opened by the agent which were closed because engineers gave up on getting workable results from the AI.

We cover more on this incident in the deepdive, Microsoft is dogfooding AI dev tools’ future.

So between bullish tech executives and unimpressed developers, what’s the truth? To get more details, I reached out to engineers at various types of companies, asking how they use AI tools now. Here’s what I learned…

2. AI dev tools startups

It’s harder to find more devs using AI tools for work than those at AI tooling companies which build tools for professionals, and dogfood their products.

Anthropic

The Anthropic team told me:

“When we gave Claude Code to our engineers and researchers, they all started using it every day, which was pretty surprising.”

Today, 90% of the code for Claude Code is written by Claude Code(!), Anthropic’s Chief Product Officer Mike Krieger says. And usage has risen sharply since 22 May – the launch day of Claude Sonnet 4 and Claude Code:

40%: how much Claude Code usage increased by on the launch day of Claude Sonnet 4

160%: Userbase growth in the month after launch

These numbers suggest Claude Code and Claude Sonnet 4 are hits among developers. Boris Cherny, creator of Claude Code, said this on the Latent Space podcast:

"Anecdotally for me, it's probably doubled my productivity. I think there are some engineers at Anthropic for whom it's probably 10x-ed their productivity."

MCP (Model Context Protocol) was created by Anthropic in November 2024. This is how it works:

MCP is gaining popularity and adoption across the industry:

November 2024 : Anthropic open sources MCP

December 2024 – February 2025 : Block, Replit, Windsurf, and Sourcegraph, adopt the protocol

March, April : OpenAI, Google, Microsoft also adopt it

Today: Thousands of active MCP servers operate, and adoption continues

We cover more about the protocol and its importance in MCP Protocol: a new AI dev tools building block.

Windsurf

Asked how they use their own product to build Windsurf, the team told me:

“~95% of our code is written using Windsurf’s agent Cascade and the passive coding feature, Windsurf Tab.”

Some non-engineers at the company also use Windsurf. Gardner Johnson, Head of Partnerships, used it to build his own quoting system, and replace an existing B2B vendor.

We previously covered How Windsurf is built with CEO Varun Mohan.

Cursor

~40-50% of Cursor’s code is written from output generated by Cursor, the engineering team at the dev tools startup estimated, when I asked. While this number is lower than Claude Code and Windsurf’s numbers, it’s still surprisingly high. Naturally, everyone at the company dogfoods Cursor and uses it daily.

We cover more on how Cursor is built in Real-world engineering challenges: building Cursor.

3. Big Tech

After talking with AI dev tools startups, I turned to engineers at Google and Amazon.

Google

From talking with five engineers at the search giant, it seems that when it comes to developer tooling, everything is custom-built internally. For example:

Borg : the Google version of Kubernetes. It predates Kubernetes, which was built by Google engineers, with learnings from Borg itself. We cover more on the history of Kubernetes with Kat Cosgrove.

Cider : the Google version of their IDE. Originally, it started off as a web-based editor. Later, a VS Code fork was created (called Cider-v). Today, this VS Code version is the “main” one and is simply called “Cider.”

Critique : in-house version of GitHub’s code review

Code Search: the internal Sourcegraph, which Code Search predates. Sourcegraph was inspired by Code Search. We previously covered Sourcegraph’s engineering culture.

The reason Google has “custom everything” for its tooling is because the tools are integrated tightly with each other. Among Big Tech, Google has the single best development tooling: everything works with everything else, and thanks to deep integrations, it’s no surprise Google added AI integrations to all of these tools:

Cider : Multi-line code completion Chat with LLM inside IDE for prompting Powered by Gemini As a current engineer told me: “Cider suggests CL [changelist – Google’s version of pull requests] descriptions, AI input on code reviews, AI auto complete. It has a chat interface like Cursor, but the UX is not as good.”

Critique : AI code review suggestions

CodeSearch: AI also integrated

An engineer told me that Google seems to be taking things “slow and steady” with developer tools:

“Generally, Google is taking a very cautious approach here to build trust. They definitely want to get it right the first time, so that software engineers (SWEs) can trust it.”

Other commonly-used tools:

Gemini: App and Gemini in Workspace features are usually dogfooded internally, and are available with unlimited usage for engineers

LLM prompt playground : works very similarly to OpenAI’s dev playground, and predates it

Internal LLM usage : various Gemini models are available for internal use: big and small, instruction-tuned, and more creative ones, thinking models and experimental ones.

MOMA search engine : knowledge base using LLMs. This is a chatbot fine-tuned with Google’s inside knowledge. The underlying model is based on some version of the Gemini model, but what it provides is pretty basic: answers to direct questions. Devs tell me MOMA is promising, but not as useful as some hoped, likely due to how dependent it is on internal documentation. For example, if a team’s service is badly documented and lacks references, the model wouldn’t do well on questions about it. And since all Google’s services are custom, the generic model knowledge doesn’t help (e.g., details about Kubernetes don’t necessarily apply to Borg!)

NotebookLM: heavily used. One use case is to feed in all product requirement documents / user experience researcher documents, and then ask questions about the contents. NotebookLM is a publicly available product.

Google keeps investing in “internal AI islands.” A current software engineer told me:

“There are many org-specific and team-specific GenAI tooling projects happening everywhere. This is because it’s what leadership likes to see, these days! Cynically: starting an AI project is partly how you get more funding these days. As to how effective this tooling is, who knows!”

I’d add that Google’s strategy of funding AI initiatives across the org might feel wasteful at first glance, but it’s exactly how successful products like NotebookLM were born. Google has more than enough capacity to fund hundreds of projects, and keep doubling down on those that win traction, or might generate hefty revenue.

Google is preparing for 10x more code to be shipped. A former Google Site Reliability Engineer (SRE) told me:

“What I’m hearing from SRE friends is that they are preparing for 10x the lines of code making their way into production.”

If any company has data on the likely impact of AI tools, it’s Google. 10x as much code generated will likely also mean 10x more:

Code review

Deployments

Feature flags

Source control footprint

… and, perhaps, even bugs and outages, if not handled with care

Amazon

I talked with six current software development engineers (SDEs) at the company for a sense of the tools they use.

Amazon Q Developer is Amazon’s own GitHub Copilot. Every developer has free access to the Pro tier and is strongly incentivized to use it. Amazon leadership and principal engineers at the company keep reminding everyone about it.

What I gather is that this tool was underwhelming at launch around two years ago because it only used Amazon’s in-house model, Nova. Nova was underwhelming, meaning Q was, too.

This April, that changed: Q did away with the Nova dependency and became a lot better. Around half of devs I spoke with now really like the new Q; it works well for AWS-related tasks, and also does better than other models in working with the Amazon codebase. This is because Amazon also trained a few internal LLMs on their own codebase, and Q can use these tailored models. Other impressions:

Limited to files. Amazon Q can currently only understand one file at a time — a limitations SDEs need to work around.

Works well with Java. If Amazon runs on one thing, it’s Java, so this is a great fit.

Finetuned models are only marginally better. Even models trained on Amazon’s own codebase feel only moderately better than non-trained models, surprisingly.

Cline hooked up to Bedrock is a popular alternative: A lot of SDEs prefer to use Cline hooked up to AWS Bedrock where they run a model (usually Sonnet 4)

Q CLI: the command line interface (CLI) is becoming very popular very quickly internally, thanks to this tool using the AWS CLI being able to directly hook up to MCP servers, of which Amazon has hundreds already (discussed below)

Q Transform: used for platform migrations internally, migrating from one language version (e.g. Java 8) to another (e.g. Java 11). It’s still hit-and-miss, said engineers: it works great with some internal services, and not others. Q transform is publicly available.

Amazon Q is a publicly available product and so far, the feedback I’m hearing from non-Amazon devs is mixed: it works better for AWS context, but a frequent complaint is how slow autocomplete is, even for paying customers. Companies paying for Amazon Q Pro are exploring snappier alternatives, like Cursor.

Claude Sonnet is another tool most Amazon SDEs use for any writing-related work. Amazon is a partner to Anthropic, which created these models, and SDEs can access Sonnet models easily – or just spin up their own instance on Bedrock. While devs could also use the more advanced Opus model, I’m told this model has persistent capacity problems – at least at present.

What SDEs are using the models for:

Writing PR/FAQ documents (also called “working backwards” documents). These documents are a big part of the culture, as covered in Inside Amazon’s engineering culture.

Writing performance review feedback for peers, and to generate self-reviews

Writing documentation

…any writing task which feels like a chore!

It’s worth considering what it would mean if more devs used LLMs to generate “mandatory” documents, instead of their own capabilities. Before LLMs, writing was a forcing function of thinking; it’s why Amazon has its culture of “writing things down.” There are cases where LLMs are genuinely helpful, like for self-review, where an LLM can go through PRs and JIRA tickets from the last 6 months to summarize work. But in many cases, LLMs generate a lot more text with much shorter prompts, so will the amount of time spent thinking about problems reduce with LLMs doing the writing?

Amazon to become “MCP-first?”

In 2002, Amazon founder and CEO Jeff Bezos introduced an “API mandate.” As former Amazon engineer Steve Yegge recalled:

“[Jeff Bezos’] Big Mandate went something along these lines: 1. All teams will henceforth expose their data and functionality through service interfaces. 2. Teams must communicate with each other through these interfaces. 3. There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another team's data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over the network. (...) 6. Anyone who doesn't do this will be fired. 7. Thank you; have a nice day! Ha, ha! Ex-Amazon folks will of course realize immediately that #7 was a little joke I threw in, because Bezos most definitely does not give a s**t about your day. #6 was real, so people went to work.”

Since the mid-2000s, Amazon has been an “API-first” company. Every service a team owned offered APIs for any other team to use. Amazon then started to make several of its services available externally, and we can see many of those APIs as today’s AWS services. In 2025, Amazon is a company with thousands of teams, thousands of services, and as many APIs as services.

Turning an API into an MCP server is trivial, which Amazon does at scale. It’s simple for teams that own APIs to turn them into MCP servers, and these MCP servers can be used by devs with their IDEs and agents to get things done. A current SDE told me:

“Most internal tools and websites already added MCP support. This means it’s trivial to hook up automation with an agent and the ticketing agent, email systems, or any other internal service with an API. You can chain pretty much everything!”

Another engineer elaborated:

“There’s even an internal amazon MCP server that hooks into our wiki, ticketing system, and Quip. The internal MCP also works with Q CLI. This integration steadily increased in popularity internally.”

Developers are often selectively lazy, and some have started to automate previously tedious workflows.

Amazon is likely the global leader in adopting MCP servers at scale, and all of this can be traced back to that 2002 mandate from Bezos pushing everyone to build APIs.

4. AI startups

Next, I turned to engineers working at startups building AI products, but not AI developer tools. I was curious about how much cutting-edge companies use LLMs for development.

incident .io

The startup is a platform for oncall, incident response, and status pages, and became AI-first in the past year, given how useful LLMs are in this area. (Note: I’m an investor in the company.)

Software engineer Lawrence Jones said:

“Our team is massively into using AI tools to accelerate them. Over the last couple of years we’ve… Seen many engineers adopt IDEs like Cursor and use them for both writing code and understanding it

Built Claude Code 'Projects' which contain our engineering documentation, so people can draft code in our style, according to our conventions and architecture preferences

Lots of the team use Granola to track notes from calls, sometimes grabbing a room to just talk to their phone about plans which they’ll later reformat into a doc Claude Code has been the biggest change, though. Our entire team are regular users. Claude Code is the interactive terminal app that runs an Anthropic agent to explore and modify your codebase.”

The team has a Slack channel where team members share their experience with AI tools for discussion. Lawrence shared a few screenshots of the types of learnings shared:

Using Linear MCP: sharing learnings with the team

Using Claude for research: sharing what worked with the rest of the team

Asking Claude for options: a few things that worked for an engineer

The startup feels like it’s in heavy experimentation mode with tools. Sharing learnings internally surely helps devs get a better feel for what works and what doesn’t.

Biotech AI startup

One startup asked not to be named because no AI tools have “stuck” for them just yet, and they’re not alone. But there’s pressure to not appear “anti-AI”, especially as theirs is a LLM-based business.

The company builds ML and AI models to design proteins, and much of the work is around building numerical and automated ML pipelines. The business is doing great, and has raised multiple rounds of funding, thanks to a product gaining traction within biology laboratories. The company employs a few dozen software engineers.

The team uses very few AI coding tools. Around half of devs use Vim or Helix as editors. The rest use VS Code or PyCharm – plus the “usual” Python tooling like Jupyter Notebooks. Tools like Cursor are not currently used by engineers, though they were trialled.

The company rolled out an AI code review tool, but found that 90% of AI comments were unhelpful. Despite the other 10% being good, the feedback felt too noisy. Here’s how an engineer at the company summarized things:

“We've experimented with several options with LLMs, but little has really stuck. It's still faster to just write correct code than to review LLM code and fix its problems, even using the latest models. Given the hype around LLMs, I speculate that we might just be in a weird niche.”

An interesting detail emerged when I asked how they would compare the impact of AI tools to other innovations in the field. This engineer said that for their domain, the impact of the uv project manager and ruff linter has been greater than AI tools, since uv made their development experience visibly faster!

Ruff is 10-100x faster than existing Python linters. Moving to this linter created a noticeable developer productivity gain for the biotech AI startup

It might be interesting to compare the impact of AI tools to other recent tools like ruff/uv. These have had a far greater impact.

This startup is a reminder that AI tools are not one-size-fits-all. The company is in an unusual niche where ML pipelines are far more common than at most companies, so the software they write will feel more atypical than at a “traditional” software company.

The startup keeps experimenting with anything that looks promising for developer productivity: they’ve found moving to high-performance Python libraries is a lot more impactful than using the latest AI tools and models; for now, that is!

5. Seasoned software engineers

Finally, I turned to a group of accomplished software engineers, who have been in the industry for years, and were considered standout tech professionals before AI tools started to spread.

Armin Ronacher: from skeptic to believer

Armin is the creator of Flask, a popular Python library, and was the first engineering hire at application monitoring scaleup, Sentry. He has been a developer professionally for 17 years, and was pretty unconvinced by AI tooling, until very recently. Then, a month ago he published a blog post, AI changes everything:

“If you would have told me even just six months ago that I'd prefer being an engineering lead to a virtual programmer intern over hitting the keys myself, I would not have believed it. I can go and make a coffee, and progress still happens. I can be at the playground with my youngest while work continues in the background. Even as I'm writing this blog post, Claude is doing some refactorings.”

I asked what changed his mind about the usefulness of these tools.

“A few things changed in the last few months: Claude Code got shockingly good. Not just in the quality of the code, but in how much I trust it. I used to be scared of giving it all permissions, now it's an acceptable risk to me – with some hand holding.

I learned more. I learned from others, and learned myself, about how to get it to make productivity gains

Clearing the hurdle of not accepting it, by using LLMs extensively. I was very skeptical; in particular, my usage of Cursor and similar code completion actually went down for a while because I was dissatisfied. The agentic flow, on the other hand, went from being not useful at all, to indispensable.

Agents change the game. Tool usage, custom tool usage, and agents writing their own tools to iterate, are massive game changers. The faults of the models are almost entirely avoided because they can run the code and see what happens. With Sonnet 3.7 and 4, I noticed a significant step up in the ability to use tools, even if the tools are previously unknown or agent created.”

Peter Steinberger: rediscovering a spark for creation

Peter Steinberger has been an iOS and Mac developer for 17 years, and is founder of PSPDFKit. In 2021, he sold all his shares in the company when PSPDFKit raised €100M in funding. He then started to tinker with building small projects on the side. Exactly one month ago, he published the post The spark returns. He writes:

“Right now, we are at an incredible crossroads in technology. AI is moving so fast and is changing the way we work in software development, but furthermore, it’s going to change the world. I haven’t been as excited, astounded, and amazed by any technology in a very long time.”

Indeed, something major did change for Pete: for the first time in ages he started to code regularly.

I asked what the trigger was that got him back to daily coding. Peter’s response:

“Tools got better. Models reached a stage where they are really capable, pricing went down: we're at this inflection point where suddenly things "just work", and especially with Cursor and Claude Code they became easy. Everyone can just open that thing on their project, type in what they want and it just happens. I see more and more folks getting infected by it. Once they see how capable this new generation of tools is, it doesn't take long before their excitement is through the roof. These tools fundamentally change how we build software. Suddenly, every side project is just a few sentences away, code becomes cheap, languages and frameworks matter less because it got incredibly simple to just switch. Combine that power with a capable engineer, and you easily create 10-20x the output. I see people left and right quitting their jobs to dedicate all their time to AI. My friend just said "it's the most exciting time since I started to learn programming”. Suddenly, I feel I can build anything I want.”

Pete emphasized:

“I’m telling you, [agentic AI tools] are the biggest shift, ever. Been talking to a bunch of engineers who wanna quit their job just because they wanna go all in on doing stuff with AI!”

Birgitta Böckeler: a new “lateral move” in development

Birgitta is a Distinguished Engineer at Thoughtworks, and has been writing code for 20 years. She has been experimenting with and researching GenAI tools for the last two years, and last week published Learnings from two years of using AI tools for software engineering in The Pragmatic Engineer. Talking with me, she summarized the state of GenAI tooling:

“We should embrace that GenAI is a lateral move and opportunity for something new, not a continuation of how we've abstracted and automated, previously. We now have this new tool that allows us to specify things in an unstructured way, and we can use it on any abstraction level. We can create low code applications with it, framework code, even Assembly. I find this lateral move much more exciting than thinking of natural language as "yet another abstraction level". LLMs open up a totally new way in from the side, which brings so many new opportunities.”

Simon Willison: “coding agents” actually work now

Simon has been a developer for 25 years, is the creator of Django, and works as an independent software engineer. He writes an interesting tech blog, documenting learnings from working with LLMs, daily. He was also the first-ever guest on The Pragmatic Engineer Podcast in AI tools for software engineers, but without the hype. I asked how he sees the current state of GenAI tools used for software development:

“Coding agents are a thing that actually work now: run an LLM in a loop, let it execute compilers and tests and linters and other tools, give it a goal, and watch it do the work for you. The models’ improvement in the last six months have tipped them over from fun toy demos, to being useful on a daily basis.”

Kent Beck: Having more fun than ever

Kent Beck is the creator of Extreme Programming (XP), an early advocate of Test Driven Development (TDD), and co-author of the Agile Manifesto. In a recent podcast episode he said:

“I’m having more fun programming than I ever had in 52 years.”

AI agents revitalized Kent, who says he feels he can take on more ambitious projects, and worry less about mastering the syntax of the latest framework being used. I asked if he’s seen other “step changes” for software engineering in the 50 years of his career, as what LLMs seem to provide. He said he has:

“I saw similar changes, impact-wise: Microprocessors (1970s) : the shift from mainframe computing

The internet (2000s): changed the digital economy

iPhone and Android (2010s): suddenly things like live location sharing is possible, and the percentage of time spent online sharply increased”

Martin Fowler: LLMs are a new nature of abstraction

Martin Fowler is Chief Scientist at Thoughworks, author of the book Refactoring, and a co-author of the Agile Manifesto. This is what he told me about LLMs:

“I think the appearance of LLMs will change software development to a similar degree as the change from assembler to the first high-level programming languages did. The further development of languages and frameworks increased our abstraction level and productivity, but didn't have that kind of impact on the nature of programming. LLMs are making the same degree of impact as high-level languages made versus the assembler. The distinction is that LLMs are not just raising the level of abstraction, but also forcing us to consider what it means to program with non-deterministic tools.”

Martin expands on his thoughts in the article, LLMs bring a new nature of abstraction.

6. Open questions

There are plenty of success stories in Big Tech, AI startups, and from veteran software engineers, about using AI tools for development. But many questions also remain, including:

#1: Why are founders and CEOs much more excited?

Founders and CEOs seem to be far more convinced of the breakthrough nature of AI tools for coding, than software engineers are. One software engineer-turned-founder and executive who runs Warp, an AI-powered command line startup, posted for help in convincing devs to stop dragging their feet on adopting LLMs for building software:

#2: How much do devs use AI?

Developer intelligence platform startup DX recently ran a study with 38,000 participants. It’s still not published, but I got access to it (note: I’m an investor at DX, and advise them). They asked developers whether they use AI tools at least once a week:

5 out of 10 devs use AI tools weekly across all companies (50%)

6 out of 10 devs use them weekly at “top” companies (62%)

On one hand, that is incredible adoption. GitHub Copilot launched with general availability 3 years ago, and Cursor launched just 2 years ago. For 50% of all developers to use AI-powered dev tools in such a short time feels like faster adoption than any tool has achieved, to date.

On the other hand, half of devs don’t even use these new tools once a week. It’s safe to assume many devs gave them a try, but decided against them, or their employer hasn’t invested.

#3: How much time does AI save devs, really?

In the same study, DX asked participants to estimate how much time these tools saved for them. On the median, it’s around 4 hours per week:

Source: a study by DX. Study yet to be published

Is four hours lots? It’s 10% of a 40-hour workweek, which is certainly meaningful. But it is nowhere near the amounts reported in the media: like Sam Altman’s claim that AI could make engineers 10x as productive.

Google CEO Sundar Pichai also estimated that the company is seeing 10% productivity increase thanks to AI tools on a Lex Fridman podcast episode, which roughly matches the DX study.

This number feels grounded to me: devs don’t spend all their time coding, after all! There’s a lot of thinking and talking with others, admin work, code reviews, and much else to do.

#4: Why don’t AI tools work so great for orgs?

Laura Tacho, CTO at DX told me:

“These GenAI tools are great for the individual developer right now, but not yet that good at the organizational level.”

This observation makes sense: increasing coding output will not lead to faster software production, automatically; not without increasing code review throughout, deployment frequency, doing more testing (as more code likely means more bugs), and adapting the whole “software development pipeline” to make use of faster coding.

Plus, there’s the issue that some things simply take time: planning, testing, gathering feedback from users and customers, etc. Even if code is generated in milliseconds, other real-world constraints don’t just vanish.

#5: Lack of buzz among devs

I left this question to last: why do many developers not believe in LLMs’ usefulness, before they try it out? It’s likely to do with the theory that LLMs are less useful in practice, then they theoretically should be.

Simon Willison has an interesting observation, which he shared on the podcast:

“Right now, if you start with the theory, it will hold you back. With LLMs, it's weirdly harmful to spend too much time trying to understand how they actually work, before you start playing with them, which is very unintuitive. I have friends who say that if you're a machine learning researcher, if you've been training models and stuff for years, you're actually more disadvantaged when starting to use these tools, than if you come in completely fresh! That’s because LLMs are very weird; they don't react like you expect from other machine learning models.”

Takeaways

Summarizing the different groups which use LLMs for development, there’s surprising contributions from each:

I’m not too surprised about the first three groups:

AI dev tools startups: their existence depends on selling tools to devs, so it’s only natural they’d “eat their own dogfood”

Big Tech: companies like Google and Amazon are very profitable and want to protect their technology advantage, so will invest heavily in any technology that could disrupt them, and incentivize engineers to use these tools; especially home grown ones, like Google’s Gemini and Amazon’s Q.

AI startups: these are innovative companies, so it’s little surprise they experiment with AI dev tools. I found it refreshing to talk to a startup where the new tools don’t work that well, yet.

The last one is where I pay a lot more attention. For seasoned software engineers: most of these folks had doubts, and were sceptical about AI tools until very recently. Now, most are surprisingly enthusiastic, and see AI dev tools as a step change that will reshape how we do software development.

LLMs are a new tool for building software that us engineers should become hands-on with. There seems to have been a breakthrough with AI agents like Claude Code in the last few months. Agents that can now “use” the command line to get feedback about suggested changes: and thanks to this addition, they have become much more capable than their predecessors.

As Kent Beck put it in our conversation:

“The whole landscape of what's ‘cheap’ and what's ‘expensive’ has shifted. Things that we didn't do because we assumed they were expensive or hard, just got ridiculously cheap. So, we just have to be trying stuff!”

It’s time to experiment! If there is one takeaway, it would be to try out tools like Claude Code/OpenAI Codex/Amp/Gemini CLI/Amazon Q CLI (with AWS CLI integration), editors like Cursor/Windsurf/VS Code with Copilot, other tools like Cline, Aider, Zed – and indeed anything that looks interesting. We’re in for exciting times, as a new category of tools are built that will be as commonplace in a few years as using a visual IDE, or utilizing Git as a source control, is today.

---

### How
 to become passionate about delivering shareholder value (8 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.seangoedecke.com%2Fshareholder-value%2F%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/8kkFZv73VSrkFb6xoloa2eSVFm7lzYx0jMhtoPoxqHQ=412
**TLDR Summary:** Many engineers believe their jobs are to write good code, thinking that delivering shareholder value is the company's business, not theirs. Delivering shareholder value means making the company stock price go up and stay up. Shareholder value is part of the software design process - engineers should be connected to the financial goals of the company. Not all engineers are working in situations that can affect shareholder value, but those who work in more functional environments have a real opportunity to shape the financial situation of their companies, for good or ill.
**Full Article Content:**
I am passionate about delivering shareholder value. It feels kind of embarrassing to admit, but it’s true. I like all the things an engineer is supposed to like - writing elegant code, designing systems, solving hard technical problems - but I confess I don’t like those things as much as I like delivering shareholder value. That’s why I kind of enjoy the vibe shift that’s happened recently in tech. I wish my job was more secure, and my colleagues were happier, but I do really like the fact that my work is now much more tightly connected to the company’s strategy.

I think delivering shareholder value is underrated among software engineers. I have worked with many smart, competent engineers who believed that their job was to write good code, and if any shareholder value happened along the way that was the company’s business. To some degree this is a trauma response: when company strategy whipsaws around enough, engineers will give up on trying to follow it and just focus on the work directly in front of them. I’m sure there are also companies that structurally encourage this mindset (e.g. by punishing engineers who try and stick their noses into strategy discussions). But I also think that many engineers just haven’t heard the best case for why they ought to be focusing on shareholder value. I’m going to try to deliver that case now.

What is shareholder value?

First, what does “delivering shareholder value” mean? It sounds like vague corporate-speak. However, it’s actually not corporate-speak but finance-speak, and like most financial statements it has a very specific definition. Delivering shareholder value means making the company stock price go up and stay up.

That’s it! By itself, it’s not a very useful definition, since it’s not clear how connected my Jira ticket is to the Microsoft stock price. But engineers should be used to accurate-but-not-useful definitions in other domains. They’re often the first step on the road to having actual functional intuitions about the topic. We’ll get there, but right now I want to emphasize that “delivering shareholder value” is not vague or nonsense. It is a concrete idea.

Note: “and stay up” is a core part of the definition. I’m not talking about pure hype - that might temporarily raise the stock price, but at some point it’ll all come crashing down. The best way to deliver durable shareholder value is to build good products that people are willing to pay for. It’s probably possible to build a career around pumping out purely short-term value, but that’s not really what I’m interested in or what I’m writing about here.

Can engineers even impact shareholder value?

Although it’s hard to say exactly how, it’s foolish to think that an individual engineer has no impact on your company’s stock price. For one thing, tech companies make money from software, and the success or failure of a software project can obviously impact company stock price in many ways:

A delayed project can lead to an unimpressive yearly conference, lowering hype

A project that launches buggy or non-functional can shape customer sentiment for a long time

Successful projects can directly make money, increasing fundamentals, or cause hype

Visible enough failures - e.g. huge security incidents - can affect stock prices all on their own

The one thing everyone agreed on in my post about shipping is that delivering a successful project requires one single engineer to have all the context in their head. So engineers leading projects have a direct connection to shareholder value. But even if you’re not leading a project, you might still be instrumental in its success or failure. Successful or unsuccessful company departments often succeed or fail on the strength of their engineers: how capable they are, how many mistakes they make, how fast they can work when speed matters.

Why might you want to create shareholder value?

What if you don’t care about any of this? What if you’re interested in the intellectual challenge of designing software, not the business challenge of building hype or profits?

One reason you might care is that shareholder value is part of the software design process. There is no such thing as “good software” in a vacuum. Good software is software that is good at something: i.e. at some particular goal. If you’re not connected to the financial goals of the company, you run the risk of optimizing for software that looks nice or is cool. In my view, that’s not really software design. It’s much more satisfying to design software against real constraints.

Another reason is that creating shareholder value is harder than most technical problems. Many technical problems you encounter in the line of work are easy to solve. But creating shareholder value - making money - is usually hard, because everyone is trying to do it and the space is much more competitive. Another reason it’s hard is that you have more potential to really fail than in most technical problems. In technical problems, you can tell pretty quickly if something’s likely to end up working or not. But when you’re trying to deliver shareholder value, you can try something that seems really promising but goes completely nowhere. That’s challenging! It’s worth getting good at.

A third reason is that it’s your job. You can certainly survive at a tech company by just doing what you’re told and only having opinions about technical matters. But it’s not really what you’re paid to do. You’re paid to produce value (i.e. value for shareholders). I don’t think it’s actually a moral failing to not do your job well. People get to decide what they want to do. But if you’re the kind of person who values doing your job, you have a strong reason to care about shareholder value.

A final reason - perhaps the most important - is that you may end up being happier at work. Many engineers are unhappy because their values are misaligned with their company’s values. If there is a way for you to care about what your company cares about, you should do it! Aside from having a better relationship with managers and executives, it’ll just feel more real.

One common theory of burnout is “work unrecognized”: engineers burn out not because they work too hard, but because their work becomes untethered from the feedback they’re getting from the company. I think one cause of this is a values mismatch between engineers and their employers - that can cause engineers to end up grinding away at a task that their manager doesn’t care about at all.

Final thoughts

I know it sounds like a joke or parody to say “I’m passionate about delivering shareholder value” - like saying “my greatest weakness is I work too hard”. But it really is true. I worry that people who are new to the industry are picking up a bit too much unwarranted cynicism, and that it’s not going to serve them well long-term.

I think a lot of engineers are working in situations where there doesn’t seem to be any path to affecting shareholder value one way or another. Either their opinions aren’t taken seriously, or their product is stagnant, or they’re just too snowed under with bullshit. The last thing I want to do is to chide those engineers - that’s a really tricky situation. But lots of us work in more functional environments, where we have a real opportunity to shape the financial situation of the company, for good or ill.

If you do have that opportunity, you’ll probably be a lot more satisfied at work if you take it.

edit: One interesting note - I run most of my blog posts through GPT-o3 before publishing to catch typos and make high-level structural suggestions (I never use any actual generated text). While o3 is much less sycophantic than 4o, it still likes to start its feedback with a paragraph of what it likes about the post. This was the first post I’ve tried where it didn’t do that. It’s not a model update: it gives positive feedback about other drafts I have in the pipeline. For some reason, GPT-o3 really didn’t like this post!

---

### The
 Coder ‘Village' at the Heart of China's A.I. Frenzy (9 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FQIhUWA/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/_ui7lJ5itKIlsokMlVz55a1GEszWkU12gNzGXI0ciGo=412
**TLDR Summary:** Liangzhu, a suburb in the southern Chinese city of Hangzhou, is a hot spot for entrepreneurs and tech talent. Lured by the low rents and proximity to tech companies like Alibaba and DeepSeek, people flock to the city to explore their own possibilities. The provincial and local governments started offering subsidies and tax breaks to new companies in the region a decade ago, which helped to incubate hundreds of startups. The region has already birthed tech powerhouses like Alibaba, DeepSeek, NetEase, and Hikvision.
**Full Article Content:**
[Scraping failed for this URL. Error: Article `download()` failed with 403 Client Error: Forbidden for url: https://www.nytimes.com/2025/07/06/technology/china-artificial-intelligence-hangzhou.html?unlocked_article_code=1.Uk8.E3py.45aVqyLh2cez&smid=url-share&utm_source=tldrnewsletter on URL https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FQIhUWA/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/_ui7lJ5itKIlsokMlVz55a1GEszWkU12gNzGXI0ciGo=412]

---

### The
 Coder ‘Village' at the Heart of China's A.I. Frenzy (9 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FQIhUWA/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/_ui7lJ5itKIlsokMlVz55a1GEszWkU12gNzGXI0ciGo=412
**TLDR Summary:** Liangzhu, a suburb in the southern Chinese city of Hangzhou, is a hot spot for entrepreneurs and tech talent. Lured by the low rents and proximity to tech companies like Alibaba and DeepSeek, people flock to the city to explore their own possibilities. The provincial and local governments started offering subsidies and tax breaks to new companies in the region a decade ago, which helped to incubate hundreds of startups. The region has already birthed tech powerhouses like Alibaba, DeepSeek, NetEase, and Hikvision.
**Full Article Content:**
[Scraping failed for this URL. Error: Article `download()` failed with 403 Client Error: Forbidden for url: https://www.nytimes.com/2025/07/06/technology/china-artificial-intelligence-hangzhou.html?unlocked_article_code=1.Uk8.E3py.45aVqyLh2cez&smid=url-share&utm_source=tldrnewsletter on URL https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FQIhUWA/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/_ui7lJ5itKIlsokMlVz55a1GEszWkU12gNzGXI0ciGo=412]

---

### The
 Companies Betting They Can Profit From Google Search's Demise (6 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FaWW90Y/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/nWC7HgKFAkI9UWX6MDyqWqBeW42LQber8Q29pOty-Gw=412
**TLDR Summary:** At least a dozen new startups are betting on the rapid demise of Google search and pouring millions of dollars into AI tools. These companies are helping businesses understand how AI chatbots gather information and how to steer them towards brands so that they appear in AI searches. The customer interest is a sign of how AI is transforming search and how companies are trying to get ahead of the changes.
**Full Article Content:**
[Scraping failed for this URL. Error: Article `download()` failed with 401 Client Error: HTTP Forbidden for url: https://www.wsj.com/tech/ai/ai-optimization-startups-google-search-ee4c561a?st=TJpeP3&reflink=desktopwebshare_permalink&utm_source=tldrnewsletter on URL https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FaWW90Y/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/nWC7HgKFAkI9UWX6MDyqWqBeW42LQber8Q29pOty-Gw=412]

---

## Quick Links

### Craving
 more AI in your inbox? (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Ftldr.tech%2Fai%2F%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=quicklinks07072025/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/dG7so9Os6kNLqzKF1c5pre7iuyvLPq2HD2azysV0CK0=412
**TLDR Summary:** TLDR AI is your daily fix of LLMs, GenAI, and deep learning goodness. Same TLDR format. Still free. Subscribe now.
**Full Article Content:**
🧠

The most important AI, ML, and data science news in a free daily email.

Sign Up

Join 500,000 readers for one daily email

---

### Craving
 more AI in your inbox? (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Ftldr.tech%2Fai%2F%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=quicklinks07072025/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/dG7so9Os6kNLqzKF1c5pre7iuyvLPq2HD2azysV0CK0=412
**TLDR Summary:** TLDR AI is your daily fix of LLMs, GenAI, and deep learning goodness. Same TLDR format. Still free. Subscribe now.
**Full Article Content:**
🧠

The most important AI, ML, and data science news in a free daily email.

Sign Up

Join 500,000 readers for one daily email

---

### opencode
 (GitHub Repo)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fgithub.com%2Fsst%2Fopencode%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/lAog8BMgqUUW4I21II3NNDbEoTtC7wTZP6kIOOnuOD0=412
**TLDR Summary:** opencode is an AI coding agent built for the terminal.
**Full Article Content:**
AI coding agent, built for the terminal.

Installation

# YOLO curl -fsSL https://opencode.ai/install | bash # Package managers npm i -g opencode-ai@latest # or bun/pnpm/yarn brew install sst/tap/opencode # macOS paru -S opencode-bin # Arch Linux

Note: Remove versions older than 0.1.x before installing

Documentation

For more info on how to configure opencode head over to our docs.

Contributing

For any new features we'd appreciate it if you could open an issue first to discuss what you'd like to implement. We're pretty responsive there and it'll save you from working on something that we don't end up using. No need to do this for simpler fixes.

Note: Please talk to us via github issues before spending time working on a new feature

To run opencode locally you need.

Bun

Golang 1.24.x

And run.

$ bun install $ bun run packages/opencode/src/index.ts

Development Notes

API Client: After making changes to the TypeScript API endpoints in packages/opencode/src/server/server.ts , you will need the opencode team to generate a new stainless sdk for the clients.

FAQ

How is this different than Claude Code?

It's very similar to Claude Code in terms of capability. Here are the key differences:

100% open source

Not coupled to any provider. Although Anthropic is recommended, opencode can be used with OpenAI, Google or even local models. As models evolve the gaps between them will close and pricing will drop so being provider agnostic is important.

A focus on TUI. opencode is built by neovim users and the creators of terminal.shop; we are going to push the limits of what's possible in the terminal.

A client/server architecture. This for example can allow opencode to run on your computer, while you can drive it remotely from a mobile app. Meaning that the TUI frontend is just one of the possible clients.

What's the other repo?

The other confusingly named repo has no relation to this one. You can read the story behind it here.

Join our community Discord | YouTube | X.com

---

### You're
 all CTO now (6 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fjamie.ideasasylum.com%2F2025%2F07%2F01%2Fyou%2527re-all-cto-now%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/n36xA1HtaLTAkPFUIDCGw2aBXqJ6e5otX1kZIRpqepg=412
**TLDR Summary:** Developers using AI are transitioning from writing code to managing agents and projects.
**Full Article Content:**
Years ago I moved from being one of the developers of Podia to being the CTO. I went from spending ~100% of my time writing code to maybe 70% as more time was taken up managing people and projects. Over the years, that percentage has continued to drop and drop. and now I’m doing very little consistent coding—I ship small changes, occasional bug fixes, upgrades etc but I’m no longer on the critical feature path.

This, is many ways, really suited me. I was never particularly interested in the code itself, and I don’t miss trying to solve some daft dependency problem that didn’t advance the feature. Instead, I was always more interested in the product and the systems and being CTO let’s me operate that that level without getting too bogged down into why this particular method call is not behaving as expected. And managing people let’s me scale my impact far beyond the features I could have shipped myself—assuming I can convince them to do what I want, how I want it done.

But here’s the thing: all that comes with a significant reduction in dopamine satisfaction. I wrote about the the manager’s unbearable lack of endorphins before and I think that’s something which many more developers are going to encounter in the age of AI.

You’re a manager now

Everyone is a manager of AI-coding agents now which brings some benefits and some downsides. Yes, you can get it to automate the drudgery and have it iterate until postgres 17.5 finally builds on your machine (last night’s problem). You can have it build out a feature according to the high-level plan you had, and implement the architecture which only exist in your imagination. You’re operating at a higher level now!

You can write more code faster than before or run these agents in parallel for the real juggling-plates management experience. Look at you scaling your output!

But how are you going to feel about this? Because you are not an AI agent and your feelings, your motivation, and your job satisfaction are going to matter over the long term.

Initially, you are going to feel amazing. How can you accomplish so much, with so little effort?! This is like swimming downstream, running with a tailwind, or when that caffeine finally kicks in. You’re flying! Who knew it could be so easy?

But then what?

Let that sink in for a while. Read it again, and again. Internalise it.

What are the proudest moments of your life? What are the things you’ve accomplished in your professional career that you’re most proud of? Did they come easy? Were they handed to you tied up with a bow, or fell into your lap through luck? I bet not. I bet you had to fight for it, you worked hard, got sooooo frustrated, and pushed and pushed through that problem. I bet you were exhausted when you finally cracked it.

Those accomplishments probably didn’t just involve explaining a concept or asking a question that changed the result of a project from a failure to a success. It wasn’t just making a decision that put the right people on the right project, or arguing for a cut in the scope, or highlighting a critical flaw in the system so someone else could fix it. It wasn’t just a well-crafted prompt to a colleague (AI, or human).

Because that’s what managers do and now, as a manager of AI agents, that’s what you will do.

Show me the dopamine!

How are you going to feel that dopamine rush now? How are you going to feel that same sense of job satisfaction?

There is a popular argument that a software developer’s job is not write software but to solve a user’s problem. Bullshit. By the time it gets to a developer’s desk, the solution should always be to write (or fix, or reuse) some software—otherwise why give it to an engineer? The product manager’s job is to solve the user’s problem. The business’s job is to solve the user’s problem. And yes, at a high-level the purpose of your job is to solve a user’s problem but your day-to-day function is to write and fix software.

Being a product manager or a business owner is probably not the reason you got into the tech industry in the first place.

Being able to satisfy a user need by spending a few minutes writing a prompt probably isn’t going to bring you the same satisfaction as the endless conveyor belt of interesting logic problems you are used to solving. So what’s going to keep you in this industry? Why will you still be here in 5 years?

I don’t know and I can’t answer that for you but maybe it’s something to consider. I think it might change the types of people that the industry attracts and retains. For one thing, it seems likely that those with ADHD are going to become less satisfied in an environment where it’s hard to achieve “flow” and doesn’t reward that sort of hyper-focus.

I don’t think AI-agents are going to work as perfectly as I’ve assumed above. There will still be room for some intense problem-solving at the code level by experienced humans. Emergency developers will be standing by, ready to dive in and rescue a project when the AI’s and less-technical people fail—the parajumpers of software development. Though you might not build the feature, you might now be dropped into the unfamiliar terrain of AI-generated code and asked to fix it: a much harder and more stressful task than working to fix something you have built up a mental model of and have some familiarity with.

Out with the old, in with the new

As you start to use AI agents more frequently, you’ll get better at explaining the tasks to them. You’ll get better at breaking down the work into suitable chunks, emphasising certain attributes you want over others, and understanding their limitations. You might get better at training them and giving them the resources they need. Hint: just like managing people.

And with those new skills, your old skills will start to atrophy. I am not as familiar with Rails code as I used to be. I have not kept up with all the changes in Ruby syntax even. I understand only enough of Turbo to be able to suggest it’s appropriate or inappropriate uses but I’d need to fish out some tutorials and documentation to write it myself.

The skills you use are the skills you maintain. Sure, you’ll have the muscle-memory—once a developer always a developer, just like former athletes can still have good form—but you won’t be as proficient as you were when you were writing everything yourself.

That alone is what’s going to make that “parajumper” role particularly hard. It’s one of the things that makes even being a CTO hard because, almost by definition, all the problems that get to me are hard problems, with code I’m unfamiliar with, and skills I’m not keeping sharp.

Welcome to your new role. I hope you’ll be happy here 😅

---

### Ask
 HN: Worth leaving position over push to adopt vibe coding? (Hacker News Thread)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fnews.ycombinator.com%2Fitem%3Fid=44468375%26utm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/k8XVP-eB_KKycSFCKYPZo1oZDhaBuXAe4VDIC8kgg0o=412
**TLDR Summary:** Developers should at least stay to learn how the technology works, whether they agree with it or not - it will either work better than expected, or they will be able to inform prospective employers that they have experience working with it later.
**Full Article Content:**
My company is increasingly pushing prompt engineering as the single way we "should" be coding. The CEO & CTO are both obsessed with it and promote things like "delete entire unit test file & have claude generate a new one" rather than manually address test failures.

I'm a 'senior engineer' with ~5 years of industry experience and am considering moving on from this company because I don't want

1. Be pushed into a workflow that will cause my technical growth to stall or degrade 2. Be overseeing a bunch of AI-generated spaghetti 2-3 years from now

Feel free to address my specific situation but I'm interested in more general opinions.

---

### Git
 experts should try Jujutsu (4 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fpksunkara.com%2Fthoughts%2Fgit-experts-should-try-jujutsu%2F%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/V0OZZy5OhPNRBYcDVRL3FWOtaw_Enj4-gOICUJNulDg=412
**TLDR Summary:** Jujutsu is a force multiplier for those who understand how version control works - it automates the tedious mechanics of history editing, letting developers focus on the what instead of the how.
**Full Article Content:**
Jul 3, 2025 · 4 min git jujutsu 4 min

Git experts should try Jujutsu

I've been a Git command-line power user for a long time. For me, Git isn't just a tool for pulling and pushing code. It's a finely-tuned instrument for crafting history. I'm the person who will meticulously clean up my commit history before submitting a pull request. My toolkit is full of commands like git rebase -i , git add -i , git commit --fixup , and git reset --hard . I can reorder, squash, and reword commits in my sleep. If something goes wrong, I know how to use the reflog to get myself out of any mess. I don't just use Git, I speak it fluently. I even have many many custom git aliases to make my workflow faster.

So when I first heard about Jujutsu, I was skeptical. The main selling point I saw was that it was much simpler than Git. It felt like a tool designed to shield beginners from Git's sharp edges, not something for a seasoned expert like me.

I gave the tutorial a quick look, but it didn't showcase any real benefits for my workflow. It confirmed my bias: this was for people who were afraid of Git's power, not for those who had already mastered it.

But the idea lingered. On a whim, I decided to install it on my work machine and used it on a complex project. That's when everything changed. I discovered that Jujutsu wasn't about avoiding history manipulation. It was about making it faster, easier, and more intuitive than I ever thought possible. It took the concepts I had mastered in Git and gave them a superior interface.

Comparison

Here are a few examples of how Jujutsu streamlined tasks that were already second nature to me in Git.

Editing an old commit

This is a classic scenario. You've spotted a typo or a small bug in a commit from five changes ago.

In Git: You start an interactive rebase, find the commit, mark it for editing, make your changes, amend the commit, and finally, continue the rebase.

# Find the commit in the log git log --oneline # Start the interactive rebase git rebase -i HEAD ~ 5 # And mark the commit you want to edit # Make your code changes vim lib/edit.ts # Amend the commit git add . git commit --amend # Finish the rebase git rebase --continue

In Jujutsu: You simply tell it which change you want to edit. It checks it out, you make your changes, and you're done. Jujutsu handles the rebase automatically in the background.

# Find the change id jj log # Edit the change directly jj edit < change-id > # Make your code changes... vim lib/edit.ts

There's no interactive editor, no --continue step. It's direct and to the point.

Splitting a commit

You've just realized you bundled two unrelated changes into a single commit.

In Git: This requires another interactive rebase, mark it for editing, reset it to unstage the changes, and then carefully using git add -p to rebuild the commits piece by piece.

# Start the interactive rebase git rebase -i < commit > ^ # And mark the commit you want to edit # Reset the commit but keep the changes in the working directory git reset HEAD^ # Interactively add the first set of changes git add -p git commit -m "First part" # Add the remaining changes git add . git commit -m "Second part" # Finish the rebase git rebase --continue

In Jujutsu: A single command initiates an interactive diff editor, allowing you to decide what to keep in the original commit and what to move to a new one.

jj split < change-id > # This creates two new commits. You can then use `jj describe` to edit the commit messages.

This is far more intuitive and significantly faster.

Creating a quick PR

In Git: The standard procedure is to create a branch, commit your changes, push that branch, and then open a pull request on your hosting platform.

# Create a new branch git checkout -b my-feature-branch # Make your changes vim lib/edit.ts # Stage and commit your changes git add . git commit -m "My feature" # Push the branch to the remote git push origin my-feature-branch # Create a pull request gh pr create

In Jujutsu: You can push your current change directly to the remote, which Jujutsu will place on a new branch for you. No need to manage local branches.

# Start a new change jj new -m "My feature" # Make your changes vim lib/edit.ts # Push the change to the remote jj git push --change @ # Create a pull request gh pr create --head < created-bookmark-name >

Conclusion

After years of honing my Git skills, I thought I had reached peak efficiency. Jujutsu proved me wrong. It's not a replacement for understanding how version control works. It's a force multiplier for those who already do. Jujutsu automates the tedious mechanics of history editing, letting you focus on the what instead of the how.

If you're a Git expert who prides yourself on your ability to manipulate history, I urge you to give Jujutsu a serious try on a real project. You might just find that your favorite power tools have been upgraded.

And yes, I've already started a new list of jj aliases to make my workflow even faster.

---

### Yet
 another ZIP trick (7 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fhackarcana.com%2Farticle%2Fyet-another-zip-trick%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/s8m3H-wOdQ-UGtHRdBR0KLwiIR50o7cbrRNqRt_zb8o=412
**TLDR Summary:** A schizophrenic zip file can be interpreted in different ways by different parsers, resulting in different content.
**Full Article Content:**
To delete account insert your password. After that, a e-mail with deletion confirm link will be send. Click on it to confirm account deletion.

You already have a account?

and to the

I have read and agree to the

Do you consent to our site using cookies in accordance to our Privacy Policy? You can consent either to all cookies, or accept only selected types.

Reject optional Cache only Allow all cookies

Advanced cookie settings

---

### Learn
 to love the Moat of Low Status (10 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fusefulfictions.substack.com%2Fp%2Flearn-to-love-the-moat-of-low-status%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/6OFMMkSgJOx3UErvN17ZcERO3HlRCBeZx0Hna0mcqhM=412
**TLDR Summary:** The fear of being temporarily low in social status stops people from living richer lives.
**Full Article Content:**
[Scraping failed for this URL. Error: Article `download()` failed with 403 Client Error: Forbidden for url: https://usefulfictions.substack.com/p/learn-to-love-the-moat-of-low-status?utm_source=tldrnewsletter on URL https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fusefulfictions.substack.com%2Fp%2Flearn-to-love-the-moat-of-low-status%3Futm_source=tldrnewsletter/1/01000197e47b1aac-96c038a0-ed8f-49e4-86ed-d2888728b8af-000000/6OFMMkSgJOx3UErvN17ZcERO3HlRCBeZx0Hna0mcqhM=412]

---

