# DS2002 — Data Science Systems

## Syllabus: Fall 2026

**University of Virginia · School of Data Science**

---

## Course Information

- **Course Start–End:** August 25 – December 8, 2026
- **Credit Hours:** 3
- **Catalog Description:** This course will center on exposing students to contemporary pipelines for data analysis through a series of steadily escalating use cases. The course will begin with simple local database construction such as SQLite and evolve to cloud-based systems such as AWS or Google Cloud. This progression will include topics such as data lakes and other non-SQL applications as appropriate.
- **Location:** Ridley Hall G006
- **Sections:** Two Monday/Wednesday sections
  - **9:00 a.m.** — TA: Zoe Hendershot (`njd5rd@virginia.edu`)
  - **10:00 a.m.** — TA: Shreyans Jain (`yex8wb@virginia.edu`)
- **Friday Labs:** Assigned every Friday and completed on your own schedule. Fridays are **not** scheduled class meetings.
- **Environment:** 100% in the browser — **Kaggle** or **Google Colab**. Work is versioned in **GitHub** and submitted via **Canvas**.

## Instructor Information

**Jason Williamson**, Data Science Professor of Practice
- Email: jasonw@virginia.edu
- Office Hours: Scheduled during class time as we build in time for projects, or by request.
- Zoom: <https://virginia.zoom.us/j/5636132721?pwd=NzljVTBlcVlZM0ZkYXFCdTJReUFEQT09>
- Discord: **DS2002F26** — <https://discord.gg/zTr98dm6x>. This is where course questions get answered. Official notices come through Canvas Announcements.

**Teaching Assistants**

| Section | TA | Email |
|---------|----|-------|
| 9:00 a.m. | Zoe Hendershot | njd5rd@virginia.edu |
| 10:00 a.m. | Shreyans Jain | yex8wb@virginia.edu |

---

## Course Overview

By definition, "data science" must make meaning out of ever-growing pools of data. But the researcher quickly discovers that the hand examination of any data, while useful for granular analysis, is never adequate for large samples. To produce data science at scale, researchers must make effective use of workflows, pipelines, and processes to ingest, parse, and transform data with tools and automation.

This course centers on exposing students to contemporary pipelines for data analysis through a series of steadily escalating use cases. We begin with simple local database construction such as SQLite and evolve toward cloud-based systems such as AWS or Google Cloud. That progression includes data lakes and other non-SQL applications as appropriate. Along the way we learn systems for data collection, transformation, and consumption. We work with data wrangling, cleansing, ETL, APIs, and communication of results.

Everything is delivered in **notebooks** (Kaggle/Colab) so that running, grading, and submitting via Git is fast and consistent.

## Learning Outcomes

By the end of the semester, you will be able to:

1. Design and implement data pipelines that ingest, clean, and transform messy multi-source data.
2. Apply best practices in data wrangling, cleansing, and ETL using contemporary tools and automation.
3. Query and combine data using SQL (SQLite), Pandas, JSON, and public APIs.
4. Use version control with Git/GitHub and a notebook-first workflow to support collaborative, reproducible analysis.
5. Communicate findings with clear visualizations and plain-language recommendations.

---

## How the Week Works

| Day | What happens | Notebook | Time |
|-----|--------------|----------|------|
| **Monday** | Lecture: concept + live demo | `… — Lecture.ipynb` | ~45 min |
| **Wednesday** | Studio: guided build + breakout checkpoint | `… — Studio.ipynb` | ~45 min |
| **Friday** | Hands-on lab — your graded weekly work (async, do it on your own time) | `… — Lab.ipynb` | Async |

> **No separate homework.** Your Friday lab is the weekly graded assignment. Plan on it taking real time.

---

## Required Software

We are **100% in notebooks** — Kaggle or Google Colab. Nothing to install locally. All libraries we use (`pandas`, `matplotlib`, `seaborn`, `sqlite3`, `requests`) are preinstalled on both platforms.

Two free accounts are required, and both take about two minutes:

- **GitHub** — <https://github.com>. Your work is versioned here, and the course notebooks live here. Needed before Lab 01.
- **Discord** — <https://discord.com>. Then accept the invite to the **DS2002F26** server: <https://discord.gg/zTr98dm6x>. This is how you get help during the week.

Set both up in the first week. If you already have accounts, use them — there is no need to make new ones for this course.

## Learning Resources

Readings are largely online articles linked in the weekly notebooks and Canvas. No textbook to purchase. From time to time, I will do readings for you in class — so pay attention to what we cover each week.

---

## Semester Schedule — Fall 2026

Refer to the Canvas calendar for exact due dates. All changes to due dates are reflected in Canvas.

### Fall 2026 — Important UVA Dates

- **Courses begin:** Tuesday, August 25, 2026
- **Labor Day (classes held):** Monday, September 7, 2026
- **Fall Reading Days (no classes):** Saturday, October 3 – Tuesday, October 6, 2026
- **Election Day (no classes):** Tuesday, November 3, 2026
- **Thanksgiving Recess:** Wednesday, November 25 – Sunday, November 29, 2026
- **Courses end:** Tuesday, December 8, 2026
- **Last class meeting:** Monday, December 7, 2026 (wrap-up lecture)
- **Final Exams:** December 10–18, 2026 — *this course has no sit-down final. The capstone, including a recorded team presentation, is due Friday, December 18 at 11:59pm ET in its place.*

### Weekly Schedule

**This schedule will change.** Treat the table below as a working plan, not a fixed contract — check Canvas and the weekly notebooks for the latest topics and due dates.

Friday labs are released each Friday and completed asynchronously. Recommended: submit by **Sunday 11:59pm ET**.

| Week | Dates | Monday — Lecture | Wednesday — Studio | Friday — Lab (graded) |
|------|-------|------------------|--------------------|-----------------------|
| 1 | Aug 26–28 | *(No Mon — term starts Tue)* Data Science Systems Overview (Wed) | *(no second meeting this week)* | Lab 01: Environment + GitHub Setup |
| 2 | Aug 31–Sep 4 | Git for Data Science | Kaggle/Colab Workflow + Notebook Hygiene | Lab 02: Submission Drill + Fix a Broken Notebook |
| 3 | Sep 7–11 | SQL Fundamentals in Notebooks | SQLite Joins + Grouping | Lab 03: SQL Challenge Set |
| 4 | Sep 14–18 | SQL → Python → DataFrames | Pandas Core Ops (filter, groupby, join) | Lab 04: Pandas Challenge |
| 5 | Sep 21–25 | Data Cleaning (types, missing, duplicates) | Cleaning Clinic on Messy CSV | Lab 05: Cleaning Gauntlet |
| 6 | Sep 28–Oct 2 | JSON & Nested Records | JSON → Tidy Tables | Lab 06: Normalize + Join Nested JSON |
| 7 | Oct 5–9 | *(No Mon — Reading Day)* | APIs 101 + Ingestion with Retries (Wed) | Lab 07: Public API → Clean Table |
| 8 | Oct 12–16 | ETL Concepts + **Walmart Case** Framing | Mini-ETL on Walmart Sample | Lab 08: Walmart Warm-Up (SKU Mess) |
| 9 | Oct 19–23 | **Midterm Kickoff** + Team Formation | Weather API Join Studio | Midterm Checkpoint (Lab 09) |
| 10 | Oct 26–30 | Midterm Clinic: Cleaning & Joins | Midterm Clinic: Analysis & Charts | Midterm Progress (Lab 10) |
| 11 | Nov 2–6 | Midterm Presentations / Peer Feedback | Reflection: What Broke, What Mattered | **Midterm Due** |
| 12 | Nov 9–13 | Visualization for Decisions (not Dashboards) | Critique + Redesign Studio | Lab 11: Visualization Challenge |
| 13 | Nov 16–20 | *(Mon Nov 16 met under the earlier capstone plan)* | **Capstone Kickoff + First Pulls** (capstone launches Wed Nov 18) | Check-in: Proposal + Pipeline Setup *(not graded)* |
| 14 | Nov 23 | *No class.* Team check-in notebook | *Thanksgiving Recess* | *No lab* |
| 15 | Nov 30–Dec 4 | Analysis Clinic: SQL in SQLite | Building and Publishing Your API | Check-in: Capstone Progress Check *(not graded)* |
| 16 | Dec 7 | Wrap-Up Lecture (last class meeting) | *(Term ends Tue Dec 8)* | *No lab* |
| Finals | Dec 18 | | | **Capstone Due, Fri Dec 18, 11:59pm ET** (notebook, database, API, recorded presentation) |

*Capstone presentations are recorded by each team and submitted with the project on Dec 18; there are no in-class capstone presentations.*

---

## Grading

### Grade Breakdown

| Component | Percentage | Notes |
|-----------|-----------|-------|
| **Weekly Labs** | **40%** | Released each Friday; you complete them on your own. Eleven over the semester (Labs 01–11); the capstone weeks have ungraded check-ins instead. These are your main weekly practice — budget time accordingly. |
| **Midterm Project** (Walmart Hurricane Analytics) | **25%** | Group project (2–4), ~3 weeks. |
| **Capstone Project** (ACC Reality Check) | **30%** | Group project (3–4), launches Nov 18. One graded submission, due Fri Dec 18 at 11:59pm ET, including a recorded eight-minute team presentation. |
| **Class Participation** | **5%** | Studio breakout checkpoints submitted individually in Canvas. See below. |

### Class Participation (5%)

With ~53 students per section, participation is **not** graded on speaking in front of the room.

Each **Wednesday studio** ends with a short **breakout checkpoint**:
1. Work in **groups of 4–5** if you wish — grouping up is optional, and it does not have to wait for the end of class.
2. Complete the checkpoint cell at the bottom of that week's **Studio** notebook on your own.
3. Submit **individually** in Canvas (**Studio Checkpoint — Week X**) by **Thursday 11:59pm ET**.

**What to submit:** paste the printed output from the checkpoint cell, or upload a screenshot. One or two sentences is enough — e.g. what worked, what broke, or what your group tried.

**How it's graded:** mostly **completion**. Submit something plausibly tied to that day's studio and you get credit for that week. TAs spot-check; you are not graded on being loud or extroverted.

**Over the term:** **11** checkpoint opportunities, in weeks 2 through 12. Submit **10** for full participation credit. The capstone studios on Nov 18 and Dec 2 do not have checkpoints, and weeks with no studio meeting (e.g. Thanksgiving) do not count.

Collaborate in the room; **submit on your own.**

### Grading Scale

| Grade | Range |
|-------|-------|
| A | 93–100 |
| A− | 90–92 |
| B+ | 87–89 |
| B | 83–86 |
| B− | 80–82 |
| C+ | 77–79 |
| C | 73–76 |
| C− | 70–72 |
| D+ | 67–69 |
| D | 63–66 |
| D− | 60–62 |
| F | below 60 |

---

## Grading Policies

### Expectations

All labs and projects are due on time, by the due date/time indicated in Canvas. Submitting on time ensures you learn prerequisite skills and are prepared for the next set.

### Late Work — Two Automatic Extensions

You get **two automatic 7-day extensions** during the term, no questions asked, for **labs only** (not projects or participation checkpoints). Falling behind compounds — if you do fall behind, complete the earlier work first. All work must be completed by the end of the semester regardless of extensions; work submitted after the last day of the semester is not counted toward the final grade.

### Extenuating Circumstances

If you are struggling to catch up or extenuating circumstances arise, reach out early — the sooner you do, the more options we have. You may also contact your primary academic advisor or Advising Dean.

### Class Attendance

Come to class if you can. If you can't, let me know — I'm flexible and understand that life happens (sick days, interviews, etc.).

---

## Course Policies

### Communication and Response Time

Three channels, and it matters which one you use.

| What | Where | Why |
|------|-------|-----|
| Official notices — due dates, schedule changes, logistics | **Canvas Announcements** | This is the course record. You are responsible for reading it. |
| Course questions — "why does my push fail," "is my join wrong" | **Discord** | Fastest answer, and the next person with your problem can find it. |
| Anything personal — grades, accommodations, extensions, health | **Email** (<jasonw@virginia.edu>) | Private, and it creates a record we can both refer to. |

Ask course questions in Discord rather than by email. You will usually get an answer sooner, and the answer helps whoever hits the same wall next week. Anything with personal information in it belongs in email, not a public channel.

The sooner you tell me about something affecting your attendance or performance, the better our chance of solving it together.

### Discord — DS2002F26

Join here: <https://discord.gg/zTr98dm6x>. You need a free Discord account first (<https://discord.com>); if you already have one, use it.

**Set your server nickname to your real name and section** — for example `Jane Doe (001)`. With over a hundred students across two sections, a handle nobody can match to the roster means I cannot help you, credit you, or tell which section you are in.

Where to post:

- **Questions forum** — one thread per question. Search it before you post; there is a good chance your question is already answered.
- **Section channels** — logistics for your own section.
- **Not DMs.** Ask in the forum, not privately. It is not that I mind — it is that a DM answer helps exactly one person, and I would rather answer once where everyone can read it. Personal matters go to email.

**One firm rule about code.** The course policy below applies in Discord exactly as it does anywhere else: explaining an individual line, describing your approach, or debugging alongside someone is collaboration and is welcome. Posting a working solution to a lab — as text or a screenshot — is not, and it is an honor violation for both of you. Post the error, the line that confuses you, and what you already tried.

Discord is a convenience, not the record. If it disappeared tomorrow, everything you are graded on still lives in Canvas and GitHub.

### Academic Integrity: Collaboration and Cheating

Cheating tends to happen at higher rates in introductory programming-based courses when students get frustrated, feel there is only one "correct" way to write code, and because it is easy to copy and paste. The difference between collaboration and cheating comes down to intent: cheating circumvents the learning process; collaboration helps you and your classmates learn more deeply.

**Examples of cheating:**
- Copying someone else's text word-for-word, or copying text from an AI tool and passing it off as your own
- Sharing/showing code to circumvent learning (e.g., letting someone copy because of a deadline)
- Asking for help without trying first; asking someone to do the work for you
- Making your homework freely available on GitHub or elsewhere
- Sharing answers to quizzes

**Examples of what's okay:**
- Two people with the same code, as long as it wasn't copy-pasted from one another
- Sharing/showing individual lines of code to teach or explain
- Debugging together (only possible once both have written their own code)
- Sharing strategies, articles, blogs, and other resources

If you are stressed about the intensity of the course, message me and we will get you back on track.

### SDS Guidelines on AI Tools and Assistance

Generative AI tools (ChatGPT, Copilot, Gemini, Claude, image models, etc.) are **permitted at no penalty** for:
- Brainstorming and refining ideas
- Fine-tuning research questions
- Finding information on your topic
- Drafting an outline to organize your thoughts
- Checking grammar and style

**You are responsible for:**
- Acknowledging that LLMs produce incorrect facts and fake citations
- Acknowledging that code-generation models may produce inaccurate outputs
- Taking responsibility for any inaccurate, biased, or unethical content you submit, regardless of origin
- Properly citing the contribution of any AI tool in submitted material
- The entirety of anything you submit based on an AI query

**AI tools are NOT permitted for:**
- Impersonating students in classroom contexts (e.g., composing discussion posts or Zoom chat as if it were you)
- Completing group work assigned to you, unless the group agrees
- Writing a draft of a writing assignment
- Writing entire sentences, paragraphs, or papers to complete assignments

Improper or uncited use may result in a failing grade on the assignment and may be an honor violation depending on context. Used well and cited, foundation models can help you submit higher-quality work in less time — so their use is encouraged within these guidelines.

---

## School of Data Science Support and Policies

### Python Support Hours

Need a Python refresher or help troubleshooting? Stop by Python support hours. Content is posted on the Python Support Hours GitHub.

### Declaring the Data Science Minor

The Minor in Data Science is open to students from all backgrounds, majors, and schools. There is no application or prerequisites and entry is not competitive. Requirements and the declaration form are on the SDS website.

### Student Success Advisor

Questions about minor requirements, progress, and course enrollment go to the Student Success Advisor at sdsminor@virginia.edu.

### UVA Career Center

The UVA Career Center supports students exploring careers, finding internships/jobs, and evaluating graduate programs. Schedule via Handshake or visit drop-in hours in Clemons Library.

### Undergraduate / Graduate Record

Visit the University Record for policies on academic regulations, standing, financial assistance, and grades.

---

## University Policies

### University Email Policy

Students are expected to activate and regularly check their official UVA email, as some communications are time-sensitive. Students who fail to check email are responsible for resulting consequences.

### Academic Integrity and the UVA Honor System

The School of Data Science relies upon and cherishes its community of trust. We endorse and uphold the University's Honor principle that students will not lie, cheat, or steal, nor tolerate those who do. Students are expected to be familiar with the University honor code, including the section on academic fraud.

All work should be pledged in the spirit of the Honor System. The instructor indicates which assignments are individual and which permit collaboration. By submitting work electronically, students acknowledge the Honor Pledge:

> "On my honor, I have neither given nor received aid on this examination, nor did I have prior knowledge of its contents."

More information: <http://www.virginia.edu/honor/>.

### Course Evaluations

Student feedback is critical. Students are expected to complete anonymous, confidential course evaluations in a timely manner at the end of the term.

### Discrimination / Harassment / Retaliation

UVA prohibits discrimination and harassment based on age, color, disability, family medical or genetic information, gender identity or expression, marital status, military status, national or ethnic origin, political affiliation, pregnancy, race, religion, sex, sexual orientation, and veteran status. UVA policy also prohibits retaliation. All faculty and TAs are responsible employees for disclosures or reports of potential discrimination, harassment, and retaliation.

### Disability and Pregnancy Accommodations

If you anticipate or experience barriers to learning, please discuss your concerns with me. If you have or think you may have a disability, contact the Student Disability Access Center (SDAC) to request reasonable accommodations. If you have SDAC accommodations, send me your Faculty Notification Letter as soon as possible so we can build an implementation plan. Students may also be entitled to reasonable accommodations for pregnancy, childbirth, or related medical issues; contact SDAC or EOCR.

### Religious Academic Accommodations

UVA provides reasonable accommodations when a student's sincerely held religious beliefs or observances conflict with academic requirements. Submit requests to me by email as far in advance as possible. Questions may go to EOCR at UVAEOCR@virginia.edu or (434) 924-3200.

### Reporting an Incident

Just Report It (JRI) is the University's online system for reporting sexual and gender-based harassment and violence; discrimination, harassment, and retaliation; hazing; Clery Act matters; interference with speech rights; youth protection; and threats or acts of violence. Confidential Resources are available if you wish to discuss a concern without reporting to the University.

### Student Mental Health and Wellbeing

UVA is committed to advancing student mental health and wellbeing. If you or someone you know is feeling overwhelmed, depressed, or in need of support, contact the CAPS Care Managers at CAPSCareMgrs@virginia.edu. Care and Support Services (CASS) is a non-clinical resource with a 24/7 line for urgent non-clinical needs:
- Monday–Friday, 8 a.m.–5 p.m.: (434) 924-7133
- After hours: University Police Department (434) 924-7166, ask for CASS on Call

---

## Technical Support

- **Login/Password:** <https://in.virginia.edu/helpdesk>
- **Canvas:** Check the Help tab for resources
- **Kaggle/Colab:** In-app help; ask in Discord first so others benefit

---

*Last updated: August 2026.*
