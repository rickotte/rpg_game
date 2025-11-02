import random
from .base_character import BaseCharacter


class Boss(BaseCharacter):
    def __init__(self, name, max_hp, attacks, skills, max_mp=80):
        super().__init__(name, max_hp, attacks, skills, max_mp)

    def take_turn(self, targets):
        if not self.is_alive():
            return
        target = random.choice([t for t in targets if t.is_alive()])
        print(f"\n{self.name}'s turn!")
        if random.random() < 0.6:
            self.normal_attack(target)
        else:
            self.use_skill(target)
