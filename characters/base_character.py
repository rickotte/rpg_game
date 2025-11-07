class BaseCharacter:
    def __init__(self, name, max_hp, max_mp, attack, skills):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mp = max_mp
        self.mp = max_mp
        self.attack = attack
        self.skills = skills or []

    def is_alive(self):
        """Return True if HP > 0."""
        return self.hp > 0

    def show_status(self):
        print(
            f"{self.name} | HP: {self.hp}/{self.max_hp} | MP: {self.mp}/{self.max_mp}"
        )
