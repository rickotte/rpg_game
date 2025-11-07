import random
import time
from combat.timing_bar import attack_timing_bar, defend_timing_bar


class Battle:
    def __init__(self, players, boss):
        self.players = players
        self.boss = boss
        self.turn = 1

    def start_battle(self):
        print(f"\n⚔️  BATTLE START: {self.boss.name} appears!\n")

        while any(p.is_alive() for p in self.players) and self.boss.is_alive():
            print(f"---------- Turn {self.turn} ----------")
            self.boss.show_status()

            for p in self.players:
                if not p.is_alive():
                    continue

                if not self.boss.is_alive():
                    break

                print(
                    f"\n{p.name}'s Turn — HP: {p.hp}/{p.max_hp}, MP: {p.mp}/{p.max_mp}"
                )
                print("Choose an action:")
                print("1. Normal attack")
                print("2. Skill")

                choice = input("> ")

                if choice == "1":
                    timing = attack_timing_bar()
                    p.attack_enemy(self.boss, timing)

                elif choice == "2" and p.skills:
                    print("\nChoose a skill:")
                    for i, s in enumerate(p.skills, 1):
                        print(
                            f"{i}. {s['name']} (Cost: {s['mp_cost']} MP, Power: {s['power']})"
                        )
                    idx = int(input("> ")) - 1
                    if 0 <= idx < len(p.skills):
                        skill = p.skills[idx]
                        if skill["type"] == "heal":
                            alive_allies = [
                                ally for ally in self.players if ally.is_alive()
                            ]
                            print("\nChoose ally to heal:")
                            for j, ally in enumerate(alive_allies, 1):
                                print(f"{j}. {ally.name} (HP: {ally.hp}/{ally.max_hp})")
                            target_idx = int(input("> ")) - 1
                            if 0 <= target_idx < len(alive_allies):
                                timing = attack_timing_bar()
                                p.use_skill(skill, alive_allies[target_idx], timing)
                        else:
                            timing = attack_timing_bar()
                            p.use_skill(skill, self.boss, timing)

            if not self.boss.is_alive():
                print(f"\n {self.boss.name} was defeated! Victory!")
                break

            # Boss turn
            target = random.choice([p for p in self.players if p.is_alive()])
            skill = self.boss.choose_skill()
            print(
                f"\n{self.boss.name} prepares to use {skill['name']} on {target.name}!"
            )
            time.sleep(1.0)
            defend_result = defend_timing_bar()

            if defend_result == "parry":
                counter_dmg = int(target.attack * 1.5)
                self.boss.hp = max(0, self.boss.hp - counter_dmg)
                print(f"{target.name} counterattacks for {counter_dmg} damage!\n")

            elif defend_result == "defend":
                print(f"{target.name} defended successfully. No damage taken.\n")

            else:
                self.boss.use_skill(skill, target)

            if not any(p.is_alive() for p in self.players):
                print("\n💀 All players have fallen... Game Over.💀")
                break

            self.turn += 1
