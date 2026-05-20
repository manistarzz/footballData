# ⚽ Football Data Analysis
A collection of football data analysis projects covering Premier League performance, player statistics, and match visualisations — built using Python, Pandas, and Jupyter Notebooks.

## 📁 Repository Structure
~~~
footballData/
│
├── notebooks/
│   ├── ChelseaStats.ipynb         # Chelsea FC 22/23 season statistical breakdown
│   ├── passHeatMap.ipynb          # Pass heat map visualisation
│   ├── radarChart.ipynb           # Player radar chart comparison
│   ├── pieChart.ipynb             # Distribution charts for match data
│   ├── Lollipop.ipynb             # Lollipop chart visualisation
│   └── eplDescriptiveStats.ipynb  # EPL descriptive statistics overview
│
├── data/
│   ├── EPL.csv                    # Premier League match dataset
│   ├── Refs.csv                   # Referee data
│   ├── messiBetis.csv             # Messi vs Real Betis match data
│   └── plChampions.csv            # Premier League champions historical data
│
├── PremierLeagueStandings/        # Premier League standings analysis
│
└── reports/
    └── Chelsea_2223_Analysis.pdf  # Full written analysis: Chelsea's 22/23 decline
~~~

---

## 📊 Projects

### 1. 🎓 Formation Recognition System *(Final Year Thesis — Maynooth University 2026)*
An interactive analytical system that automatically detects football formations from positional data using StatsBomb 360 freeze-frame data. Built on one-dimensional Jenks Natural Breaks clustering and a competition-specific Expected Threat (xT) model trained on all Euro 2020 event data.

**Key features:**
- Automatic formation detection from freeze-frame snapshots
- Interactive draggable pitch — move players or the ball to simulate tactical adjustments
- Real-time xT and xG updates as positions change
- Cross-validated on Metrica Sports tracking data
- Match used: Italy vs Turkey, UEFA Euro 2020

**→ [View the thesis repo](https://github.com/manistarzz/Football-formation-analysis)**

---

### 2. Chelsea FC 22/23 Season Analysis
A comprehensive statistical and written analysis of Chelsea's historically poor 2022/23 Premier League season. Covers squad performance metrics, goal contributions, defensive breakdowns, and contextual factors behind the decline.

- **Notebook:** `ChelseaStats.ipynb`
- **Report:** `Chelsea_2223_Analysis.pdf`

---

### 3. Premier League Standings
Analysis and visualisation of EPL standings data across seasons.

- **Folder:** `PremierLeagueStandings/`

---

### 4. Player & Match Visualisations
A set of focused notebooks producing different chart types used in football analytics:

| Notebook | Visualisation Type |
|---|---|
| `passHeatMap.ipynb` | Pass heat maps |
| `radarChart.ipynb` | Player attribute radar charts |
| `pieChart.ipynb` | Percentage distribution charts |
| `Lollipop.ipynb` | Lollipop ranking charts |
| `eplDescriptiveStats.ipynb` | Descriptive statistical summaries |

---

## 🛠 Tools & Libraries

- Python 3
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook
- mplsoccer *(for football-specific visualisations)*

---

## 🔗 About

This repository reflects my interest in applying data analysis and visualisation to football — exploring how data can tell clearer stories about player performance, team dynamics, and match outcomes.

The thesis project — a formation recognition system using StatsBomb 360 data — represents the most advanced work here, combining clustering algorithms, Expected Threat modelling, and interactive visualisation into a single system.

Part of a broader interest in sports data infrastructure and what it takes to make performance insights genuinely accessible to clubs and analysts.
