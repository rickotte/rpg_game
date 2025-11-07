from .base_character import BaseCharacter
import random


class Boss(BaseCharacter):
    def __init__(self, name, max_hp, max_mp, attack, skills):
        super().__init__(name, max_hp, max_mp, attack, skills)

    def choose_skill(self):
        return random.choice(self.skills)

    def use_skill(self, skill, target):
        skill_name = skill["name"]
        skill_type = skill.get("type", "attack")
        power = skill.get("power", 0)

        if skill_type == "attack":
            dmg = self.attack + power
            target.hp = max(0, target.hp - dmg)
            print(f"{self.name} used {skill_name}! {target.name} took {dmg} damage!")
            return dmg
        return 0
