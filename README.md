# Campus E-Rickshaw Mobility - A TQM Intervention

Group 2. TQM Course Project. IIT Roorkee. April 2026.

A 150-respondent student survey, nine TQM artefacts, a working React prototype, and a 24-slide deck applied to the four pain points of campus E-rickshaw service: forced-fill wait, route mismatch, cash-payment leakage, and empty return trips.

## Repository layout

```
.
+- app/                 Vite + React prototype (student, driver, admin views)
+- docs/                Final_Problem_and_Solution, Course_Content_Mapping, Complete_Project_Report (PDF + md)
+- survey/              Questionnaire, seeded synthetic data generator, 150-row CSV, analysis notebook, charts, report
+- analysis/            9 TQM artefacts (Ishikawa, 5 Whys, Pareto, SIPOC, Flowchart, FMEA, PDCA, Affinity, Relations) each with diagram.png + writeup.md
+- presentation/        TQM_Project_Final.pptx (24 slides, 7 MB) + build_deck.py
+- ideas/               Original problem brief
+- slides/              Course reference PDFs (10 chapters of TQM material)
+- README.md            You are here.
```

## Quickstart (run the app locally)

Prerequisites: Node 20+, npm 10+.

```bash
cd app
npm install
npm run dev
# open http://localhost:5173
```

The dev server supports HMR. Three views are selectable from the top-right role switcher: Student (default), Driver, Admin.

## Deploying to Vercel

The `app/` folder is a standard Vite + React project. To deploy:

1. Sign in at https://vercel.com using your GitHub account.
2. Click **Add New -> Project**.
3. Import this repository (`PrathamSingla15/QM_project`).
4. Configure the project:
   - **Framework Preset**: Vite
   - **Root Directory**: `app` (important - this repo has multiple subdirectories)
   - **Build Command**: `npm run build` (default)
   - **Output Directory**: `dist` (default)
   - **Install Command**: `npm install` (default)
5. No environment variables are required.
6. Click **Deploy**. First build takes about 60 seconds.
7. Your production URL will look like `qm-project-<hash>.vercel.app`.
8. Every push to `main` triggers a new production deployment automatically.

Rollbacks are available via the Deployments tab. Optionally add a custom domain under Project Settings -> Domains.

### Expected build output

```
dist/index.html                  0.9 kB gzip: 0.5 kB
dist/assets/index-*.css         19.4 kB gzip: 4.3 kB
dist/assets/index-*.js         178.5 kB gzip: 55.7 kB
```

Total production bundle under 250 KB gzipped. No external API calls at runtime.

## Reproducing the analysis

The survey is 150 seeded synthetic respondents (seed `20260421`). To regenerate from scratch:

```bash
# from repo root
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib seaborn python-pptx python-docx nbformat jupyter

# regenerate the survey CSV
python survey/generate_responses.py

# regenerate the 9 TQM diagrams
python analysis/build_all_diagrams.py
python analysis/build_conceptual_diagrams.py
python analysis/build_process_diagrams.py

# regenerate the 5 survey charts
python survey/build_charts.py

# regenerate the deck
python presentation/build_deck.py

# regenerate the docx reports
pandoc docs/Final_Problem_and_Solution.md -o docs/Final_Problem_and_Solution.docx --toc
pandoc docs/Course_Content_Mapping.md -o docs/Course_Content_Mapping.docx --toc
pandoc survey/Survey_Analysis_Report.md -o survey/Survey_Analysis_Report.docx --toc --resource-path=survey
```

## Key numbers

- n = 150 (synthetic, seeded, realistic correlated distributions)
- Mean wait: 8.2 min; median 7; 90th percentile 13
- Top-3 pain points account for 56.8% of mentions
- r(payment issues, wallet comfort) = 0.40
- r(satisfaction, app willingness) = -0.27
- Fee acceptance (Likert >= 3): 80%
- Drop-off locations: 43 across 4 groups (14 hostels, 16 departments, 4 gates, 9 facilities)
- FMEA top-3 RPN: Driver-offline 126, Cancellation-dispute 120, Wallet-insufficient 100

## Credits

- Group 2 - TQM Course Project, IIT Roorkee, April 2026
- Tools: Vite, React, python-pptx, python-docx, pandoc, xelatex, Playwright (for screenshots)
- Synthetic data generator: seed 20260421 for reproducibility
