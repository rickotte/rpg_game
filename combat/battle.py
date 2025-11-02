import time
from .timing_bar import TimingBar


class Battle:
    def __init__(self, players, boss):
        self.players = players
        self.boss = boss

    def all_players_dead(self):
        return all(not p.is_alive() for p in self.players)

    def show_status(self):
        print("\n=== Team Status ===")
        for p in self.players:
            print(
                f"{p.name}: {p.current_hp}/{p.max_hp} HP | {p.current_mp}/{p.max_mp} MP"
            )
        print(
            f"Boss {self.boss.name}: {self.boss.current_hp}/{self.boss.max_hp} HP | {self.boss.current_mp}/{self.boss.max_mp} MP"
        )
        print("====================\n")

    def start(self):
        print(f"\n The battle begins against {self.boss.name}!\n")
        while not self.all_players_dead() and self.boss.is_alive():
            self.show_status()

            for player in self.players:
                if not player.is_alive():
                    continue
                tb = TimingBar(duration=2)
                tb.run()
                player.choose_action(self.boss)
                time.sleep(1.2)
                if not self.boss.is_alive():
                    print(f"\n {self.boss.name} HAS BEEN DEFEATED")
                    return

            if self.boss.is_alive():
                tb = TimingBar(duration=2)
                tb.run()
                self.boss.take_turn(self.players)
                time.sleep(1.2)

        print("\n All players have fallen\n GAME OVER")
