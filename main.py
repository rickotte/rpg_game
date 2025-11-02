import json
from characters import Player, Boss
from combat import Battle


def load_players():
    with open("data/players.json") as f:
        data = json.load(f)
    players = [
        Player(
            p["name"],
            p["max_hp"],
            p["attacks"],
            p["skills"],
            max_mp=p.get("max_mp", 50),
        )
        for p in data["players"]
    ]
    return players


def load_boss():
    with open("data/bosses.json") as f:
        data = json.load(f)
    b = data["bosses"][0]
    return Boss(
        b["name"], b["max_hp"], b["attacks"], b["skills"], max_mp=b.get("max_mp", 60)
    )


def main():
    print("=== Turn-Based Battle Demo with MP ===\n")
    players = load_players()
    boss = load_boss()
    battle = Battle(players, boss)
    battle.start()


if __name__ == "__main__":
    main()
