import json
from characters.player_team import Player
from characters.boss import Boss
from combat.battle import Battle


def load_data(path):
    with open(path, "r") as f:
        return json.load(f)


def main():
    players_data = load_data("data/players.json")
    bosses_data = load_data("data/bosses.json")

    team = [Player(**pdata) for pdata in players_data]
    boss = Boss(**bosses_data[0])

    battle = Battle(team, boss)
    battle.start_battle()


if __name__ == "__main__":
    main()
