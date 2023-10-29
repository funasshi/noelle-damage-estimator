from accessory import *


class Character:
    def __init__(self, name, attack=0, defence=0, hp=0, basic_attack=0, basic_defence=0,
                 C=0, crt_rate=5, crt_damage=50, weapon=None, accessory=None):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.basic_attack = basic_attack
        self.basic_defence = basic_defence
        self.C = C
        self.crt_rate = crt_rate
        self.crt_damage = crt_damage
        self.weapon = weapon
        self.accessory = accessory
        if weapon:
            self.basic_attack += weapon.basic_attack

    def attack_buff(self, *inputs):
        return 0

    def defence_buff(self, *inputs):
        return 0

    def damage_buff(self, *inputs):
        return 0

    def special_damage_plus(self, *inputs):
        return 0

    def crt_rate_buff(self, *inputs):
        return 0

    def crt_damage_buff(self, *inputs):
        return 0

    def enemy_debuff(self, *inputs):
        return 0

    def enemy_defence(self, *inputs):
        return 0


class Noelle(Character):
    def __init__(self, C, weapon, accessory):
        super().__init__(name='ノエル',
                         basic_attack=191, basic_defence=799,
                         C=C,
                         weapon=weapon, accessory=accessory)

    def defence_buff(self, noelle):
        return noelle.basic_defence*0.3


class Zhongli(Character):
    def __init__(self, attack=0, defence=0, hp=0, basic_attack=0, basic_defence=0,
                 C=0, crt_rate=5, crt_damage=50, weapon=None, accessory=Sengan()):
        super().__init__(name='鍾離', attack=attack, defence=defence, hp=hp,
                         basic_attack=basic_attack, basic_defence=basic_defence,
                         C=C, crt_rate=crt_rate, crt_damage=crt_damage,
                         weapon=weapon, accessory=accessory)

    def enemy_debuff(self, *inputs):
        return 20


class Bennett(Character):
    def __init__(self, attack=0, defence=0, hp=0, basic_attack=0, basic_defence=0,
                 C=0, crt_rate=5, crt_damage=50, weapon=None, accessory=Kyuukizoku()):
        super().__init__(name='ベネット', attack=attack, defence=defence, hp=hp,
                         basic_attack=basic_attack, basic_defence=basic_defence,
                         C=C, crt_rate=crt_rate, crt_damage=crt_damage,
                         weapon=weapon, accessory=accessory)

    def attack_buff(self, *input):
        if self.C >= 1:
            return self.basic_attack*1.15
        return self.basic_attack*0.95


class Yelan(Character):
    def __init__(self, attack=0, defence=0, hp=0, basic_attack=0, basic_defence=0,
                 C=0, crt_rate=5, crt_damage=50, weapon=None, accessory=None):
        super().__init__(name='夜蘭', attack=attack, defence=defence, hp=hp,
                         basic_attack=basic_attack, basic_defence=basic_defence,
                         C=C, crt_rate=crt_rate, crt_damage=crt_damage,
                         weapon=weapon, accessory=accessory)

    def damage_buff(self, *input):
        return 25


class Gorou(Character):
    def __init__(self, attack=0, defence=0, hp=0, basic_attack=0, basic_defence=0,
                 C=0, crt_rate=5, crt_damage=50, weapon=None, accessory=Kyuukizoku()):
        super().__init__(name='ゴロー', attack=attack, defence=defence, hp=hp,
                         basic_attack=basic_attack, basic_defence=basic_defence,
                         C=C, crt_rate=crt_rate, crt_damage=crt_damage,
                         weapon=weapon, accessory=accessory)

    def defence_buff(self, character: Character, *input):
        return 412+character.basic_defence*0.25

    def damage_buff(self, *input):
        return 15

    def crt_damage_buff(self, *input):
        if self.C == 6:
            return 40
        else:
            return 0


class Candace(Character):
    def __init__(self, attack=0, defence=0, hp=0, basic_attack=0, basic_defence=0,
                 C=0, crt_rate=5, crt_damage=50, weapon=None, accessory=Accessory("")):
        super().__init__(name='キャンディス', attack=attack, defence=defence, hp=hp,
                         basic_defence=basic_defence,
                         C=C, crt_rate=crt_rate, crt_damage=crt_damage,
                         weapon=weapon, accessory=accessory)

    def damage_buff(self, *input):
        return 40
