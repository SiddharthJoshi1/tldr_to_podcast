# TLDR Newsletter Summary: 2025-07-09

## TLDR2025-07-09

### WorkOS
 AuthKit + Radar: Authentication with Abuse Prevention (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fworkos.com%2Fblog%2Fhow-workos-radar-really-works%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=q22025/2/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/JD4Ybq095pbvTaIwGudbit6oA1aIUdYkY-MheTdsqk0=413
**TLDR Summary:** Authentication isn't just login. It's building secure flows, managing sessions, handling tokens, supporting SSO, and protecting user data. AuthKit gives you a fully hosted, customizable UI for sign-up, MFA, password resets, and seamless SSO. Production-ready from day one. But authentication alone doesn't stop abuse. WorkOS Radar adds real-time threat prevention: blocking bots, stopping brute force attempts, and catching free trial abuse. Built-in defenses activate instantly without custom scripts or logic. Protect your app today with AuthKit and WorkOS Radar.
**Full Article Content:**
How does WorkOS Radar really work? How do you install and set it up and what does it reveal?

What happens in the milliseconds after someone attempts to log into your application? For most systems, it's a simple check of username and password.

But what if that login attempt comes from a bot farm in a distant country? What if it's the 500th attempt in the last hour? What if it's a valid credential being tested across thousands of accounts?

These are the threats that modern applications face, and they're why WorkOS built Radar. This real-time protection system makes split-second decisions about every authentication attempt that hits your application.

While the technical documentation covers implementation details and the launch blog introduces features, this article takes you behind the scenes to understand what it's actually like to use Radar day-to-day - from seeing your first suspicious login attempt to fine-tuning your security rules based on real-world patterns.

Installation and setup

Radar builds on top of AuthKit, WorkOS's authentication SDK. While Radar isn't enabled by default for all AuthKit instances, it can be activated by contacting the WorkOS team. Once enabled, Radar immediately begins collecting signals about user behavior during authentication attempts.

Real-time monitoring and analysis

Radar's dashboard provides a comprehensive view of your application's authentication activity:

A real-time chart showing counts of suspicious events and automated actions

Time-range toggles for 24 hours, 7 days, and 30 days of historical data

Detailed cards showing detection activity by different identifiers (devices, locations, users)

A complete event list that can be filtered by detection type, action taken, or specific users

Each event captures rich metadata, including:

Device fingerprints

Location data

User-agent information

IP addresses

Authentication attempt timing

What can WorkOS Radar detect?

1. Bots...of all kinds

Radar's bot detection goes beyond simple pattern matching. It can differentiate between:

AI agents

Search engine crawlers

Automation scripts

Testing tools

This granular detection allows you to block or allow different types of automated access selectively.

2. Brute force and credential stuffing attacks

Radar uses device fingerprinting to isolate attack traffic from legitimate users, ensuring your application stays available even during an attack. The system tracks:

Authentication frequency per client

Pattern matching across multiple accounts

Password variation patterns

Geographic distribution of attempts

3.“ Impossible travel”

The system tracks login locations and calculates whether sequential authentication attempts could be physically possible, flagging suspiciously rapid changes in location.

4. Stale account compromise

For enhanced security, Radar monitors dormant accounts (no successful logins in 30+ days) and can notify administrators when they become active - a common indicator of account takeover.

5. Unrecognized devices

Using sophisticated device fingerprinting, Radar maintains a history of known devices per user and can trigger additional verification for new devices.

6. Custom restrictions

Organizations can implement specific allow/deny rules based on:

IP ranges

User agents

Device types

Individual users

Installing Radar through AuthKit

Before Radar can protect your application, you must install AuthKit - WorkOS's authentication SDK. AuthKit enables Radar to monitor every authentication attempt in real time.

Here's how to set it up with Next.js (a similar process for other frameworks):

First, install the AuthKit SDK:

npm install @workos-inc/authkit-nextjs

Configure your environment variables:

WORKOS_API_KEY= 'your_api_key' WORKOS_CLIENT_ID= 'your_client_id' WORKOS_COOKIE_PASSWORD= "your_secure_password" NEXT_PUBLIC_WORKOS_REDIRECT_URI= "http://localhost:3000/callback"

Add the AuthKit provider to your app layout:

import { AuthKitProvider } from '@workos-inc/authkit-nextjs' ; export default function RootLayout ( { children } ) { return ( < html lang = "en" > < body > < AuthKitProvider > {children} </ AuthKitProvider > </ body > </ html > ); }

Once AuthKit is installed, Radar begins delivering events and data to the Radar panel in the WorkOS dashboard.

‍How Radar makes decisions

What sets Radar apart is its sophisticated decision-making process. Rather than using simple yes/no rules, Radar evaluates each authentication attempt through a multi-stage pipeline. Here's how an authentication attempt flows through the system:

Real-world protection

Let's say an attacker starts testing stolen credentials against your application. Within seconds, Radar will:

Detect the high-frequency login attempts

Identify patterns indicating automated tools

Notice if the attempts are coming from unusual locations

Calculate a risk score based on all these factors

Take appropriate action based on your security settings

Try WorkOS Radar today

WorkOS Radar represents a new approach to authentication security that combines sophisticated threat detection with practical, real-world usability.

As it evolves and integrates with features like Actions, it will continue to expand its capabilities while maintaining its streamlined implementation.

---

## Big Tech & Startups

### Samsung's
 event spoiled by massive last-minute leak (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.theverge.com%2Fnews%2F700584%2Fsamsung-galaxy-unpacked-2025-leak%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/vXb-P_kmdo75dWlFBfouYYfQW22JRMaWlMRVpGYXKVA=413
**TLDR Summary:** A reliable leaker has shared a whole bunch of marketing materials for Samsung's Galaxy Unpacked event (which kicks off today at 10 AM ET) containing details and images of the company's upcoming devices. The Z Fold 7 will measure 4.2 millimeters when unfolded and the Z Flip 7 will measure 6.5 millimeters when unfolded. None of the marketing materials highlight an S Pen on the Z Fold 7, suggesting that the device may not support an S Pen at all. The leaked material also contains images and specs for new Galaxy Watches, which have upgraded storage, displays, and batteries.
**Full Article Content:**
is a news writer who covers the streaming wars, consumer tech, crypto, social media, and much more. Previously, she was a writer and editor at MUO.

Samsung’s Galaxy Unpacked event is just one day away, but a new leak may have just revealed even more details and images of the company’s upcoming devices. In a series of posts on Bluesky, reliable leaker Roland Quandt shared a whole bunch of marketing materials that suggest Samsung is dropping support for the S Pen on its slimmed-down Z Fold 7.

This adds to the leak Quandt shared on Monday, which appeared to show the specs for the Galaxy Z Fold 7, Z Flip 7, and Z Flip 7 FE. The marketing materials highlight the Z Fold 7’s slim profile; it measures 4.2mm when unfolded and weighs 215 grams, or “less than a large bar of chocolate.” They also say the Z Flip 7 will measure 6.5mm when unfolded, which the materials claim is “about the width of a pencil.”

As pointed out by Quandt, none of the marketing materials highlight an S Pen on the Z Fold 7. With previous generations, you could purchase the S Pen Fold Edition separately and store it in a special case (not inside the phone itself, like you can with the Galaxy S25 Ultra). Based on the leak, the Z Fold 7 may not support an S Pen at all.

Additionally, Quandt posted the purported images and specs for the Galaxy Watch 8, Galaxy Watch 8 Classic, and Galaxy Watch Ultra. The new Watch Ultra appears to come with an upgraded 64GB of storage, up from 32GB on its predecessor. It also has many of the same features as the previous Watch Ultra, including a 1.5-inch AMOLED display, up to 100 hours of battery life in power-saving mode, a safety siren, and dual-frequency GPS.

The Galaxy Watch 8 and Watch 8 Classic appear to adopt the same round display shape and squircle body design as the Watch Ultra. The materials also show that the Watch 8 may offer an upgraded 3,000 nits of brightness and have an 11 percent thinner profile than its predecessor.

Meanwhile, the Watch 8 Classic could come with a much higher 64GB of storage and a larger 445mAh battery when compared to the 16GB of storage and up to 425mAh battery on the Watch 6 Classic. It also looks like the Galaxy Watch 8 Classic will come in just one size, 1.3 inches, along with a silver rotating bezel and a watch face that’s available in black or white.

---

### Samsung's
 event spoiled by massive last-minute leak (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.theverge.com%2Fnews%2F700584%2Fsamsung-galaxy-unpacked-2025-leak%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/vXb-P_kmdo75dWlFBfouYYfQW22JRMaWlMRVpGYXKVA=413
**TLDR Summary:** A reliable leaker has shared a whole bunch of marketing materials for Samsung's Galaxy Unpacked event (which kicks off today at 10 AM ET) containing details and images of the company's upcoming devices. The Z Fold 7 will measure 4.2 millimeters when unfolded and the Z Flip 7 will measure 6.5 millimeters when unfolded. None of the marketing materials highlight an S Pen on the Z Fold 7, suggesting that the device may not support an S Pen at all. The leaked material also contains images and specs for new Galaxy Watches, which have upgraded storage, displays, and batteries.
**Full Article Content:**
is a news writer who covers the streaming wars, consumer tech, crypto, social media, and much more. Previously, she was a writer and editor at MUO.

Samsung’s Galaxy Unpacked event is just one day away, but a new leak may have just revealed even more details and images of the company’s upcoming devices. In a series of posts on Bluesky, reliable leaker Roland Quandt shared a whole bunch of marketing materials that suggest Samsung is dropping support for the S Pen on its slimmed-down Z Fold 7.

This adds to the leak Quandt shared on Monday, which appeared to show the specs for the Galaxy Z Fold 7, Z Flip 7, and Z Flip 7 FE. The marketing materials highlight the Z Fold 7’s slim profile; it measures 4.2mm when unfolded and weighs 215 grams, or “less than a large bar of chocolate.” They also say the Z Flip 7 will measure 6.5mm when unfolded, which the materials claim is “about the width of a pencil.”

As pointed out by Quandt, none of the marketing materials highlight an S Pen on the Z Fold 7. With previous generations, you could purchase the S Pen Fold Edition separately and store it in a special case (not inside the phone itself, like you can with the Galaxy S25 Ultra). Based on the leak, the Z Fold 7 may not support an S Pen at all.

Additionally, Quandt posted the purported images and specs for the Galaxy Watch 8, Galaxy Watch 8 Classic, and Galaxy Watch Ultra. The new Watch Ultra appears to come with an upgraded 64GB of storage, up from 32GB on its predecessor. It also has many of the same features as the previous Watch Ultra, including a 1.5-inch AMOLED display, up to 100 hours of battery life in power-saving mode, a safety siren, and dual-frequency GPS.

The Galaxy Watch 8 and Watch 8 Classic appear to adopt the same round display shape and squircle body design as the Watch Ultra. The materials also show that the Watch 8 may offer an upgraded 3,000 nits of brightness and have an 11 percent thinner profile than its predecessor.

Meanwhile, the Watch 8 Classic could come with a much higher 64GB of storage and a larger 445mAh battery when compared to the 16GB of storage and up to 425mAh battery on the Watch 6 Classic. It also looks like the Galaxy Watch 8 Classic will come in just one size, 1.3 inches, along with a silver rotating bezel and a watch face that’s available in black or white.

---

### Meta Invests
 $3.5 Billion in World's Largest Eye-Wear Maker in AI Glasses Push (3 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FvE380D/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/aBjqOorc15Rbq7OhxPOcyWThK2T2ABnExz1m0nYnsVo=413
**TLDR Summary:** Meta has bought a minority stake in EssilorLuxottica. It acquired just under 3% of the Ray-Ban maker, a stake worth around $3.5 billion at the current market price. Meta is considering further investment that could build the stake to around 5% over time, though those plans could still change. The deal provides EssilorLuxottica with a deeper presence in the tech world.
**Full Article Content:**
[Scraping failed for this URL. Error: Article `download()` failed with 403 Client Error: Forbidden for url: https://www.bloomberg.com/news/articles/2025-07-08/meta-invests-3-5-billion-in-essilorluxottica-in-ai-glasses-push?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc1MjAyNjk4NCwiZXhwIjoxNzUyNjMxNzg0LCJhcnRpY2xlSWQiOiJTWVZMT1lEV0xVNjgwMCIsImJjb25uZWN0SWQiOiJFQTExNDNDNTM4NEE0RUY5QTg5RjJEN0IxMTg2MzcwOSJ9.-6dyoMcfNaGxmPwnyQD-yGVtwAcbq04UfQAlr5Qxmg8&utm_source=tldrnewsletter on URL https://tracking.tldrnewsletter.com/CL0/https:%2F%2Flinks.tldrnewsletter.com%2FvE380D/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/aBjqOorc15Rbq7OhxPOcyWThK2T2ABnExz1m0nYnsVo=413]

---

## Science & Futuristic Technology

### China
 jumps ahead in the race to achieve a new kind of reuse in space (9 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Farstechnica.com%2Fspace%2F2025%2F07%2Fchina-jumps-ahead-in-the-race-to-achieve-a-new-kind-of-reuse-in-space%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/nm7SrYqErkwYLsDRCX0h68kWvrC6ysJ_Wlg4MNHLEzk=413
**TLDR Summary:** China likely completed the first high-altitude attempt at orbital refueling sometime last week. Two of its satellites appeared to dock together in geosynchronous orbit, coming together and then becoming indistinguishable as a single object. Besides refueling satellites in space, the technology could also be used to approach, capture, and disable other satellites. The US Space Force plans to perform the first refueling of a US military asset in orbit as soon as next year.
**Full Article Content:**
Two Chinese satellites have rendezvoused with one another more than 20,000 miles above the Earth in what analysts believe is the first high-altitude attempt at orbital refueling.

China's Shijian-21 and Shijian-25 satellites, known as SJ-21 and SJ-25 for short, likely docked together in geosynchronous orbit sometime last week. This is the conclusion of multiple civilian satellite trackers using open source imagery showing the two satellites coming together, then becoming indistinguishable as a single object.

Chinese officials have released no recent public information on what the two satellites are up to, but they've said a bit about their missions in prior statements.

SJ-25, which launched in January, is designed "for the verification of satellite fuel replenishment and life extension service technologies," according to the Shanghai Academy of Spaceflight Technology, the Chinese state-owned contractor that developed the satellite. SJ-21 launched in 2021 and docked with a defunct Chinese Beidou navigation satellite in geosynchronous orbit, then towed it to a higher altitude for disposal before returning to the geosynchronous belt. Chinese officials described this demonstration as a test of "space debris mitigation" techniques.

More than meets the eye

These kinds of technologies are dual-use, meaning they have civilian and military applications. For example, a docking in geosynchronous orbit could foretell an emerging capability for China to approach, capture, and disable another country's satellite. At the same time, the US Space Force is interested in orbital refueling as it seeks out ways to extend the lives of military satellites, which are often limited by finite fuel supplies.

The Space Force sometimes calls this concept dynamic space operations. While some military leaders remain skeptical about the payoff of in-space refueling, the Space Force has an agreement with Astroscale to perform the first refueling of a US military asset in orbit as soon as next year.

China appears to be poised to beat the US Space Force to the punch. The apparent docking of the two satellites last week suggests SJ-21 is the target for SJ-25's refueling demonstration, and US officials are watching. Two of the Space Force's inspector satellites, known by the acronym GSSAP, positioned themselves near SJ-21 and SJ-25 to get a closer look.

---

### China
 jumps ahead in the race to achieve a new kind of reuse in space (9 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Farstechnica.com%2Fspace%2F2025%2F07%2Fchina-jumps-ahead-in-the-race-to-achieve-a-new-kind-of-reuse-in-space%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/nm7SrYqErkwYLsDRCX0h68kWvrC6ysJ_Wlg4MNHLEzk=413
**TLDR Summary:** China likely completed the first high-altitude attempt at orbital refueling sometime last week. Two of its satellites appeared to dock together in geosynchronous orbit, coming together and then becoming indistinguishable as a single object. Besides refueling satellites in space, the technology could also be used to approach, capture, and disable other satellites. The US Space Force plans to perform the first refueling of a US military asset in orbit as soon as next year.
**Full Article Content:**
Two Chinese satellites have rendezvoused with one another more than 20,000 miles above the Earth in what analysts believe is the first high-altitude attempt at orbital refueling.

China's Shijian-21 and Shijian-25 satellites, known as SJ-21 and SJ-25 for short, likely docked together in geosynchronous orbit sometime last week. This is the conclusion of multiple civilian satellite trackers using open source imagery showing the two satellites coming together, then becoming indistinguishable as a single object.

Chinese officials have released no recent public information on what the two satellites are up to, but they've said a bit about their missions in prior statements.

SJ-25, which launched in January, is designed "for the verification of satellite fuel replenishment and life extension service technologies," according to the Shanghai Academy of Spaceflight Technology, the Chinese state-owned contractor that developed the satellite. SJ-21 launched in 2021 and docked with a defunct Chinese Beidou navigation satellite in geosynchronous orbit, then towed it to a higher altitude for disposal before returning to the geosynchronous belt. Chinese officials described this demonstration as a test of "space debris mitigation" techniques.

More than meets the eye

These kinds of technologies are dual-use, meaning they have civilian and military applications. For example, a docking in geosynchronous orbit could foretell an emerging capability for China to approach, capture, and disable another country's satellite. At the same time, the US Space Force is interested in orbital refueling as it seeks out ways to extend the lives of military satellites, which are often limited by finite fuel supplies.

The Space Force sometimes calls this concept dynamic space operations. While some military leaders remain skeptical about the payoff of in-space refueling, the Space Force has an agreement with Astroscale to perform the first refueling of a US military asset in orbit as soon as next year.

China appears to be poised to beat the US Space Force to the punch. The apparent docking of the two satellites last week suggests SJ-21 is the target for SJ-25's refueling demonstration, and US officials are watching. Two of the Space Force's inspector satellites, known by the acronym GSSAP, positioned themselves near SJ-21 and SJ-25 to get a closer look.

---

### CRISPR
 breakthrough allows scientists to edit multiple genes simultaneously (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fnewatlas.com%2Fcrispr-cas12a-gene-editing-multiple-eth-zurich%2F61068%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/jSCfKY_wTtVknU0R0NMdLBCFenmM72hI5rZW3cpyltU=413
**TLDR Summary:** Scientists at ETH Zurich have developed a new CRISPR method that can modify dozens of genes simultaneously. It can be used to systematically modify entire gene networks in a single step. The technique uses the lesser-known Cas12a enzyme, which is slightly more precise in its ability to identify targeted genes and can handle shorter RNA molecules compared to the traditional Cas9 enzyme. It enables scientists to explore broad genetic interactions.
**Full Article Content:**
We've seen a number of recent improvements to the CRISPR gene editing method, from enhanced precision to novel techniques to block the process. But despite all these innovations, the technique is generally only able to modify one single gene at a time. An incredible new breakthrough from scientists at ETH Zurich has, for the first time, demonstrated a new CRISPR method that can modify dozens of genes simultaneously, allowing for more large-scale cell reprogramming.

In a recently published paper in the journal Nature Methods, a team of ETH scientists demonstrated their new gene editing process can modify 25 different target sites simultaneously. The scientists say this new technique is not necessarily limited to 25 targets, but theoretically could be increased to hundreds of simultaneous gene modifications.

"Thanks to this new tool, we and other scientists can now achieve what we could only dream of doing in the past," says Randall Platt, from ETH Zurich in Basel. "Our method enables us, for the first time, to systematically modify entire gene networks in a single step."

Instead of using the traditional Cas9 enzyme, utilized in most CRISPR work, this technique utilizes the lesser known Cas12a enzyme. Prior research has already revealed the Cas12a enzyme to be slightly more precise in its ability to identify targeted genes, however, the new research reveals Cas12a can also handle shorter RNA address molecules compared to Cas9.

The general CRISPR-Cas technique homes in on its target in a DNA sequence using a pre-designed RNA sequence, called guide RNA. This RNA molecule functions like an address label. The new technique involved the design of a novel plasmid, or circular DNA molecule, that can hold a number of different RNA address labels. One of the strengths of the Cas12a enzyme is its ability to effectively read shorter RNA address sequences.

"The shorter these addressing sequences are, the more of them we can fit onto a plasmid," explains Platt.

Genes interact with each other in extraordinarily complex ways. So, while single gene editing can be useful when we know a certain condition is caused by just one gene, the reality underlying many disorders is much more complicated. This innovative new technique now allows scientists to explore broad genetic interactions by influencing a number of genes in one single step.

The new research was published in the journal Nature Methods.

Source: ETH Zurich

---

## Programming, Design & Data Science

### 😘
 Kiss bugs goodbye with fully automated end-to-end test coverage (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.qawolf.com%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=ACQ_All_Demo_Conversions__NewsletterAudience_-_Newsletter_KissBugsGoodbye_20250709-None_Experiment-FALSE%26utm_term=headline-KissBugsGoodbyeWithFullyAutomatedEndtoEndTestCoverage%26utm_content=KissBugsGoodbye_ScheduleADemoToLearnMore_None_Headline%253AKissBugsGoodbyeWithFullyAutomatedEndToEndTestCoverage____Newsletter-SecondaryPlacement_20250709_v1_/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/H3SY9FEYAtzn8FEZ596c-qEzkJ8x_oWOgqQISkPVdjc=413
**TLDR Summary:** QA Wolf's AI-native service gets web and mobile apps to 80% automated end-to-end test coverage in just 4 months. They build and maintain your automated test suite, plus provide unlimited parallel test runs. Skeptical? This case study shows how Salesloft saves $750k/year in QA engineering + executes >300 tests in parallel on every PR in minutes. Schedule a demo to learn more
**Full Article Content:**
Zero Flakes

100% reliable test results on every run

Separating bugs and flakes slows down QA cycles, delays new features, and eats up development time. So we do it for you. Starting with our AI, which starts investigating failed tests within seconds and developing a solution for our human QA engineers to review and approve.



Having AI do the work and humans do the thinking, guarantees speed, accuracy, and accountability.

---

### 😘
 Kiss bugs goodbye with fully automated end-to-end test coverage (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.qawolf.com%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=ACQ_All_Demo_Conversions__NewsletterAudience_-_Newsletter_KissBugsGoodbye_20250709-None_Experiment-FALSE%26utm_term=headline-KissBugsGoodbyeWithFullyAutomatedEndtoEndTestCoverage%26utm_content=KissBugsGoodbye_ScheduleADemoToLearnMore_None_Headline%253AKissBugsGoodbyeWithFullyAutomatedEndToEndTestCoverage____Newsletter-SecondaryPlacement_20250709_v1_/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/H3SY9FEYAtzn8FEZ596c-qEzkJ8x_oWOgqQISkPVdjc=413
**TLDR Summary:** QA Wolf's AI-native service gets web and mobile apps to 80% automated end-to-end test coverage in just 4 months. They build and maintain your automated test suite, plus provide unlimited parallel test runs. Skeptical? This case study shows how Salesloft saves $750k/year in QA engineering + executes >300 tests in parallel on every PR in minutes. Schedule a demo to learn more
**Full Article Content:**
Zero Flakes

100% reliable test results on every run

Separating bugs and flakes slows down QA cycles, delays new features, and eats up development time. So we do it for you. Starting with our AI, which starts investigating failed tests within seconds and developing a solution for our human QA engineers to review and approve.



Having AI do the work and humans do the thinking, guarantees speed, accuracy, and accountability.

---

### Introducing
 OpenCLI (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fpatriksvensson.se%2Fposts%2F2025%2F07%2Fintroducing-open-cli%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/6q24F9dmkcaYYtnMzN1ar2lIklpA_k_BhieWLdGp6yA=413
**TLDR Summary:** The OpenCLI specification defines a standard, platform and language-agnostic interface to command-line applications that allows both humans and computers to understand how a tool should be invoked without access to source code or documentation. With the growing interest in MCP (Model Context Protocol) and command-line automation, there's a huge potential in standardizing how command-line applications are described. The specification is still a draft and incomplete. It is maintained under the Specter.Console GitHub organization.
**Full Article Content:**
About three years ago, I was invited to meetings with the System.CommandLine team at Microsoft. They were in the process of finalizing System.CommandLine and wanted input from people in the community, and I was included due to my work on Spectre.Console and Spectre.Console.Cli.

One of the things discussed briefly during those meetings was an open specification to describe the structure of a CLI, something akin to OpenAPI, but for command-line applications. I absolutely LOVED this idea, because I saw how many problems it could solve, not just for documentation generation, but also for creating strongly typed wrappers to interact with CLI tools programmatically.

Three years have passed, and I haven't seen anyone take the initiative to build something like this.

So I figured: it's time I do something myself.

That's why today I want to introduce the OpenCLI initiative which (for now) is maintained under the Spectre.Console GitHub organization. The specification is a draft and still incomplete, but I think it acts as a great starting point.

To paraphrase the specification:

The OpenCLI specification (OCS) defines a standard, platform and language-agnostic interface to CLI applications, which allows both humans and computers to understand how a CLI tool should be invoked without access to source code or documentation.

I genuinely believe that today, especially with the growing interest in MCP (Model Context Protocol) and CLI automation, there's huge potential in standardizing how we describe command-line applications.

If you think this is a good idea or have thoughts, suggestions, or feedback, please don't hesitate to reach out.

I'm interested in collaborating with anyone who is interested in this topic!

https://opencli.org

https://github.com/spectreconsole/open-cli

---

### Gemini
 Nano in Chrome 137: notes for AI Engineers (5 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fgithub.com%2Fswyxio%2Fswyxdotio%2Fissues%2F536%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/PNe6yKaViiPS3F5EKHKllkcUN4uvQ3jeH0ceM0OYZho=413
**TLDR Summary:** Gemini Nano is starting to be shipped unflagged in Chrome and will likely be shipped fully unflagged by the end of the year. There are a few APIs available for commonly used patterns, but the main one engineers will be interested in is the Prompt API, which is the most flexible and open-ended one. This article goes through how to set up and use Gemini Nano. It covers the basic important things and pitfalls to be aware of when using the API.
**Full Article Content:**
slug: gemini-nano

at long last, Gemini Nano is almost here for all Chrome users (i was originally misinformed that it was in Chrome 138 - but i checked my own facts and since Chrome 137+ it is starting to be shipped unflagged in limited situations). I was reminded by this HN post. I expect it to be shipped fully unflagged by end of year.

I don't like the way google write docs, so this blogpost is basically me rewriting their docs in a way that fits my brain.

they have a few apis for commonly used patterns on offer, but reallly the main one you'll care about as an engineer is the Prompt API, the most flexible/open ended one.

setup

Unlike the initial overpromise of window.ai (which spawned copycat shims like xander and chromeai, none actively maintained), the current released implementation is much less "clean". anyway here's the current way to set it up.

make sure you have chrome 137+ go chrome://flags/#prompt-api-for-gemini-nano and turn it on (unfortunately you'll have to reload chrome) then download the model by calling LangaugeModel.create() for the first time - takes a few mins on home wifi. Gemini says "has an approximate download size ranging from 1.5 GB to 2.4 GB." so lets say thats a 4-6B model at a 4-8bit quantization.

const session = await LanguageModel . create ( { monitor ( m ) { m . addEventListener ( "downloadprogress" , ( e ) => { console . log ( `Downloaded ${ e . loaded * 100 } %` ) ; } ) ; } , // // uncomment if want multimodal input https://developer.chrome.com/docs/ai/prompt-api#multimodal_capabilities // expectedInputs: [ // { type: "audio" }, // { type: "image" } // ] } )

basic important things

the loaded model has 6k token context (just ask for inputQuota without any initialPrompts ):

session . inputQuota // 6144

Now unlike the Gemini Nano team, I happen to be a guy who thinks that function calling/json output is very impt, so let's see how to get this going in Gemini Nano, with prompt examples stolen from Hamel and Jason:

const JSONschema = `<schema> { "description": "Correctly extracted \`UserDetail\` with all the required parameters with correct types", "name": "UserDetail", "parameters": { "properties": { "age": { "title": "Age", "type": "integer" }, "name": { "title": "Name", "type": "string" } }, "required": [ "age", "name" ], "type": "object" } } </schema>` const JSONsession = await LanguageModel . create ( { initialPrompts : [ { role : 'system' , content : 'You are a helpful LLM that only responds in valid JSON fitting a schema: ' + JSONschema } , { role : 'user' , content : "Extract Jason is 35 years old" } , { role : 'assistant' , content : '{age: 35, name: Jason}' } , ] } ) ; const result1 = await JSONsession . prompt ( "Extract sarah is 22 years old" ) ; console . log ( result1 ) ; // {age: 22, name: Sarah}

pitfalls

it doesnt do great instruction following, so required fields aren't really respected:

const result1 = await JSONsession . prompt ( "its been a year since vibhu's birthday, he was 28 last year, guess how old he is now" ) ; console . log ( result1 ) ; // { "age": 29 }

the other thing is that sessions are default stateful, which can be a little nasty if you forget. So a stateless version looks like:

const baseSession = await LanguageModel . create ( { initialPrompts : // blah blah, as above } ) // you can also implement this as a class if you want to force users to use`new` keyword to make super clear it is stateless const statelessSession = { async prompt ( str ) { const clonedSession = await session . clone ( ) return clonedSession . prompt ( str ) } } // these are all stateless calls now! yay repeatability and predictability! const result1 = await statelessSession . prompt ( "Extract sarah is 22 years old" ) ; console . log ( result1 ) ; const result2 = await statelessSession . prompt ( "Extract tanisha is 30 years old" ) ; console . log ( result2 ) ;

pitfalls like these are why you will probably want little wrapper libraries you can handroll or reference https://github.com/kstonekuan/simple-chromium-ai

the last tip here for non js pros is how to import those wrapper libraries in browser contexts (aka without npm install or a build step) using ESM syntax (may need <script type="module"> - run on localhost or a site with relaxed CSP):

---

### Tech
 Philosophy and AI Opportunity (28 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fstratechery.com%2F2025%2Ftech-philosophy-and-ai-opportunity%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/NmUfRLdxYiZdBl0p1-koWXaJRaLHtcINrj-fuGDM0yc=413
**TLDR Summary:** While AI is hailed as the route to abundance, the most important financial outcomes have been about scarcity. One of these scarce resources is AI talent. As the work needed to be done is the same across the various companies bidding for talent, it makes sense that the team that the best researchers play for is the team that pays the most. The teams that are destined to lose are the ones who can't or won't offer enough money or mission.
**Full Article Content:**
Listen to this post: Log in to listen

One of the most paradoxical aspects of AI is that while it is hailed as the route to abundance, the most important financial outcomes have been about scarcity. The first and most obvious example has been Nvidia, whose valuation has skyrocketed while demand for its chips continues to outpace supply:

Another scarce resource that has come to the forefront over the last few months is AI talent; the people who are actually building and scaling the models are suddenly being paid more than professional athletes, and it makes sense:

The potential financial upside from “winning” in AI are enormous

Outputs are somewhat measurable

The work-to-be-done is the same across the various companies bidding for talent

It’s that last point that is fairly unique in tech history. While great programmers have always been in high demand, and there have been periods of intense competition in specific product spaces, over the past few decades tech companies have been franchises, wherein their market niches have been fairly differentiated: Google and search, Amazon and e-commerce, Meta and social media, Microsoft and business applications, Apple and devices, etc. This reality meant that the company mattered more than any one person, putting a cap on individual contributor salaries.

AI, at least to this point, is different: in the long run it seems likely that there will be dominant product companies in various niches, but as long as the game is foundational models, then everyone is in fact playing the same game, which elevates the bargaining power of the best players. It follows, then, that the team they play for is the team that pays the most, through some combination of money and mission; by extension, the teams that are destined to lose are the ones who can’t or won’t offer enough of either.

Apple’s Reluctance

It’s that last point I’m interested in; I’m not in position to judge the value of any of the players changing teams, but the teams are worth examining. Consider Meta and Apple and the latest free agent signing; from Bloomberg:

Apple Inc.’s top executive in charge of artificial intelligence models is leaving for Meta Platforms Inc., another setback in the iPhone maker’s struggling AI efforts. Ruoming Pang, a distinguished engineer and manager in charge of the company’s Apple foundation models team, is departing, according to people with knowledge of the matter. Pang, who joined Apple from Alphabet Inc. in 2021, is the latest big hire for Meta’s new superintelligence group, said the people, who declined to be named discussing unannounced personnel moves. To secure Pang, Meta offered a package worth tens of millions of dollars per year, the people said. Meta Chief Executive Officer Mark Zuckerberg has been on a hiring spree, bringing on major AI leaders including Scale AI’s Alexandr Wang, startup founder Daniel Gross and former GitHub CEO Nat Friedman with high compensation. Meta has also hired Yuanzhi Li, a researcher from OpenAI, and Anton Bakhtin, who worked on Claude at Anthropic PBC, according to other people with knowledge of the matter. Last month, it hired a slew of other OpenAI researchers. Meta, later on Monday, confirmed it is hiring Pang. Apple, Pang, OpenAI and Anthropic didn’t respond to requests for comment.

That Apple is losing AI researchers is a surprise only in that they had researchers worth hiring; after all, this is the company who already implicitly signaled its AI reluctance in terms of that other scarce resource: Nvidia chips. Again from Bloomberg:

Former Chief Financial Officer Luca Maestri’s conservative stance on buying GPUs, the specialized circuits essential to AI, hasn’t aged well either. Under Cook, Apple has used its market dominance and cash hoard to shape global supply chains for everything from semiconductors to the glass for smartphone screens. But demand for GPUs ended up overwhelming supply, and the company’s decision to buy them slowly — which was in line with its usual practice for emerging technologies it isn’t fully sold on — ended up backfiring. Apple watched as rivals such as Amazon and Microsoft Corp. bought much of the world’s supply. Fewer GPUs meant Apple’s AI models were trained all the more slowly. “You can’t magically summon up more GPUs when the competitors have already snapped them all up,” says someone on the AI team.

It may seem puzzling that the company that in its 2024 fiscal year generated $118 billion in free cash flow would be so cheap, but Apple’s reluctance makes sense from two perspectives.

First, the potential impact of AI on Apple’s business prospects, at least in the short term, are fairly small: we still need devices on which to access AI, and Apple continues to own the high end of devices (there is, of course, long-term concern about AI obviating the need for a smartphone, or meaningfully differentiating an alternative platform like Android). That significantly reduces the financial motivation for Apple to outspend other companies in terms of both GPUs and researchers.

Second, AI, at least some of the more fantastical visions painted by companies like Anthropic, is arguably counter to Apple’s entire ethos as a company.

Tech’s Two Philosophies

It was AI, at least the pre-LLM version of it, that inspired me in 2018 to write about Tech’s Two Philosophies; one was represented by Google and Facebook (now Meta):

In Google’s view, computers help you get things done — and save you time — by doing things for you. Duplex was the most impressive example — a computer talking on the phone for you — but the general concept applied to many of Google’s other demonstrations, particularly those predicated on AI: Google Photos will not only sort and tag your photos, but now propose specific edits; Google News will find your news for you, and Maps will find you new restaurants and shops in your neighborhood. And, appropriately enough, the keynote closed with a presentation from Waymo, which will drive you… Zuckerberg, as so often seems to be the case with Facebook, comes across as a somewhat more fervent and definitely more creepy version of Google: not only does Facebook want to do things for you, it wants to do things its chief executive explicitly says would not be done otherwise. The Messianic fervor that seems to have overtaken Zuckerberg in the last year, though, simply means that Facebook has adopted a more extreme version of the same philosophy that guides Google: computers doing things for people.

The other philosophy was represented by Apple and Microsoft:

Earlier this week, while delivering Microsoft’s Build conference keynote, CEO Satya Nadella struck a very different tone…This is technology’s second philosophy, and it is orthogonal to the other: the expectation is not that the computer does your work for you, but rather that the computer enables you to do your work better and more efficiently. And, with this philosophy, comes a different take on responsibility. Pichai, in the opening of Google’s keynote, acknowledged that “we feel a deep sense of responsibility to get this right”, but inherent in that statement is the centrality of Google generally and the direct culpability of its managers. Nadella, on the other hand, insists that responsibility lies with the tech industry collectively, and all of us who seek to leverage it individually. This second philosophy, that computers are an aid to humans, not their replacement, is the older of the two; its greatest proponent — prophet, if you will — was Microsoft’s greatest rival, and his analogy of choice was, coincidentally enough, about transportation as well. Not a car, but a bicycle: I remember reading an article when I was about 12 years old, I think it might have been in Scientific American, where they measured the efficiency of locomotion for all these species on planet earth, how many kilocalories did they expand to get from point A to point B, and the condor came in the top of the list, surpassed everything else, and humans came in about a third of the way down the list, which was not such a great showing for the crown of creation. But somebody there had the imagination to test the efficiency of a human riding a bicycle, and a human riding a bicycle blew away the condor all the way off the top of the list. And it made a really big impression on me that we humans are tool builders, and that we can fashion tools that amplify these inherent abilities that we have to spectacular magnitudes. And so for me a computer has always been a bicycle of the mind, something that takes us far beyond our inherent abilities. I think we’re just at the early stages of this tool, very early stages, and we’ve come only a very short distance, and it’s still in its formation, but already we’ve seen enormous changes. I think that’s nothing compared to what’s coming in the next 100 years.

We are approximately forty years on from that clip, and Steve Jobs’ prediction that enormous changes were still to come is obviously prescient: mobile and the Internet have completely transformed the world, and AI is poised to make those impacts look like peanuts. What I’m interested in in the context of this Article, however, is the interplay between business opportunity — or risk — and philosophy. Apple’s position is here:

In this view the company’s conservatism makes sense: Apple doesn’t quite see the upside of AI for their business (and isn’t overly concerned about the downsides), and its bias towards tools means that AI apps on iPhones are sufficient; Apple might be an increasingly frustrating platform steward, but they are at their core a platform company, and apps on their platform are delivering Apple users AI tools.

This same framework also explains Meta’s aggressiveness. First, the opportunity is huge, as I documented last fall in Meta’s AI Abundance (and, for good measure, there is risk as well, as time — the ultimate scarcity for an advertising-based business — is spent using AI). Second, Meta’s philosophy is that computers do things for you:

Given this graph, is it any surprise that Meta hired away Apple’s top AI talent?

I’m Feeling Lucky

Another way to think about how companies are approaching AI is through the late Professor Clayton Christensen’s discussion around sustaining versus disruptive innovation. From an Update last month after the news of Meta’s hiring spree first started making waves:

The other reason to believe in Meta versus Google comes down to the difference between disruptive and sustaining innovations. The late Professor Clayton Christensen described the difference in The Innovator’s Dilemma: Most new technologies foster improved product performance. I call these sustaining technologies. Some sustaining technologies can be discontinuous or radical in character, while others are of an incremental nature. What all sustaining technologies have in common is that they improve the performance of established products, along the dimensions of performance that mainstream customers in major markets have historically valued. Most technological advances in a given industry are sustaining in character. An important finding revealed in this book is that rarely have even the most radically difficult sustaining technologies precipitated the failure of leading firms. Occasionally, however, disruptive technologies emerge: innovations that result in worse product performance, at least in the near-term. Ironically, in each of the instances studied in this book, it was disruptive technology that precipitated the leading firms’ failure. Disruptive technologies bring to a market a very different value proposition than had been available previously. Generally, disruptive technologies underperform established products in mainstream markets. But they have other features that a few fringe (and generally new) customers value. Products based on disruptive technologies are typically cheaper, simpler, smaller, and, frequently, more convenient to use. The question of whether generative AI is a sustaining or disruptive innovation for Google remains uncertain two years after I raised it. Obviously Google has tremendous AI capabilities both in terms of infrastructure and research, and generative AI is a sustaining innovation for its display advertising business and its cloud business; at the same time, the long-term questions around search monetization remain as pertinent as ever. Meta, however, does not have a search business to potentially disrupt, and a whole host of ways to leverage generative AI across its business; for Zuckerberg and company I think that AI is absolutely a sustaining technology, which is why it ultimately makes sense to spend whatever is necessary to get the company moving in the right direction.

The problem with this analysis is the Google part: how do you square the idea that AI is disruptive to Google with the fact that they are investing just has heavily as everyone else, and in fact started far earlier than everyone else? I think the answer goes back to Google’s founding, and the “I’m Feeling Lucky” button:

While that button is now gone from Google.com, I don’t think it was an accident that it persisted long after it was even usable (instant search results meant that by 2010 you didn’t even have a chance to click it); “I’m Feeling Lucky” was a statement of purpose. From 2016’s Google and the Limits of Strategy:

In yesterday’s keynote, Google CEO Sundar Pichai, after a recounting of tech history that emphasized the PC-Web-Mobile epochs I described in late 2014, declared that we are moving from a mobile-first world to an AI-first one; that was the context for the introduction of the Google Assistant. It was a year prior to the aforementioned iOS 6 that Apple first introduced the idea of an assistant in the guise of Siri; for the first time you could (theoretically) compute by voice. It didn’t work very well at first (arguably it still doesn’t), but the implications for computing generally and Google specifically were profound: voice interaction both expanded where computing could be done, from situations in which you could devote your eyes and hands to your device to effectively everywhere, even as it constrained what you could do. An assistant has to be far more proactive than, for example, a search results page; it’s not enough to present possible answers: rather, an assistant needs to give the right answer. This is a welcome shift for Google the technology; from the beginning the search engine has included an “I’m Feeling Lucky” button, so confident was Google founder Larry Page that the search engine could deliver you the exact result you wanted, and while yesterday’s Google Assistant demos were canned, the results, particularly when it came to contextual awareness, were far more impressive than the other assistants on the market. More broadly, few dispute that Google is a clear leader when it comes to the artificial intelligence and machine learning that underlie their assistant.

The problem — apparent even then — was the conflict with Google’s business model:

A business, though, is about more than technology, and Google has two significant shortcomings when it comes to assistants in particular. First, as I explained after this year’s Google I/O, the company has a go-to-market gap: assistants are only useful if they are available, which in the case of hundreds of millions of iOS users means downloading and using a separate app (or building the sort of experience that, like Facebook, users will willingly spend extensive amounts of time in). Secondly, though, Google has a business-model problem: the “I’m Feeling Lucky” button guaranteed that the search in question would not make Google any money. After all, if a user doesn’t have to choose from search results, said user also doesn’t have the opportunity to click an ad, thus choosing the winner of the competition Google created between its advertisers for user attention. Google Assistant has the exact same problem: where do the ads go?

What I articulated in that Article was Google’s position on this graph:

AI is the ultimate manifestation of “I’m Feeling Lucky”; Google has been pursuing AI because that is why Page and Brin started the company in the first place; business models matter, but they aren’t dispositive, and while that may mean short-term difficulties for Google, it is a reason to be optimistic that the company will figure out AI anyways.

Microsoft, OpenAI, and Anthropic

Frameworks like this are useful, but not fully explanatory; I think this particular one goes a long way towards contextualizing the actions of Apple, Meta, and Google, but is much more speculative for some other relevant AI players. Consider Microsoft, which I would place here:

Microsoft doesn’t have any foundational models of note, but has invested heavily in OpenAI; its most important AI product are its various Copilots, which are indeed a bet on the “tool” philosophy. The question, as I laid out last year in Enterprise Philosophy and the First Wave of AI, is whether rank-and-file employees want Microsoft’s tools:1

Notice, though, how this aligned with the Apple and Microsoft philosophy of building tools: tools are meant to be used, but they take volition to maximize their utility. This, I think, is a challenge when it comes to Copilot usage: even before Copilot came out employees with initiative were figuring out how to use other AI tools to do their work more effectively. The idea of Copilot is that you can have an even better AI tool — thanks to the fact it has integrated the information in the “Microsoft Graph” — and make it widely available to your workforce to make that workforce more productive. To put it another way, the real challenge for Copilot is that it is a change management problem: it’s one thing to charge $30/month on a per-seat basis to make an amazing new way to work available to all of your employees; it’s another thing entirely — a much more difficult thing — to get all of your employees to change the way they work in order to benefit from your investment, and to make Copilot Pages the “new artifact for the AI age”, in line with the spreadsheet in the personal computer age.

This tension explains the anecdotes in this Bloomberg article last month:

OpenAI’s nascent strength in the enterprise market is giving its partner and biggest investor indigestion. Microsoft salespeople describe being caught flatfooted at a time when they’re under pressure to get Copilot into as many customers’ hands as possible. The behind-the-scenes dogfight is complicating an already fraught relationship between Microsoft and OpenAI…It’s unclear whether OpenAI’s momentum with corporations will continue, but the company recently said it has 3 million paying business users, a 50% jump from just a few months earlier. A Microsoft spokesperson said Copilot is used by 70% of the Fortune 500 and paid users have tripled compared with this time last year… This story is based on conversations with more than two dozen customers and salespeople, many of them Microsoft employees. Most of these people asked not to be named in order to speak candidly about the competition between Microsoft and OpenAI. Both companies are essentially pitching the same thing: AI assistants that can handle onerous tasks — researching and writing; analyzing data — potentially letting office workers focus on thornier challenges. Since both chatbots are largely based on the same OpenAI models, Microsoft’s salesforce has struggled to differentiate Copilot from the much better-known ChatGPT, according to people familiar with the situation.

As long as AI usage relies on employee volition, ChatGPT has the advantage; what is interesting about this observation, however, is that it shows that OpenAI is actually in the same position as Microsoft:

This, by extension, explains why Anthropic is different; the other leading independent foundational lab is clearly focused on agents, not chatbots, i.e. AI that does stuff for you, instead of a tool. Consider the contrast between Cursor and Claude Code: Cursor is an integrated development environment (IDE) that provides the best possible UI for AI-augmented programming; Claude Code, on the other hand, barely bothers with a UI at all. It runs in the terminal, which people put up with because it is the best at one-shotting outputs; this X thread was illuminating:

More generally, I wrote in an Update after the release of Claude 4, which was heavily focused on agentic workloads:

This, by extension, means that Anthropic’s goal is what I wrote about in last fall’s Enterprise Philosophy and the First Wave of AI: Computing didn’t start with the personal computer, but rather with the replacement of the back office. Or, to put it in rather more dire terms, the initial value in computing wasn’t created by helping Boomers do their job more efficiently, but rather by replacing entire swathes of them completely…Agents aren’t copilots; they are replacements. They do work in place of humans — think call centers and the like, to start — and they have all of the advantages of software: always available, and scalable up-and-down with demand… Benioff isn’t talking about making employees more productive, but rather companies; the verb that applies to employees is “augmented”, which sounds much nicer than “replaced”; the ultimate goal is stated as well: business results. That right there is tech’s third philosophy: improving the bottom line for large enterprises. Notice how well this framing applies to the mainframe wave of computing: accounting and ERP software made companies more productive and drove positive business results; the employees that were “augmented” were managers who got far more accurate reports much more quickly, while the employees who used to do that work were replaced. Critically, the decision about whether or not to make this change did not depend on rank-and-file employees changing how they worked, but for executives to decide to take the plunge. This strikes me as a very worthwhile goal, at least from a business perspective. OpenAI is busy owning the consumer space, while Google and its best-in-class infrastructure and leading models struggles with product; Anthropic’s task is to build the best agent product in the world, including not just state-of-the-art models but all of the deterministic computing scaffolding that actually makes them replacement-level workers. After all, Anthropic’s API pricing may look expensive relative to Google, but it looks very cheap relative to a human salary.

That means that Anthropic shares the upper-right quadrant with Meta:

Again, this is just one framework; there are others. Moreover, the boundaries are fuzzy. OpenAI is working on agentic workloads, for example, and the hyperscalers all benefit from more AI usage, whether user- or agent-driven; Google, meanwhile, is rapidly evolving Search to incorporate generative AI.

At the same time, to go back to the talent question, I don’t think it’s a surprise that Meta appears to be picking off more researchers from OpenAI than from Anthropic: my suspicion is that to the extent mission is a motivator the more likely an AI researcher is to be enticed by the idea of computers doing everything, instead of merely augmenting humans. And, by extension, the incumbent tool-makers may have no choice but to partner with the true believers.

---

### Tech
 Philosophy and AI Opportunity (28 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fstratechery.com%2F2025%2Ftech-philosophy-and-ai-opportunity%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/NmUfRLdxYiZdBl0p1-koWXaJRaLHtcINrj-fuGDM0yc=413
**TLDR Summary:** While AI is hailed as the route to abundance, the most important financial outcomes have been about scarcity. One of these scarce resources is AI talent. As the work needed to be done is the same across the various companies bidding for talent, it makes sense that the team that the best researchers play for is the team that pays the most. The teams that are destined to lose are the ones who can't or won't offer enough money or mission.
**Full Article Content:**
Listen to this post: Log in to listen

One of the most paradoxical aspects of AI is that while it is hailed as the route to abundance, the most important financial outcomes have been about scarcity. The first and most obvious example has been Nvidia, whose valuation has skyrocketed while demand for its chips continues to outpace supply:

Another scarce resource that has come to the forefront over the last few months is AI talent; the people who are actually building and scaling the models are suddenly being paid more than professional athletes, and it makes sense:

The potential financial upside from “winning” in AI are enormous

Outputs are somewhat measurable

The work-to-be-done is the same across the various companies bidding for talent

It’s that last point that is fairly unique in tech history. While great programmers have always been in high demand, and there have been periods of intense competition in specific product spaces, over the past few decades tech companies have been franchises, wherein their market niches have been fairly differentiated: Google and search, Amazon and e-commerce, Meta and social media, Microsoft and business applications, Apple and devices, etc. This reality meant that the company mattered more than any one person, putting a cap on individual contributor salaries.

AI, at least to this point, is different: in the long run it seems likely that there will be dominant product companies in various niches, but as long as the game is foundational models, then everyone is in fact playing the same game, which elevates the bargaining power of the best players. It follows, then, that the team they play for is the team that pays the most, through some combination of money and mission; by extension, the teams that are destined to lose are the ones who can’t or won’t offer enough of either.

Apple’s Reluctance

It’s that last point I’m interested in; I’m not in position to judge the value of any of the players changing teams, but the teams are worth examining. Consider Meta and Apple and the latest free agent signing; from Bloomberg:

Apple Inc.’s top executive in charge of artificial intelligence models is leaving for Meta Platforms Inc., another setback in the iPhone maker’s struggling AI efforts. Ruoming Pang, a distinguished engineer and manager in charge of the company’s Apple foundation models team, is departing, according to people with knowledge of the matter. Pang, who joined Apple from Alphabet Inc. in 2021, is the latest big hire for Meta’s new superintelligence group, said the people, who declined to be named discussing unannounced personnel moves. To secure Pang, Meta offered a package worth tens of millions of dollars per year, the people said. Meta Chief Executive Officer Mark Zuckerberg has been on a hiring spree, bringing on major AI leaders including Scale AI’s Alexandr Wang, startup founder Daniel Gross and former GitHub CEO Nat Friedman with high compensation. Meta has also hired Yuanzhi Li, a researcher from OpenAI, and Anton Bakhtin, who worked on Claude at Anthropic PBC, according to other people with knowledge of the matter. Last month, it hired a slew of other OpenAI researchers. Meta, later on Monday, confirmed it is hiring Pang. Apple, Pang, OpenAI and Anthropic didn’t respond to requests for comment.

That Apple is losing AI researchers is a surprise only in that they had researchers worth hiring; after all, this is the company who already implicitly signaled its AI reluctance in terms of that other scarce resource: Nvidia chips. Again from Bloomberg:

Former Chief Financial Officer Luca Maestri’s conservative stance on buying GPUs, the specialized circuits essential to AI, hasn’t aged well either. Under Cook, Apple has used its market dominance and cash hoard to shape global supply chains for everything from semiconductors to the glass for smartphone screens. But demand for GPUs ended up overwhelming supply, and the company’s decision to buy them slowly — which was in line with its usual practice for emerging technologies it isn’t fully sold on — ended up backfiring. Apple watched as rivals such as Amazon and Microsoft Corp. bought much of the world’s supply. Fewer GPUs meant Apple’s AI models were trained all the more slowly. “You can’t magically summon up more GPUs when the competitors have already snapped them all up,” says someone on the AI team.

It may seem puzzling that the company that in its 2024 fiscal year generated $118 billion in free cash flow would be so cheap, but Apple’s reluctance makes sense from two perspectives.

First, the potential impact of AI on Apple’s business prospects, at least in the short term, are fairly small: we still need devices on which to access AI, and Apple continues to own the high end of devices (there is, of course, long-term concern about AI obviating the need for a smartphone, or meaningfully differentiating an alternative platform like Android). That significantly reduces the financial motivation for Apple to outspend other companies in terms of both GPUs and researchers.

Second, AI, at least some of the more fantastical visions painted by companies like Anthropic, is arguably counter to Apple’s entire ethos as a company.

Tech’s Two Philosophies

It was AI, at least the pre-LLM version of it, that inspired me in 2018 to write about Tech’s Two Philosophies; one was represented by Google and Facebook (now Meta):

In Google’s view, computers help you get things done — and save you time — by doing things for you. Duplex was the most impressive example — a computer talking on the phone for you — but the general concept applied to many of Google’s other demonstrations, particularly those predicated on AI: Google Photos will not only sort and tag your photos, but now propose specific edits; Google News will find your news for you, and Maps will find you new restaurants and shops in your neighborhood. And, appropriately enough, the keynote closed with a presentation from Waymo, which will drive you… Zuckerberg, as so often seems to be the case with Facebook, comes across as a somewhat more fervent and definitely more creepy version of Google: not only does Facebook want to do things for you, it wants to do things its chief executive explicitly says would not be done otherwise. The Messianic fervor that seems to have overtaken Zuckerberg in the last year, though, simply means that Facebook has adopted a more extreme version of the same philosophy that guides Google: computers doing things for people.

The other philosophy was represented by Apple and Microsoft:

Earlier this week, while delivering Microsoft’s Build conference keynote, CEO Satya Nadella struck a very different tone…This is technology’s second philosophy, and it is orthogonal to the other: the expectation is not that the computer does your work for you, but rather that the computer enables you to do your work better and more efficiently. And, with this philosophy, comes a different take on responsibility. Pichai, in the opening of Google’s keynote, acknowledged that “we feel a deep sense of responsibility to get this right”, but inherent in that statement is the centrality of Google generally and the direct culpability of its managers. Nadella, on the other hand, insists that responsibility lies with the tech industry collectively, and all of us who seek to leverage it individually. This second philosophy, that computers are an aid to humans, not their replacement, is the older of the two; its greatest proponent — prophet, if you will — was Microsoft’s greatest rival, and his analogy of choice was, coincidentally enough, about transportation as well. Not a car, but a bicycle: I remember reading an article when I was about 12 years old, I think it might have been in Scientific American, where they measured the efficiency of locomotion for all these species on planet earth, how many kilocalories did they expand to get from point A to point B, and the condor came in the top of the list, surpassed everything else, and humans came in about a third of the way down the list, which was not such a great showing for the crown of creation. But somebody there had the imagination to test the efficiency of a human riding a bicycle, and a human riding a bicycle blew away the condor all the way off the top of the list. And it made a really big impression on me that we humans are tool builders, and that we can fashion tools that amplify these inherent abilities that we have to spectacular magnitudes. And so for me a computer has always been a bicycle of the mind, something that takes us far beyond our inherent abilities. I think we’re just at the early stages of this tool, very early stages, and we’ve come only a very short distance, and it’s still in its formation, but already we’ve seen enormous changes. I think that’s nothing compared to what’s coming in the next 100 years.

We are approximately forty years on from that clip, and Steve Jobs’ prediction that enormous changes were still to come is obviously prescient: mobile and the Internet have completely transformed the world, and AI is poised to make those impacts look like peanuts. What I’m interested in in the context of this Article, however, is the interplay between business opportunity — or risk — and philosophy. Apple’s position is here:

In this view the company’s conservatism makes sense: Apple doesn’t quite see the upside of AI for their business (and isn’t overly concerned about the downsides), and its bias towards tools means that AI apps on iPhones are sufficient; Apple might be an increasingly frustrating platform steward, but they are at their core a platform company, and apps on their platform are delivering Apple users AI tools.

This same framework also explains Meta’s aggressiveness. First, the opportunity is huge, as I documented last fall in Meta’s AI Abundance (and, for good measure, there is risk as well, as time — the ultimate scarcity for an advertising-based business — is spent using AI). Second, Meta’s philosophy is that computers do things for you:

Given this graph, is it any surprise that Meta hired away Apple’s top AI talent?

I’m Feeling Lucky

Another way to think about how companies are approaching AI is through the late Professor Clayton Christensen’s discussion around sustaining versus disruptive innovation. From an Update last month after the news of Meta’s hiring spree first started making waves:

The other reason to believe in Meta versus Google comes down to the difference between disruptive and sustaining innovations. The late Professor Clayton Christensen described the difference in The Innovator’s Dilemma: Most new technologies foster improved product performance. I call these sustaining technologies. Some sustaining technologies can be discontinuous or radical in character, while others are of an incremental nature. What all sustaining technologies have in common is that they improve the performance of established products, along the dimensions of performance that mainstream customers in major markets have historically valued. Most technological advances in a given industry are sustaining in character. An important finding revealed in this book is that rarely have even the most radically difficult sustaining technologies precipitated the failure of leading firms. Occasionally, however, disruptive technologies emerge: innovations that result in worse product performance, at least in the near-term. Ironically, in each of the instances studied in this book, it was disruptive technology that precipitated the leading firms’ failure. Disruptive technologies bring to a market a very different value proposition than had been available previously. Generally, disruptive technologies underperform established products in mainstream markets. But they have other features that a few fringe (and generally new) customers value. Products based on disruptive technologies are typically cheaper, simpler, smaller, and, frequently, more convenient to use. The question of whether generative AI is a sustaining or disruptive innovation for Google remains uncertain two years after I raised it. Obviously Google has tremendous AI capabilities both in terms of infrastructure and research, and generative AI is a sustaining innovation for its display advertising business and its cloud business; at the same time, the long-term questions around search monetization remain as pertinent as ever. Meta, however, does not have a search business to potentially disrupt, and a whole host of ways to leverage generative AI across its business; for Zuckerberg and company I think that AI is absolutely a sustaining technology, which is why it ultimately makes sense to spend whatever is necessary to get the company moving in the right direction.

The problem with this analysis is the Google part: how do you square the idea that AI is disruptive to Google with the fact that they are investing just has heavily as everyone else, and in fact started far earlier than everyone else? I think the answer goes back to Google’s founding, and the “I’m Feeling Lucky” button:

While that button is now gone from Google.com, I don’t think it was an accident that it persisted long after it was even usable (instant search results meant that by 2010 you didn’t even have a chance to click it); “I’m Feeling Lucky” was a statement of purpose. From 2016’s Google and the Limits of Strategy:

In yesterday’s keynote, Google CEO Sundar Pichai, after a recounting of tech history that emphasized the PC-Web-Mobile epochs I described in late 2014, declared that we are moving from a mobile-first world to an AI-first one; that was the context for the introduction of the Google Assistant. It was a year prior to the aforementioned iOS 6 that Apple first introduced the idea of an assistant in the guise of Siri; for the first time you could (theoretically) compute by voice. It didn’t work very well at first (arguably it still doesn’t), but the implications for computing generally and Google specifically were profound: voice interaction both expanded where computing could be done, from situations in which you could devote your eyes and hands to your device to effectively everywhere, even as it constrained what you could do. An assistant has to be far more proactive than, for example, a search results page; it’s not enough to present possible answers: rather, an assistant needs to give the right answer. This is a welcome shift for Google the technology; from the beginning the search engine has included an “I’m Feeling Lucky” button, so confident was Google founder Larry Page that the search engine could deliver you the exact result you wanted, and while yesterday’s Google Assistant demos were canned, the results, particularly when it came to contextual awareness, were far more impressive than the other assistants on the market. More broadly, few dispute that Google is a clear leader when it comes to the artificial intelligence and machine learning that underlie their assistant.

The problem — apparent even then — was the conflict with Google’s business model:

A business, though, is about more than technology, and Google has two significant shortcomings when it comes to assistants in particular. First, as I explained after this year’s Google I/O, the company has a go-to-market gap: assistants are only useful if they are available, which in the case of hundreds of millions of iOS users means downloading and using a separate app (or building the sort of experience that, like Facebook, users will willingly spend extensive amounts of time in). Secondly, though, Google has a business-model problem: the “I’m Feeling Lucky” button guaranteed that the search in question would not make Google any money. After all, if a user doesn’t have to choose from search results, said user also doesn’t have the opportunity to click an ad, thus choosing the winner of the competition Google created between its advertisers for user attention. Google Assistant has the exact same problem: where do the ads go?

What I articulated in that Article was Google’s position on this graph:

AI is the ultimate manifestation of “I’m Feeling Lucky”; Google has been pursuing AI because that is why Page and Brin started the company in the first place; business models matter, but they aren’t dispositive, and while that may mean short-term difficulties for Google, it is a reason to be optimistic that the company will figure out AI anyways.

Microsoft, OpenAI, and Anthropic

Frameworks like this are useful, but not fully explanatory; I think this particular one goes a long way towards contextualizing the actions of Apple, Meta, and Google, but is much more speculative for some other relevant AI players. Consider Microsoft, which I would place here:

Microsoft doesn’t have any foundational models of note, but has invested heavily in OpenAI; its most important AI product are its various Copilots, which are indeed a bet on the “tool” philosophy. The question, as I laid out last year in Enterprise Philosophy and the First Wave of AI, is whether rank-and-file employees want Microsoft’s tools:1

Notice, though, how this aligned with the Apple and Microsoft philosophy of building tools: tools are meant to be used, but they take volition to maximize their utility. This, I think, is a challenge when it comes to Copilot usage: even before Copilot came out employees with initiative were figuring out how to use other AI tools to do their work more effectively. The idea of Copilot is that you can have an even better AI tool — thanks to the fact it has integrated the information in the “Microsoft Graph” — and make it widely available to your workforce to make that workforce more productive. To put it another way, the real challenge for Copilot is that it is a change management problem: it’s one thing to charge $30/month on a per-seat basis to make an amazing new way to work available to all of your employees; it’s another thing entirely — a much more difficult thing — to get all of your employees to change the way they work in order to benefit from your investment, and to make Copilot Pages the “new artifact for the AI age”, in line with the spreadsheet in the personal computer age.

This tension explains the anecdotes in this Bloomberg article last month:

OpenAI’s nascent strength in the enterprise market is giving its partner and biggest investor indigestion. Microsoft salespeople describe being caught flatfooted at a time when they’re under pressure to get Copilot into as many customers’ hands as possible. The behind-the-scenes dogfight is complicating an already fraught relationship between Microsoft and OpenAI…It’s unclear whether OpenAI’s momentum with corporations will continue, but the company recently said it has 3 million paying business users, a 50% jump from just a few months earlier. A Microsoft spokesperson said Copilot is used by 70% of the Fortune 500 and paid users have tripled compared with this time last year… This story is based on conversations with more than two dozen customers and salespeople, many of them Microsoft employees. Most of these people asked not to be named in order to speak candidly about the competition between Microsoft and OpenAI. Both companies are essentially pitching the same thing: AI assistants that can handle onerous tasks — researching and writing; analyzing data — potentially letting office workers focus on thornier challenges. Since both chatbots are largely based on the same OpenAI models, Microsoft’s salesforce has struggled to differentiate Copilot from the much better-known ChatGPT, according to people familiar with the situation.

As long as AI usage relies on employee volition, ChatGPT has the advantage; what is interesting about this observation, however, is that it shows that OpenAI is actually in the same position as Microsoft:

This, by extension, explains why Anthropic is different; the other leading independent foundational lab is clearly focused on agents, not chatbots, i.e. AI that does stuff for you, instead of a tool. Consider the contrast between Cursor and Claude Code: Cursor is an integrated development environment (IDE) that provides the best possible UI for AI-augmented programming; Claude Code, on the other hand, barely bothers with a UI at all. It runs in the terminal, which people put up with because it is the best at one-shotting outputs; this X thread was illuminating:

More generally, I wrote in an Update after the release of Claude 4, which was heavily focused on agentic workloads:

This, by extension, means that Anthropic’s goal is what I wrote about in last fall’s Enterprise Philosophy and the First Wave of AI: Computing didn’t start with the personal computer, but rather with the replacement of the back office. Or, to put it in rather more dire terms, the initial value in computing wasn’t created by helping Boomers do their job more efficiently, but rather by replacing entire swathes of them completely…Agents aren’t copilots; they are replacements. They do work in place of humans — think call centers and the like, to start — and they have all of the advantages of software: always available, and scalable up-and-down with demand… Benioff isn’t talking about making employees more productive, but rather companies; the verb that applies to employees is “augmented”, which sounds much nicer than “replaced”; the ultimate goal is stated as well: business results. That right there is tech’s third philosophy: improving the bottom line for large enterprises. Notice how well this framing applies to the mainframe wave of computing: accounting and ERP software made companies more productive and drove positive business results; the employees that were “augmented” were managers who got far more accurate reports much more quickly, while the employees who used to do that work were replaced. Critically, the decision about whether or not to make this change did not depend on rank-and-file employees changing how they worked, but for executives to decide to take the plunge. This strikes me as a very worthwhile goal, at least from a business perspective. OpenAI is busy owning the consumer space, while Google and its best-in-class infrastructure and leading models struggles with product; Anthropic’s task is to build the best agent product in the world, including not just state-of-the-art models but all of the deterministic computing scaffolding that actually makes them replacement-level workers. After all, Anthropic’s API pricing may look expensive relative to Google, but it looks very cheap relative to a human salary.

That means that Anthropic shares the upper-right quadrant with Meta:

Again, this is just one framework; there are others. Moreover, the boundaries are fuzzy. OpenAI is working on agentic workloads, for example, and the hyperscalers all benefit from more AI usage, whether user- or agent-driven; Google, meanwhile, is rapidly evolving Search to incorporate generative AI.

At the same time, to go back to the talent question, I don’t think it’s a surprise that Meta appears to be picking off more researchers from OpenAI than from Anthropic: my suspicion is that to the extent mission is a motivator the more likely an AI researcher is to be enticed by the idea of computers doing everything, instead of merely augmenting humans. And, by extension, the incumbent tool-makers may have no choice but to partner with the true believers.

---

### CTOs
 Reveal How AI Changed Software Developer Hiring in 2025 (18 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.finalroundai.com%2Fblog%2Fsoftware-developer-skills-ctos-want-in-2025%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/NP_O8GY2P1xEZuUqxGqCLnJyLt9-jtxqJIOG2d_sK9o=413
**TLDR Summary:** While AI evangelists promise the technology will make everyone become a '10x developer', the reality is that companies are drowning in AI-generated code that looks perfect but breaks in production. The most valuable developers aren't the ones churning out AI code, but the ones who can think their way out of the problems AI creates. Engineering leaders want developers who can look at AI-generated code and figure out what's wrong with it instead of just accepting whatever the AI produces. AI was supposed to make coding easier, but it's actually making the thinking parts of development more valuable than ever.
**Full Article Content:**
AI is turning every junior developer into a code factory and every senior developer into a janitor.

That's the brutal reality we are seeing across the industry right now. While AI evangelists promise that everyone will become a "10x developer," what's actually happening is that companies are drowning in AI-generated code that looks perfect but breaks in production.

So we asked the people who actually have to deal with this mess: CTOs and engineering leaders who are hiring developers in 2025.

What we found might surprise the AI hype machine.

We asked one simple question: "What skill do you now look for when hiring developers that you didn't care about as much before AI?"

Spoiler: "They're not hiring prompt engineers".

Here's what these leaders told us and why it proves that the most valuable developers aren't the ones churning out AI code, but the ones who can think their way out of the problems AI creates.



Critical Thinking Over Code Generation

Most engineering leaders said the same thing: they want developers who can look at AI-generated code and figure out what's wrong with it, not just accept whatever the AI spits out.

1. "AI Often Gives Confident But Wrong Answers"

For us, critical thinking and healthy skepticism are now a priority. AI often gives "confident but wrong" answers - the developer must doubt. The key to quality is the ability to test assumptions. Without critical thinking, a developer can believe false results.

At the interview, we demonstrate this skill as follows:

We add errors or ambiguities to the task condition. We monitor whether the candidate asks clarifying questions. We ask the candidate to evaluate the code in terms of risks, not just functionality.

The approach to hiring has changed:

We give more open-ended tasks without clear instructions. The way of thinking becomes more important than a template solution. We actively involve behavioral interviews to check resistance to "false confidence."

Taras Tymoshchuk, CEO, Co-Founder, Geniusee

2. "The Best Candidates Treat AI Like a Junior Teammate"

One skill I'm prioritizing now is "critical thinking in code validation". Essentially, the ability to question and verify what AI tools produce rather than assuming it's correct.

With AI assistants like Copilot or ChatGPT generating boilerplate and even complex code, developers are moving faster but the risk of subtle bugs, security holes, or performance issues creeping in has increased. What sets apart strong engineers now is their instinct to pause and ask,

Does this really do what I think it does?

Could there be an edge case?"

They're not just consuming AI outputs; they're auditing them.

I've adjusted interviews to include AI-assisted coding rounds. For example, I'll have the candidate use an AI tool to scaffold a solution, then ask them to explain potential failure points or suggest tests to validate it. I also like giving them slightly flawed AI-generated code and asking them to debug or refactor it on the spot. Those who can calmly dissect and improve on AI's output stand out.

Has AI changed how I hire? Yes. I'm less focused on speed typing or memorizing syntax and more on design, reasoning, and their ability to collaborate with AI tools. The best candidates treat AI like a junior teammate: helpful, but not infallible.



One great example: I hired a mid-level developer who impressed me by catching a subtle concurrency bug in code Copilot wrote. She sketched out how she'd test and refactor it and showing the exact mindset I now value.

Vipul Mehta, Co-Founder & CTO, WeblineGlobal

3. "That Moment of Scrutiny Saved Us From a Patient Safety Issue"

We recently interviewed a developer for a healthcare app project. During a test, we handed over AI-generated code that looked clean on the surface. Most candidates moved on. However, this particular candidate paused and flagged a subtle issue: the way the AI handled HL7 timestamps could delay remote patient vitals syncing. That mistake might have gone live and risked clinical alerts.

Thanks to that moment of scrutiny, we avoided what could have been a serious patient safety issue. We later found this fix would have prevented potential liability and saved us thousands in rework.

Now, I look for developers who challenge AI outputs, ask, "What if this breaks?" and think about how code behaves in the real world. It's not about knowing more; it's about thinking deeper.

If you're hiring in any field touched by AI, test how candidates respond when the machine is wrong. That's where the real talent shows up.

Riken Shah, Founder & CEO, OSP Labs

4. "We Need Developers Who Can Spot When AI Gets It Wrong"

One skill we've started prioritizing in hiring is how well developers can think critically about AI-generated code. With tools like GitHub Copilot and ChatGPT in the mix, it's easy for someone to accept whatever output they get without questioning it. That's risky.

We need people who can pause, review what the AI produced, and ask:

Does this actually fit our architecture?

Is it secure?

Could this break under certain conditions?

This ability to analyze and challenge AI suggestions is now just as important as writing clean code.

In the interview, we often show the candidates a code snippet from the AI tool and ask them to review it. The best candidates do not just point out syntax issues. They notice design flaws, security gaps, or ways to improve maintainability.

AI has not really changed who we hire, but it has changed how we evaluate. We now focus more on how candidates collaborate with AI, instead of treating AI as magic they can rely on blindly.

Vikrant Bhalodia, Head of Marketing & People Ops, WeblineIndia

Systems Thinking: The New Competitive Advantage

Multiple leaders emphasized that while AI can write individual functions, it cannot understand how systems work together at scale.

5. "AI Can Write Code, But It Can't Think About How Systems Scale"

As a CTO in 2025, one of the skills I am beginning to prioritize while hiring developers is system design. With AI eliminating much of the mundane coding, developers are now primarily called upon to design scalable, efficient, and flexible systems. While AI can write code, it cannot think critically about how different parts of a system will interact and scale in the future. This is where human judgment plays a crucial role.

When hiring now, I place more emphasis on candidates who can abstract complex problems and design architecture with the future in mind. During interviews, I like to ask them about specific real-world examples where they had to design a system from the ground up or optimize an existing one. I ask them to walk me through their "space of solutions" and the trade-offs they considered, how they addressed scaling issues, and what they learned in the process.

AI hasn't made hiring easier. It has actually altered how we evaluate developers. While technical knowledge remains important, I increasingly search for problem-solving and big-picture thinking skills. AI tools are just that tools. What truly matters is how developers utilize these tools to solve challenging problems that require a deep understanding of systems and design.

Jason Hishmeh, Author | CTO | Founder | Tech Investor, Varyence

6. "We've Seen Perfect Code Break Under Real-World Pressure"

One skill I now prioritize is systems thinking, the ability to understand how different parts of a solution work together and how to design for long-term performance and flexibility.

AI tools like GitHub Copilot and ChatGPT have boosted developer productivity by up to 55%, but this shift has moved the real value away from just writing code. Developers now spend more time debugging, integrating, and making architectural decisions. So, we look for people who think in systems.

We've seen cases where the code looked perfect but broke under real-world pressure due to overlooked issues like caching or database bottlenecks. That's why we don't rely solely on technical tests anymore.

In interviews, we focus on:

Real-world problem solving: "How would you scale a CRM module or reduce loading times during peak usage?" Design reviews: "We show a flawed system plan and ask candidates how they would fix or improve it."

The strongest candidates explain their thinking clearly and understand the trade-offs. We're also cautious with candidates who can only talk about tools or frameworks but struggle to explain the reasoning behind their decisions. That's a red flag, especially now.

Royal Rovshan, CTO & Product Manager, Vitanur

7. "AI Handles Basic Code Generation, Developers Create Structure"

One specific skill we now prioritize is systems thinking. We look for developers who understand how code connects to broader architecture, user experience, and operational impact. Writing functions is one piece of the work. Designing durable, scalable solutions is what drives long-term value.

Why it matters more now: AI handles basic code generation. Developers who think in systems create structure, reduce risk, and support growth. They make better decisions at every layer of the product.

How do we spot it? We give real-world scenarios and ask candidates how they would design, build, and scale a solution. We listen to how they reason through complexity, define priorities, and anticipate impact. This shows how they approach real work.

How AI has changed our hiring process: We focus on judgment, context, and tool fluency. Developers who understand how to integrate AI into their workflow move faster with precision.

We prioritize those who lead with structure and understand the business impact of their technical choices.

Alex Smereczniak, Co-Founder & CEO, Franzy

Understanding the Business Behind the Code

Several leaders noted that AI excels at writing technically correct code but completely misses business requirements.

8. "We Used to Hire People Who Could Code; Now We Hire People Who Can Think"

One specific skill being prioritized due to AI is Business Context Translation. the ability to understand complex client requirements and guide AI tools towards actual solutions, not just technically correct code. We have observed AI generate perfect authentication systems when clients only needed simple login bypasses. Our most valuable developers now bridge this gap between business needs and AI execution.

I present candidates with complex, real-world scenarios such as: "A restaurant owner claims their 'online ordering is broken' but customers are successfully placing orders." Strong candidates don't immediately resort to coding - they ask clarifying questions about customer complaints, payment issues, or interface problems.

Everything has changed. We used to hire people who could code; now we hire people who can think, then use AI to code their thoughts. We have replaced traditional coding tests with "problem-solving simulations" using real client scenarios and AI tools. We are hiring more "technical translators" - hybrids who bridge business needs and AI capabilities. Surprisingly, our best new hires often have less coding experience but stronger communication skills. Our interviews now include client role-playing and requirement gathering exercises. We're testing interpretation and AI collaboration skills, not algorithm memorization.

Cache Merrill, Founder, Zibtek

9. "AI Can Help With Implementation, But Only Humans Understand Business Needs"

While AI is now capable of writing code efficiently, it still lacks the ability to frame problems that need to be solved or determine exactly what to build. Because of this, the skill I prioritize most when hiring developers today, far more than before AI, is system design and architecture.

My clients want candidates who can design robust, scalable systems that directly address core business problems. AI can help with implementation, but only humans can deeply understand business needs and translate them into effective architectures. That's why system design has become such a critical differentiator in 2025.

To assess this capability, I use a blend of strategies during interviews. I ask open-ended system design questions and scenario prompts like, "How would you design for resiliency at scale?" I also incorporate whiteboard architecture problems to see how candidates structure their thinking. I listen for whether they approach the problem step by step, clarify assumptions, and thoughtfully consider trade-offs rather than jumping straight to code.

Archie Payne, Co-Founder & President, CalTek Staffing

10. "Engineers Who Integrate Business Insights Into Technical Decisions Thrive"

One skill that I've prioritized in hiring is product mindset. This is especially true for product engineers, who blend technical expertise with a deep understanding of business goals and user needs.

AI tools like Copilot and Cursor have automated many routine coding tasks, freeing engineers to focus on more strategic aspects of product development. This shift requires a broader perspective as they now need to not only write code but also understand the business implications and user value of their work. I believe that the ability to see the big picture and align technical solutions with business objectives has become essential.

When evaluating candidates, I look for their ability to understand and clearly articulate business goals and user needs, break down complex problems, define what actually needs to be done, and propose solutions from a product perspective rather than just a technical one. I want to see how they bridge the gap between business teams, designers, and analysts — connecting "what we want" with "how to achieve it" and how they engage meaningfully in planning, prioritization, and strategic decision-making.

In my experience, engineers who integrate business insights into technical decisions thrive in this environment. For example, one candidate I interviewed had collaborated with a Product Owner to assess market impact before developing a new feature, ensuring resources were invested wisely. I've also seen developers who focus solely on technical tasks without considering the broader business context struggle to adapt.

‍

The integration of AI in development has elevated product mindset from a nice-to-have to an essential skill, fundamentally transforming how I approach hiring to prioritize candidates who can think strategically and collaborate across functions to drive product success.

Maxim Ivanov, Chief Executive Officer, Aimprosoft

Debugging AI Is the New Interview Test

Multiple leaders highlighted that debugging AI code requires different skills than debugging code you wrote yourself.

11. "We're Hiring AI Editors, Interpreters, and Sense-Makers"

One skill we now actively seek is contextual thinking in debugging AI-assisted code.

With tools like GitHub Copilot or ChatGPT helping generate substantial amounts of logic, many junior and even mid-level developers rely too heavily on suggestions without truly understanding why the code works or why it doesn't.

AI is fast, but it's not always correct. Consequently, debugging has become less about syntax errors and more about identifying logic gaps, edge cases, and side effects that AI might overlook.

We once had a strong candidate who excelled in all the Data Structures and Algorithms (DSA) rounds and built applications using AI tools. However, when we gave him a prompt to debug an AI-generated code that subtly misused asynchronous handling in Node.js, he couldn't discern what the code was attempting to do before trying to fix it. That's now considered a red flag.

To test this, we give candidates an AI-written function and ask: "What do you think this was supposed to do?" Then, "What could go wrong?" We're not just testing debugging skills; we're assessing how well they think like a human.

So yes, AI has indeed changed our hiring process. We're no longer just hiring developers; we're hiring AI editors, interpreters, and sense-makers.

Jigar Shah, Founder & CEO, WPWeb Infotech

12. "She Spent 15 Minutes Asking Smart Questions Before Writing Any Code"

AI has profoundly changed how we hire developers, though perhaps in subtle yet powerful ways. It's undeniably less about assessing raw coding speed or memorized algorithms and far more about evaluating strategic thinking and adaptability. Our coding challenges now very often start with a fully functional AI assistant at the candidate's disposal.

I actually remember one candidate who really impressed me recently, Ana, let's call her that. We'd given her this task to build a pretty specific data processing pipeline. Instead of just jumping straight into coding, she spent her first fifteen minutes, a full fifteen minutes - asking incredibly smart questions about data sources, expected volumes, how we'd handle errors, and even future scalability. Then, when she finally did use an AI tool, she made it quite clear she was concerned about a suggested for loop's efficiency for really large datasets. So, she intelligently re-prompted the AI, asking for a more optimized, vectorized approach.

We're definitely shifting our focus from just assessing pure coding ability to evaluating deep problem-solving acumen, keen architectural foresight, and that nuanced, uniquely human ability to question, reason effectively, and adapt swiftly. Developers who can critically assess and skillfully guide AI, rather than just be passively guided by it, are the ones who will truly drive meaningful innovation and provide lasting, invaluable contributions in 2025 and beyond.

André Ahlert, CEO and Managing Partner, AEX

The Bottom Line

While everyone's debating whether AI will replace developers, the people actually hiring them are looking for the opposite of what you'd expect. They don't want prompt engineers or AI evangelists. They want the developers who can clean up the mess AI creates.



The irony is perfect: AI was supposed to make coding easier, but it's actually making the thinking parts of development more valuable than ever.

Companies are learning the hard way that AI-generated code comes with hidden costs. The developers who can spot those costs upfront are going to be in high demand.

If you're worried about AI taking your job, stop.



The companies that figure this out first are going to need more developers, not fewer. They just want developers who can think, not just code.

---

## Quick Links

### Craving
 more AI in your inbox? (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Ftldr.tech%2Fai%2F%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=quicklinks07092025/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/jn4vt1U28F-1_4t2j_EO8pztxlNVdFd_HJgK1RCORcQ=413
**TLDR Summary:** TLDR AI is your daily fix of LLMs, GenAI, and deep learning goodness. Same TLDR format. Still free. Subscribe now.
**Full Article Content:**
🧠

The most important AI, ML, and data science news in a free daily email.

Sign Up

Join 500,000 readers for one daily email

---

### Craving
 more AI in your inbox? (Sponsor)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Ftldr.tech%2Fai%2F%3Futm_source=tldr%26utm_medium=newsletter%26utm_campaign=quicklinks07092025/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/jn4vt1U28F-1_4t2j_EO8pztxlNVdFd_HJgK1RCORcQ=413
**TLDR Summary:** TLDR AI is your daily fix of LLMs, GenAI, and deep learning goodness. Same TLDR format. Still free. Subscribe now.
**Full Article Content:**
🧠

The most important AI, ML, and data science news in a free daily email.

Sign Up

Join 500,000 readers for one daily email

---

### Apple
 says COO Jeff Williams will retire from company later this year (3 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.cnbc.com%2F2025%2F07%2F08%2Fapple-says-coo-jeff-williams-handing-over-role-to-sabih-khan-this-month.html%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/ojVYcwtB0xeDl2D7JRV5BOOYH72aLkFGwxKFDm_bFOY=413
**TLDR Summary:** Sabih Khan, Apple's senior vice president of operations, will be taking over the COO role as part of along-planned succession.
**Full Article Content:**
Jeff Williams, chief operating officer of Apple Inc., during the Apple Worldwide Developers Conference (WWDC) at Apple Park campus in Cupertino, California, US, on Monday, June 9, 2025.

Apple said on Tuesday that Chief Operating Officer Jeff Williams, a 27-year company veteran, will be retiring later this year.

Current operations leader Sabih Khan will take over much of the COO role later this month, Apple said in a press release. For his remaining time with the company, Williams will continue to head up Apple's design team, Apple Watch, and health initiatives, reporting to CEO Tim Cook.

Williams becomes the latest longtime Apple executive to step down as key employees, who were active in the company's hyper-growth years, reach retirement age. Williams, 62, previously headed Apple's formidable operations division, which is in charge of manufacturing millions of complicated devices like iPhones, while keeping costs down.

He also led important teams inside Apple, including the company's fabled industrial design team, after longtime leader Jony Ive retired in 2019. When Williams retires, Apple's design team will report to CEO Tim Cook, Apple said.

"He's helped to create one of the most respected global supply chains in the world; launched Apple Watch and overseen its development; architected Apple's health strategy; and led our world class team of designers with great wisdom, heart, and dedication," Cook said in the statement.

Williams said he plans to spend more time with friends and family.

"June marked my 27th anniversary with Apple, and my 40th in the industry," Williams said in the release.

Williams is leaving Apple at a time when its famous supply chain is under significant pressure, as the U.S. imposes tariffs on many of the countries where Apple sources its devices, and White House officials publicly pressure Apple to move more production to the U.S.

Khan was added to Apple's executive team in 2019, taking an senior vice president title. Apple said on Tuesday that he will lead supply chain, product quality, planning, procurement, and fulfillment at Apple.

The operations leader joined Apple's procurement group in 1995, and before that worked as an engineer and technical leader at GE Plastics. He has a bachelor's degree from Tufts University and a master's degree in mechanical engineering from Rensselaer Polytechnic Institute in upstate New York.

Khan has worked closely with Cook. Once, during a meeting when Cook said that a manufacturing problem was "really bad," Khan stood up and drove to the airport, and immediately booked a flight to China to fix it, according to an anecdote published in Fortune.

WATCH: Jefferies upgrades Apple

---

### How
 I build software quickly (10 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fevanhahn.com%2Fhow-i-build-software-quickly%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/1s5sCLVpu7-KhUtg7zzO4ZJPEIDFDutc8Vorwj0Omj0=413
**TLDR Summary:** Know how good your code needs to be for the task at hand, start with a rough draft/spike, try to soften requirements if you can, don't get distracted, make small changes, and practice specific skills.
**Full Article Content:**
Software is built under time and quality constraints. We want to write good code and have it done quickly.

If you go too fast, your work is buggy and hard to maintain. If you go too slowly, nothing gets shipped. I have not mastered this tension, but I’ll share a few lessons I’ve learned.

This post focuses on being a developer on a small team, maintaining software over multiple years. It doesn’t focus on creating quick prototypes. And this is only based on my own experience!

“How good should this be?”

Early in my career, I wanted all my code to be perfect: every function well-tested, every identifier elegantly named, every abstraction easily understood. And absolutely no bugs!

But I learned a lesson that now seems obvious in hindsight: there isn’t one “right way” to build software.

For example, if you’re making a game for a 24-hour game jam, you probably don’t want to prioritize clean code. That would be a waste of time! Who really cares if your code is elegant and bug-free?

On the other hand, if you’re building a pacemaker device, a mistake could really hurt someone. Your work should be much better! I wouldn’t want to risk my life with someone’s spaghetti code!

Most of my work has been somewhere in the middle. Some employers have aggressive deadlines where some bugs are acceptable, while other projects demand a higher quality bar with more relaxed schedules. Sussing this out has helped me determine where to invest my time. What is my team’s idea of “good enough”? What bugs are acceptable, if any? Where can I do a less-than-perfect job if it means getting things done sooner?

In general, my personal rule of thumb is to aim for an 8 out of 10 score, delivered on time. The code is good and does its job. It has minor issues but nothing major. And it’s done on time! (To be clear, I aim for this. I don’t always hit it!) But again, it depends on the project—sometimes I want a perfect score even if it’s delayed, and other times I write buggy code that’s finished hastily.

Rough drafts

Software, like writing, can benefit from a rough draft. This is sometimes called a “spike” or a “walking skeleton”.

I like implementing a rough draft as quickly as I can. Later, I shape it into the final solution.

My rough draft code is embarrassing. Here are some qualities of my typical spikes:

Lots of bugs and failed test cases.

Dozens of TODO comments.

comments. Error cases are not handled. (I recently had a branch where an error message was logged 20 times per second.)

print() statements everywhere.

statements everywhere. No regard for performance.

Commit messages are just three letters: “WIP”, short for “work in progress”.

3 packages were added and none of them are used anymore.

Lots of code is unnecessarily repeated.

Data is hard-coded.

The linter is angry.

This sounds pretty bad, but it has one important quality: it vaguely resembles a good solution.

As you might imagine, I fix these mistakes before the final patch!

This “rough draft” approach has a few advantages:

It can reveal “unknown unknowns”. Often, prototypes uncover things I couldn’t have anticipated. It’s generally good to discover those ASAP, not after I’ve perfected some code that ultimately gets discarded.

Lots of these problems disappear over the course of the rough draft and I never have to fix them. For example, I write a function that’s too slow but works well enough for a prototype. Later, I realize I didn’t need that function at all. Good thing I didn’t waste time speeding it up! (I can’t tell you how many functions I’ve fully unit tested and then deleted. What a waste of time!)

It helps me focus . I’m not fixing a problem in another part of the codebase or worrying about the perfect function name. I’m speedrunning this rough draft to understand the problem better.

It helps me avoid premature abstractions . If I’m rushing to get something ugly working, I’m less likely to try to build some byzantine abstraction. I build what I need for the specific problem, not what I think I might need for future problems that may never come.

It becomes easier to communicate progress to others in two ways: first, I can usually give a more accurate estimate of when I’ll be done because I know approximately what’s left. Second, I can demo something, which helps stakeholders understand what I’m building and provide better feedback. This feedback might change the direction of the work, which is better to know sooner.

Here are some concrete things I do when building rough drafts:

Focus on binding decisions. Some choices, like the selection of programming language or database schema design, can be hard to change later. A rough draft is a good time for me to explore these, and make sure I’m not boxing myself into a choice that I’ll regret in a year.

Keep track of hacks. Every time I cut a corner, I add a TODO comment or equivalent. Later, when it’s time for polish, I run git grep TODO to see everything that needs attention.

Build “top to bottom”. For example, in an application, I prefer to scaffold the UI before the business logic, even if lots of stuff is hard-coded. I’ve sometimes written business logic first, which I later discarded once the UI came into play, because I miscalculated how it would be used. Build the top layer first—the “dream code” I want to write or the API I wish existed—rather than trying to build the “bottom” layer first. It’s easier to make the right API decisions when I start with how it will be used. It can also be easier to gather feedback on.

Extract smaller changes while working. Sometimes, during a rough draft, I realize that some improvement needs to be made elsewhere in the code. Maybe there’s a dependency that needs updating. Before finishing the final draft, make a separate patch to just update that dependency. This is useful on its own and will benefit the upcoming change. I can push it for code review separately, and hopefully, it’ll be merged by the time I finish my final draft.

See also: “Throw away your first draft of your code” and “Best Simple System for Now”. “YAGNI” is also somewhat related to this topic.

Try to change the requirements

Generally, doing less is faster and easier! Depending on the task, you may be able to soften the requirements.

Some example questions to ask:

Could I combine multiple screens into one?

Is it okay if we don’t handle a particularly tricky edge case?

Instead of an API supporting 1000 inputs, what if it just supported 10?

Is it okay to build a prototype instead of a full version?

What if we didn’t do this at all?

More generally, I sometimes try to nudge the culture of the organization towards a slower pace. This is a big topic, and I’m no expert on organizational change! But I’ve found that making big demands rarely works; I’ve had better luck with small, gradual suggestions that slowly shift discussions. I don’t know much about unionizing, but I wonder if it could help here too.

Avoid wandering through the code

The modern world is full of distractions: notifications from your phone, messages from colleagues, and dreaded meetings. I don’t have smart answers for handling these.

But there’s another kind of distraction: I start wandering through the code. I begin working on one thing, and two hours later, I’m changing something completely unrelated. Maybe I’m theoretically being productive and improving the codebase, but that bug I was assigned isn’t getting fixed! I’m “lost in the sauce”!

I’ve found two concrete ways to manage this:

Set a timer. When I start working on a discrete task, I often set a timer. Maybe I think this function is going to take me 15 minutes to write. Maybe I think it’ll take me 1 hour to understand the source of this bug. My estimates are frequently wrong, but when the timer goes off, I’m often jolted out of some silly distraction. And there’s nothing as satisfying as running git commit right as my timer goes off—a perfect estimation. (This also helps me practice the impossible art of time estimation, though I’m still not great at it.)

Pair programming helps keep me focused. Another soul is less likely to let me waste their time with some rabbit hole.

Some programmers naturally avoid this kind of distraction, but not me! Discipline and deliberate action help me focus.

Make small changes

The worst boss I ever had encouraged us to make large patches. These changes were wide in scope, usually touching multiple parts of the code at once. From my experience, this was terrible advice.

Small, focused diffs have almost always served me better. They have several advantages:

They are usually easier to write, because there’s less to keep in your head.

They are usually easier to review. This lightens teammates’ cognitive load, makes my mistakes easier to spot, and usually means my code is merged sooner.

They are usually easier to revert if something goes wrong.

They reduce the risk of introducing new bugs since you’re changing less at once.

I also like to make smaller changes that build up to a larger one. For example, if I’m adding a screen that requires fixing a bug and upgrading a dependency, that could be three separate patches: one to fix the bug, one to upgrade the dependency, and one to add the screen.

Small changes usually help me build software more quickly and with higher quality.

Skills that have been useful

Most of the above is fairly high-level. Several more specific skills have come in handy, especially when trying to build software quickly:

Reading code is, by far, the most important skill I’ve acquired as a programmer. I’ve had to work on this a lot! It helps in so many ways: debugging is easier because I can see how some function works, bugs and poor documentation in third-party dependencies are less scary, it’s a huge source of learning, and so much more.

Data modeling is usually important to get right, even if it takes a little longer. Making invalid states unrepresentable can prevent whole classes of bugs. Getting a database schema wrong can cause all sorts of headaches later. I think it’s worth spending time to design your data models carefully, especially when they’re persisted or exchanged.

Scripting. Being able to comfortably write quick Bash or Python scripts has sped me up. I write a few scripts a week for various tasks, such as sorting Markdown lists, cleaning up some data, or finding duplicate files. I highly recommend Shellcheck for Bash as it catches many common mistakes. LLMs tend to be good at these scripts, especially if they don’t need to be robust.

Debuggers have saved me lots of time. There’s no substitute for a proper debugger. It makes it much easier to understand what’s going on (whether there’s a bug or not!), and quickly becomes faster than print() -based debugging.

Knowing when to take a break. If I’m stuck on a problem without making progress, I should probably take a break. This has happened to me many times: I struggle with a problem for hours, step away for a few minutes, come back, and solve it in 5 minutes.

Prefer pure functions and immutable data. The functional programming style eliminates many bugs and reduces mental overhead. It’s often easier than designing complex class hierarchies. Not always practical, but it’s my default choice.

LLMs, despite their issues, can accelerate some parts of the development process. It’s taken me awhile to understand their strengths and weaknesses, but I use them in my day-to-day programming. Lots of ink has been spilled on the topic of LLM-assisted software development and I don’t have much to add. I like the “vibecoding” tag on Lobsters, but there are lots of other places to read.

All of these are skills I’ve practiced a bunch, and I feel the investment has made me a faster developer.

Summary

Here’s a summary of things I’ve learned about building software quickly:

Know how good your code needs to be for the task at hand.

Start with a rough draft/spike.

Try to soften requirements if you can.

Don’t get distracted.

Make small changes.

Practice specific skills.

Everything in this list seems obvious in hindsight, but these are lessons that took me a long time to learn.

I’m curious to what you’ve discovered on this topic. Are there more tricks to know, or practices of mine you disagree with? Contact me any time. I’d love to learn from you!

Thanks to the anonymous reviewers who provided feedback on drafts of this post.

---

### The
 first version of Coinbase launched with just a hot wallet (3 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fthreadreaderapp.com%2Fthread%2F1942673835381383289.html%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/umN794uh0Ov17GyBeFeP5Wm_HfmmIS5J_7lF_j-mpQk=413
**TLDR Summary:** Coinbase's v2 key storage system, which has served the company well for years, was coded by two people in about eight weeks.
**Full Article Content:**
Bookmark Save as PDF

The first version of Coinbase launched with just a hot wallet - a risky proposition. We were in beta and the app prominently told people not to store any money there they couldn't afford to lose. But the amounts of deposits kept steadily rising.



I realized we needed to build build a cold storage system to improve security (otherwise a single hot wallet breach would mean we were insolvent and the company would die), and called the two cryptography/security experts I knew (@zooko and @octal if memory serves) and asked them what the best architecture would be. They were super helpful and gave me a crash course, since I had never built such a system before. I asked them how long it would take to build and I remember one of them said it might take a team of ~10 people 18 months to get it all up and running and tested.



The problem was we had about 8 weeks until the total deposits on the platform would exceed the total assets of the company, and only 2 engineers (including myself) to build it. We were seeing signs that hackers were already trying to break in, a true do or die moment.



@satoshilite and I buckled down and set about coding the new cold storage system from scratch, and integrating it into the app. We made some reasonable trade offs but what we came up with was fundamentally secure, and a massive improvement. We even unboxed some new laptops for key generation, stored backup material across several safe deposit boxes and locations. With about a week remaining, we started the process of transferring funds over to the new system. We were both extremely sleep deprived (how mistakes happen!), and paired up to double check each others work as we sent over the first test transaction, then a bigger one, and so on until it was fully transferred. We breathed a sigh of relief and went home to sleep for about 12 hours.



This was one of my proudest technical accomplishments from the early days of Coinbase: coding our v2 key storage system with 2 people in about 8 weeks, which should have taken 10 people 18 months. And it worked and served us well for years.



We're now on ~v5 of key storage, and have advanced way beyond what we came up with that day. But if we hadn't gotten it out in time, Coinbase very well may not exist today. It's a great testament to how constraints breed creativity, top talent matters in startups, and teams are often capable of more than they think when there is no other option.



Most products which succeed have early moments like this, where someone has to step up and make a play on the field that defies all the odds. As we face new challenges and deadlines across our many products, I always look out for who on the team is ready to step up and make the game winning play on the field.

• • •

---

### SVGs
 that feel like GIFs (1 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fkoaning.io%2Fposts%2Fsvg-gifs%2F%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/L_oARCYSoNHtujbvtmsYFM5-GfNCZTUvuR1N9bX4uWM=413
**TLDR Summary:** Animations are built into the SVG spec.
**Full Article Content:**
The moving image below is only 49Kb and has an incredibly high resolution.

It's similar to a GIF but instead of showing moving images, it shows moving SVGs! The best part: Github supports these in their README.md files!

Getting these to work involves asciinema and svg-term-cli. After uploading the asciinema you can use the tool to download a file that you can immediately click and drag into a README, or you can use this snippet to keep things local:

> asciinema rec test.cast <do stuff in the terminal then ctrl-d> > cat test.cast | svg-term --out=test.svg

It's something that I'm using extensively on bespoken.

How it works?

I was surpised to learn that moving SVGs were even a thing. But then I was reminded that animations are built into the svg spec.

<animate> - animates individual attributes over time

- animates individual attributes over time <animateTransform> - animates transformations like rotation, scaling, translation

- animates transformations like rotation, scaling, translation <animateMotion> - moves elements along a path

---

### Cloudflare:
 We Will Get Google To Provide A Way To Block AI Overviews (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.seroundtable.com%2Fcloudflare-block-google-ai-overviews-39718.html%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/uvaxHVxmMvnIzuN0zv9v6gn4UngdYg7_Sdsglv9iw6U=413
**TLDR Summary:** There currently isn't a clean way to block content from being used in Google's AI Overviews or AI Mode while being fully safe with ranking in the main Google search results.
**Full Article Content:**
A week or so ago, Cloudflare announced it would block AI bots by default and offer a new pay per crawl initiative to compensate you all for your content that AI just consumes for free. But as most SEOs know, Google AI Mode and AI Overviews can't be blocked without really blocking your site from Google Search.

But the CEO of Cloudflare, Matthew Prince, believes Google will give them a way to block AI Overviews and Answer boxes without being forced to block class search indexing.

He wrote on X, "Gemini is blocked by default. We will get Google to provide ways to block Answer Box and AI Overview, without blocking classic search indexing, as well."

Here is that post:

Gemini is blocked by default. We will get Google to provide ways to block Answer Box and AI Overview, without blocking classic search indexing, as well. — Matthew Prince 🌥 (@eastdakota) July 3, 2025

I mean, we've all been asking Google to give us this level of control. In which Google says, no, or you can use nosnippet controls but that will also impact your Google Search results in some ways. So there really isn't a clean way to block your content from being used in AI Overviews or AI Mode while being fully safe with ranking in the main Google search results.

I am not sure how Matthew Prince, the CEO of Cloudflare, is so confident he will get Google to give him a way to do this.

Do you think Cloudflare will be able to get Google to do this?

Forum discussion at X.

Update: More from Matthew Prince on how they will get Google to cooperate:

Worst case we’ll pass a law somewhere that requires them to break out their crawlers and then announce all routes to their crawlers from there. And that wouldn’t be hard. But I’m hopeful it won’t need to come to that. — Matthew Prince 🌥 (@eastdakota) July 7, 2025

---

### Waymo
 Begins Offering Teen Accounts, Starting in Metro Phoenix (2 minute read)
**URL:** https://tracking.tldrnewsletter.com/CL0/https:%2F%2Ffinance.yahoo.com%2Fnews%2Fwaymo-begins-offering-teen-accounts-170020443.html%3Futm_source=tldrnewsletter/1/01000197eeca22c3-fd1be8f0-a5ec-420a-8ca9-8a1900f6c629-000000/NdVV876kGliXT8m2MhLJ_CGoO_X5ciGx2zOZ56VDi40=413
**TLDR Summary:** Waymo's new teen accounts will let teenagers from 14 to 17 hail robotaxis and ride alone.
**Full Article Content:**
(Bloomberg) -- Alphabet Inc.’s Waymo is launching a new account type that lets teenagers hail a robotaxi and ride alone, expanding its rider base while continuing to test its service in more US cities.

Most Read from Bloomberg

Teens from 14 to 17 can have a user profile paired to a parent’s account starting on Tuesday, the company said in a statement. The program will initially be available where Waymo’s vehicles operate in the Metro Phoenix area. The company intends to expand teen service to other cities.

Waymo said it will have specially trained support agents available to assist teens during rides and will loop in parents during trips if needed. Parents can also track the real-time status of a trip if the teen rider opted to share it. That’s a different approach compared to Uber Technologies Inc., which allows parents to be automatically notified when teens hail a ride and check trip progress at any time.

The new program marks another expansion of Waymo’s ride-hailing service. The company’s more than 1,500 driverless vehicles now complete more than 250,000 paid passenger trips per week — up five-fold from a year ago. Waymo has announced plans to launch its robotaxi service in Miami and Washington next year, and is gathering data and conducting road tests in several markets, including New York City. The unit is part of Alphabet’s “other bets” division, a collection of futuristic businesses that generated $450 million in first-quarter revenue.

Adapting its service to a broader demographic would help Waymo better compete against Uber, which launched its teen offering in 2023 and has described it as a “runaway hit” with US users. Teen trips jumped more than 50% in the fourth quarter of last year from the prior period, Uber said in February, and are now available in 50 countries globally.

The two companies have teamed up in Austin and Atlanta where Waymo rides are offered exclusively through the Uber app. But teens with an Uber account won’t be eligible for the Waymo teen program in those two markets just yet. “We may consider enabling access for teens through our network partners in the future,” a Waymo spokesperson said.

The state of California, where Waymo currently operates paid rides through its own app in San Francisco and Los Angeles, does not currently allow unaccompanied minors in autonomous cars. The company “may seek to add” teen accounts in the state as “rules evolve,” a spokesperson said. Uber discontinued its teen rides program in the state after the California Public Utilities Commission in December began mandating that all drivers who transport unaccompanied minors be fingerprinted.

---

