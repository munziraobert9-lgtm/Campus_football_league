import tempfile
import unittest
from pathlib import Path

from main import register_team, record_match, sorted_table, goal_difference, save_data, load_data


class LeagueManagerTests(unittest.TestCase):
    def setUp(self):
        self.teams = []
        register_team(self.teams, "Engineering")
        register_team(self.teams, "Business")
        register_team(self.teams, "Science")

    def test_win_awards_three_points(self):
        record_match(self.teams, "Engineering", "Business", 2, 0)
        engineering = self.teams[0]
        self.assertEqual(engineering["points"], 3)
        self.assertEqual(engineering["won"], 1)

    def test_draw_awards_one_point_each(self):
        record_match(self.teams, "Engineering", "Science", 1, 1)
        self.assertEqual(self.teams[0]["points"], 1)
        self.assertEqual(self.teams[2]["points"], 1)

    def test_table_uses_goal_difference_as_tie_break(self):
        record_match(self.teams, "Engineering", "Business", 2, 0)
        record_match(self.teams, "Science", "Business", 3, 0)
        table = sorted_table(self.teams)
        self.assertEqual(table[0]["name"], "Science")
        self.assertEqual(goal_difference(table[0]), 3)

    def test_negative_score_is_rejected(self):
        with self.assertRaises(ValueError):
            record_match(self.teams, "Engineering", "Business", -1, 0)

    def test_save_and_load(self):
        record_match(self.teams, "Engineering", "Business", 2, 1)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "league.json"
            save_data(self.teams, path)
            loaded = load_data(path)
            self.assertEqual(loaded[0]["points"], 3)


if __name__ == "__main__":
    unittest.main()
