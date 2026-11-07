# Campus Football League Table Manager

**Case Study 17** — Python group project

## Overview
A menu-driven Python program for managing an inter-faculty football league. It registers teams, records scores, awards league points, calculates goal difference, sorts the league table, displays team match results, identifies the most prolific attack and best defence, and saves data to a JSON file.

## Requirements
- Python 3.9 or later
- No third-party packages are required to run the program.

## Run the program
From this folder, run:

```bash
python main.py
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## League rules
- Win: 3 points
- Draw: 1 point
- Loss: 0 points
- Ranking order: points (highest first), goal difference (highest first), then goals scored (highest first).
- Goal difference = goals for − goals against.

## Files
- `main.py` — application source code.
- `tests/test_league.py` — automated tests.
- `data/league_data.json` — created automatically when the application saves data.
- `PROBLEM_BREAKDOWN.md` — completed analysis table.
- `TASK_ALLOCATION.md` — proposed division of group responsibilities.
- `PROJECT_REPORT.docx` — cover page and project documentation.

## Data storage
The application stores team statistics and match results in `data/league_data.json`. The file is created automatically when data is saved or the application exits.

## Important note about "top scorer"
The case study can be satisfied by reporting the team with the most goals scored and the team with the fewest goals conceded. Individual player top-scorer statistics would require collecting player names and goalscorer details, which are not included in the stated match-result inputs.
