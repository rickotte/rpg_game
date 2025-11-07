from .base_character import BaseCharacter


class Player(BaseCharacter):
    def __init__(self, name, max_hp, max_mp, attack, skills):
        super().__init__(name, max_hp, max_mp, attack, skills)

    def attack_enemy(self, target, timing):
        base_dmg = self.attack
        dmg = int(base_dmg * timing)
        target.hp = max(0, target.hp - dmg)
        self.mp = min(self.max_mp, self.mp + 10)  # restore 10 MP
        print(f"{self.name} attacks {target.name} for {dmg} damage and restores 10 MP!")
        return dmg

    def use_skill(self, skill, target, timing):
        skill_name = skill["name"]
        mp_cost = skill.get("mp_cost", 0)
        skill_type = skill.get("type", "attack")
        power = skill.get("power", 0)

        if self.mp < mp_cost:
            print(f"{self.name} doesn't have enough MP to use {skill_name}!")
            return 0

        self.mp -= mp_cost

        if skill_type == "attack":
            base_dmg = self.attack + power
            dmg = int(base_dmg * timing)
            target.hp = max(0, target.hp - dmg)
            print(
                f"{self.name} used {skill_name} and dealt {dmg} damage to {target.name}!"
            )
            return dmg

        elif skill_type == "heal":
            heal_amount = int(power * timing)
            target.hp = min(target.max_hp, target.hp + heal_amount)
            print(
                f"{self.name} used {skill_name} and healed {target.name} for {heal_amount} HP!"
            )
            return -heal_amount
