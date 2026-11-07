"""
Campus Football League Table Manager
Case Study 17

A menu-driven league manager that registers teams, records match results,
calculates league points and goal difference, sorts the table, displays team
results and identifies the strongest attack and best defence.

Points: win = 3, draw = 1, loss = 0.
Tie-break order: points, goal difference, goals scored.
Data is stored in data/league_data.json.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "league_data.json"


def create_team(name):
    """Create a team's league statistics."""
    return {
        "name": name,
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0,
        "results": []
    }


def register_team(teams, name):
    """Register a team unless its name is blank or already in use."""
    name = name.strip()
    if not name:
        raise ValueError("Team name cannot be blank.")
    if name.casefold() in (team["name"].casefold() for team in teams):
        raise ValueError(f"{name} is already registered.")
    teams.append(create_team(name))


def update_team(team, goals_for, goals_against, opponent):
    """Update one team's statistics after a match."""
    team["played"] += 1
    team["goals_for"] += goals_for
    team["goals_against"] += goals_against

    if goals_for > goals_against:
        team["won"] += 1
        team["points"] += 3
        result = "W"
    elif goals_for == goals_against:
        team["drawn"] += 1
        team["points"] += 1
        result = "D"
    else:
        team["lost"] += 1
        result = "L"

    team["results"].append({
        "opponent": opponent,
        "score": f"{goals_for}-{goals_against}",
        "result": result
    })


def record_match(teams, home_name, away_name, home_goals, away_goals):
    """Validate and record a match, updating both teams."""
    if home_name.casefold() == away_name.casefold():
        raise ValueError("A team cannot play against itself.")
    if not isinstance(home_goals, int) or not isinstance(away_goals, int):
        raise ValueError("Goals must be whole numbers.")
    if home_goals < 0 or away_goals < 0:
        raise ValueError("Goals cannot be negative.")

    lookup = {team["name"].casefold(): team for team in teams}
    if home_name.casefold() not in lookup or away_name.casefold() not in lookup:
        raise ValueError("Both teams must be registered before a match.")

    home = lookup[home_name.casefold()]
    away = lookup[away_name.casefold()]
    update_team(home, home_goals, away_goals, away["name"])
    update_team(away, away_goals, home_goals, home["name"])


def goal_difference(team):
    """Return goals scored minus goals conceded."""
    return team["goals_for"] - team["goals_against"]


def sorted_table(teams):
    """Sort by points, goal difference, then goals scored (descending)."""
    return sorted(
        teams,
        key=lambda team: (
            team["points"],
            goal_difference(team),
            team["goals_for"]
        ),
        reverse=True
    )


def display_table(teams):
    """Print the current league table."""
    print("\nPOS TEAM                 P  W  D  L  GF GA GD PTS")
    print("-" * 55)
    for position, team in enumerate(sorted_table(teams), start=1):
        print(
            f"{position:<3} {team['name'][:20]:<20} "
            f"{team['played']:>2} {team['won']:>2} {team['drawn']:>2} "
            f"{team['lost']:>2} {team['goals_for']:>3} "
            f"{team['goals_against']:>2} {goal_difference(team):>3} "
            f"{team['points']:>3}"
        )


def show_team_results(teams, name):
    """Display every recorded result for a selected team."""
    team = next((t for t in teams if t["name"].casefold() == name.casefold()), None)
    if team is None:
        print("Team not found.")
        return
    print(f"\nResults for {team['name']}:")
    if not team["results"]:
        print("No matches recorded yet.")
    for item in team["results"]:
        print(f"{item['result']} vs {item['opponent']} ({item['score']})")


def show_highlights(teams):
    """Show the most prolific attack and strongest defence."""
    if not teams:
        print("Register teams to see league highlights.")
        return
    best_attack = max(teams, key=lambda team: team["goals_for"])
    best_defence = min(teams, key=lambda team: team["goals_against"])
    print(f"Most goals scored: {best_attack['name']} ({best_attack['goals_for']})")
    print(
        f"Best defence (fewest goals conceded): "
        f"{best_defence['name']} ({best_defence['goals_against']})"
    )


def save_data(teams, filename=DATA_FILE):
    """Save league data as JSON."""
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    with filename.open("w", encoding="utf-8") as file:
        json.dump(teams, file, indent=4)


def load_data(filename=DATA_FILE):
    """Load saved league data, or return an empty list if no file exists."""
    filename = Path(filename)
    if not filename.exists():
        return []
    with filename.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_non_negative_int(prompt):
    """Read a valid non-negative integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter zero or a positive whole number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def run_menu():
    """Run the interactive application."""
    teams = load_data()
    while True:
        print("\n=== CAMPUS FOOTBALL LEAGUE MANAGER ===")
        print("1. Register team")
        print("2. Record match result")
        print("3. Display league table")
        print("4. Show a team's results")
        print("5. Show league highlights")
        print("6. Save data")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                register_team(teams, input("Team name: "))
                print("Team registered.")
            elif choice == "2":
                home = input("Home team: ").strip()
                away = input("Away team: ").strip()
                hg = get_non_negative_int("Home goals: ")
                ag = get_non_negative_int("Away goals: ")
                record_match(teams, home, away, hg, ag)
                print("Match recorded.")
            elif choice == "3":
                display_table(teams)
            elif choice == "4":
                show_team_results(teams, input("Team name: ").strip())
            elif choice == "5":
                show_highlights(teams)
            elif choice == "6":
                save_data(teams)
                print(f"Data saved to {DATA_FILE}.")
            elif choice == "7":
                save_data(teams)
                print("Data saved. Goodbye.")
                break
            else:
                print("Invalid choice. Select 1 to 7.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    run_menu()
