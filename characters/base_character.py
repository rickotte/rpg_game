import random


class BaseCharacter:
    def __init__(self, name, max_hp, attacks, skills, max_mp=50):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attacks = attacks
        self.skills = skills  # {skill_name: {"damage": int, "cost": int}}
        self.max_mp = max_mp
        self.current_mp = max_mp

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, amount):
        self.current_hp = max(0, self.current_hp - amount)
        print(f"{self.name} took {amount} damage! ({self.current_hp}/{self.max_hp} HP)")

    def spend_mp(self, cost):
        if self.current_mp >= cost:
            self.current_mp -= cost
            return True
        return False

    def recover_mp(self, amount):
        old_mp = self.current_mp
        self.current_mp = min(self.max_mp, self.current_mp + amount)
        gained = self.current_mp - old_mp
        if gained > 0:
            print(
                f"{self.name} recovered {gained} MP! ({self.current_mp}/{self.max_mp} MP)"
            )

    def normal_attack(self, target):
        attack_name, damage = random.choice(list(self.attacks.items()))
        print(f"{self.name} used {attack_name}!")
        target.take_damage(damage)
        # Restore MP when doing a normal attack
        self.recover_mp(10)

    def use_skill(self, target, skill_name=None):
        available_skills = [
            s for s in self.skills.items() if self.current_mp >= s[1]["cost"]
        ]
        if not available_skills:
            print(
                f"{self.name} has no MP for skills! Performing normal attack instead."
            )
            self.normal_attack(target)
            return

        if skill_name:
            if skill_name not in self.skills:
                print(f"{self.name} doesn't know that skill.")
                return
            skill = skill_name
            info = self.skills[skill]
        else:
            skill, info = random.choice(available_skills)

        cost, damage = info["cost"], info["damage"]
        if not self.spend_mp(cost):
            print(f"{self.name} doesn’t have enough MP! Normal attack instead.")
            self.normal_attack(target)
            return

        print(f"{self.name} used skill: {skill}! (-{cost} MP)")
        target.take_damage(damage)
