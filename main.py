from abc import ABC, abstractmethod

class Fighter():
    def __init__(self):
        self.weapon = None
    def fight(self):
        self.weapon.attack()

    def change_weapon(self, weapon):
        self.weapon = weapon
        self.weapon.set_weapon()

class Monster():
    def __init__(self):
        self.weapon = None


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
    def set_weapon(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец рубит монстра мечом")
        print('Меч разрубил мостра пополам. Монстр побежден!')
    def set_weapon(self):
        print('Боец выбирает меч')

class Bow(Weapon):
    def attack(self):
        print("Боец запускает стрелу из лука")
        print('Стрела попала монстру в глаз. Монстр побежден!')
    def set_bow(self):
        print('Боец выбирает лук')

class Grenade(Weapon):
    def attack(self):
        print("Боец кидает гранату")
        print('Граната разнесла монстра на кусочки. Монстр побежден!')
    def set_grenade(self):
        print('Боец выбирает гранату')

# тест использования
monster1 = Monster()
fighter1 = Fighter()
fighter1.change_weapon(Sword())
fighter1.fight()
fighter1.change_weapon(Grenade())
fighter1.fight()
fighter1.change_weapon(Bow())
fighter1.fight()
