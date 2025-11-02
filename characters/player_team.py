from .base_character import BaseCharacter


class Player(BaseCharacter):
    def __init__(self, name, max_hp, attacks, skills, max_mp=50):
        super().__init__(name, max_hp, attacks, skills, max_mp)

    def choose_action(self, target):
        print(
            f"\n{self.name}'s turn! HP: {self.current_hp}/{self.max_hp} | MP: {self.current_mp}/{self.max_mp}"
        )
        print("1. Normal Attack (restores 10 MP)")
        print("2. Skill Attack")
        while True:
            choice = input("Choose your action (1/2): ")
            if choice == "1":
                self.normal_attack(target)
                break
            elif choice == "2":
                skill_names = list(self.skills.keys())
                print("\nAvailable Skills:")
                for i, skill in enumerate(skill_names, 1):
                    info = self.skills[skill]
                    print(
                        f"{i}. {skill} (DMG: {info['damage']}, Cost: {info['cost']} MP)"
                    )
                skill_choice = input("Choose a skill number: ")
                if skill_choice.isdigit() and 1 <= int(skill_choice) <= len(
                    skill_names
                ):
                    skill = skill_names[int(skill_choice) - 1]
                    cost = self.skills[skill]["cost"]
                    damage = self.skills[skill]["damage"]
                    if self.current_mp >= cost:
                        self.spend_mp(cost)
                        print(f"{self.name} used {skill}! (-{cost} MP)")
                        target.take_damage(damage)
                    else:
                        print(
                            "Not enough MP! You perform a weak normal attack instead."
                        )
                        self.normal_attack(target)
                    break
                else:
                    print("Invalid skill choice. Try again.")
            else:
                print("Invalid choice. Try again.")
