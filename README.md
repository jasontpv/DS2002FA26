# DS2002 — Data Science Systems (Fall 2026)

**University of Virginia · School of Data Science**

This repository is the **official course record** for DS2002 in Fall 2026. It holds every lecture, studio, lab, project brief, rubric, and template for the semester.

- **Do all coding/analysis in Kaggle Notebooks or Google Colab.**
- **Version and organize your work here in GitHub.**
- **Submit links (GitHub repo + Kaggle/Colab) in Canvas.**

---

## How the week works

| Day | Notebook | What it is | Time |
|-----|----------|------------|------|
| **Monday** | `… — Lecture.ipynb` | Concept + live demo I walk through | ~45 min |
| **Wednesday** | `… — Studio.ipynb` | Guided build in class; ends with a breakout checkpoint for participation | ~45 min |
| **Friday** | `… — Lab.ipynb` | Hands-on lab you do on your own — **this is your graded weekly work** | Async |

Fridays are **not scheduled meetings**. The lab is released Friday and you complete it on your own time. Recommended target: submit by **Sunday 11:59pm ET** to stay on pace.

> There is **no separate homework** in this course. The Friday lab *is* the weekly graded assignment, and it is intentionally challenging.

---

## Repo structure

```
DS2002FA26/
├── README.md                     <- you are here
├── syllabus/                     <- Fall 2026 syllabus
├── templates/                    <- project README + submission checklist
├── rubrics/                      <- lab + project rubrics
├── data/sample/                  <- tiny sample data only
└── notebooks/
    ├── 01-foundations/           <- notebooks, Python, Git workflow
    ├── 02-sql-databases/         <- SQL + SQLite in notebooks
    ├── 03-pandas-cleaning/       <- Pandas + data cleaning
    ├── 04-json-apis/             <- JSON + consuming APIs
    ├── 05-etl-walmart/           <- ETL concepts + Walmart case framing
    ├── 06-midterm-walmart/       <- Midterm project (Walmart Hurricane Analytics)
    ├── 07-visualization/         <- Visualization for decisions
    ├── 08-capstone-acc/          <- Capstone (ACC Reality Check)
    └── 10-Reference/             <- Not tied to a class day; reopen as needed
```

---

## Notebook naming (follow exactly)

`YYYY-MM-DD — Topic — Type.ipynb`

**Type** is one of:

- `Lecture` — my Monday concept notebook
- `Studio` — my Wednesday guided build
- `Lab` — your Friday hands-on assignment
- `Template` — project scaffold

Example: `2026-09-18 — JSON to Tidy Tables — Lab.ipynb`

Answer keys are named the same with ` — ANSWER KEY` appended. They live in the private `instructor/` mirror and are **not** pushed to the student repo.

---

## What to submit

Unless Canvas says otherwise:

1. Your **GitHub repo link**
2. The `.ipynb` file(s) for the assignment in the correct folder
3. A short Markdown write-up **inside the notebook**

For projects, also submit a **project README** (see `templates/PROJECT_README_TEMPLATE.md`).

---

## Notebook hygiene (before every submission)

1. Restart the kernel
2. **Run All** top to bottom
3. Confirm no errors and that outputs (plots, tables, prints) are present
4. Add short Markdown notes between major steps

If a submitted notebook does not run, it is graded as-is.

---

## Environment

100% in the browser. No local installs required.

- **Kaggle Notebooks** (official environment) — <https://www.kaggle.com/>
- **Google Colab** (fully supported alternative) — <https://colab.research.google.com/>

Libraries used this term: `pandas`, `matplotlib`, `seaborn`, `sqlite3` (stdlib), `requests`. All are preinstalled on Kaggle and Colab.

---

*Last updated: July 2026.*
