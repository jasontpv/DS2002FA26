# Project Rubric (DS2002 Midterm & Capstone)

Applies to both the **Midterm (Walmart Hurricane Analytics)** and the **Capstone (ACC Reality Check)**. Each project brief also lists its own weighted rubric; this is the shared standard.

## Midterm — Walmart Hurricane Analytics (25% of grade)

| Component | Weight | What we're looking for |
|-----------|--------|------------------------|
| Data Cleaning | 25% | Thorough pipeline: dedup, SKU consolidation, timestamp/type fixes, missing values; clear code |
| Weather API Integration | 15% | Working API calls, parsing to DataFrame, timezone handling, meaningful join |
| Analytical Questions (1–5) | 30% | Correct methodology, sound reasoning, clear data-backed answers |
| Visualizations | 15% | ≥6 plots, right chart types, labeled, tells a story |
| Reflection Write-Up | 15% | Specific, thoughtful, shows understanding of ETL/pipeline trade-offs |

## Capstone — ACC Reality Check (30% of grade)

Graded once, from the submission due Friday, December 18, 2026, at 11:59pm ET, which includes a recorded team presentation. The studios and check-in notebooks from November 18 to December 4 are not graded. Full requirements are in `notebooks/08-capstone-acc/DS2002 Capstone — ACC Reality Check.pdf`.

| Component | Points | What we're looking for |
|-----------|--------|------------------------|
| Pipeline | 25 | Torvik CSV and ESPN JSON pulled and saved; name crosswalk with fixes shown; UTC to Eastern dates; one row per team per game; possessions estimated; decision log with row counts |
| SQLite and queries | 20 | Six tables with primary keys; a load that is safe to rerun; correct SQL for all six questions, including a cross-source join and a window function |
| The API | 20 | Live on PythonAnywhere; all five routes working; `?` placeholders in every query; sensible 404 and 400 responses |
| Charts | 15 | Four charts with titles that state the finding and labeled axes; chart 4 drawn from the team's own API |
| Presentation (recorded) | 10 | Video of eight minutes or less; every member speaks; each finding comes with its number |
| Reflection | 10 | Specific answers to the five reflection questions; every member contributes |

## Shared expectations

- **Do not fabricate data.** All external/API data must come from a real call shown in the notebook.
- **Show your work.** Messy input → cleaning steps → clean result, all visible.
- **Cite your API** (name + base URL).
- **Restart + Run All** before submitting.
- Every team member contributes to the reflection.
