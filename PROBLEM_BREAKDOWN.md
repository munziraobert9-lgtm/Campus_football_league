# Problem Breakdown — Case 17: Campus Football League Table Manager

| Question | Group's answer |
|---|---|
| Case study title and group number | Case 17: Campus Football League Table Manager. Group number: [insert your class group number]. |
| The problem in our own words (2 sentences) | The campus needs a reliable way to keep football league records for inter-faculty matches. The program will record scores, calculate points and goal difference, rank teams fairly, display results and preserve the records between sessions. |
| Who will use the program and what do they need? | League administrators, sports coordinators and team representatives. They need to register teams, enter match scores, view an accurate table and check previous results. |
| Inputs (what goes in) | Team names; home team; away team; home goals; away goals. Goals must be whole numbers equal to or greater than zero. |
| Outputs (what comes out) | Updated league table; points, played, wins, draws, losses, goals for, goals against and goal difference; each team's match results; team with most goals scored; team with fewest goals conceded; saved JSON data. |
| Things/data we must store and how | A list of dictionaries, one dictionary per team. Each team dictionary stores its name, match statistics, points and a list of result dictionaries. JSON is used for permanent storage. |
| Functions or classes we need (name and one-line job) | `create_team()` creates a team's record; `register_team()` validates and adds a team; `record_match()` validates a score and updates both teams; `update_team()` updates one team's statistics; `goal_difference()` calculates GF − GA; `sorted_table()` ranks teams using `sorted()` and a lambda key; `display_table()` prints the standings; `show_team_results()` lists a team's results; `show_highlights()` reports most goals and best defence; `save_data()` writes JSON; `load_data()` reads JSON; `run_menu()` handles user choices. |
| What can go wrong and how we will handle it | Blank or duplicate team names are rejected; unregistered teams and a team playing itself are rejected; negative, non-numeric or decimal goals are rejected; invalid menu choices are handled with a message; missing save file starts a new league; file access or invalid JSON errors can be reported and corrected if encountered. |
| Files we will read or write | Read/write `data/league_data.json`; source file `main.py`; automated tests in `tests/test_league.py`. |
| How we will test it (3 test examples with expected answers) | 1) Engineering beats Business 2–0: Engineering gets 3 points, Business gets 0, GD becomes +2 and −2. 2) Science draws with Engineering 1–1: each receives 1 point and both have one draw. 3) A negative score such as −1–0 is rejected and no statistics change. Additional automated tests cover saving/loading and ranking. |
| Who is responsible for which part? | See `TASK_ALLOCATION.md`. Each member should review and understand the final integrated program. |
