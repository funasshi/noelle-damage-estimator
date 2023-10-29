class Accessory:
    def __init__(self, name, attack_per=0, defence_per=0, attack_plus=0, defence_plus=0, crt_rate=0, crt_damage=0):
        self.name = name
        self.attack_per = attack_per
        self.defence_per = defence_per
        self.attack_plus = attack_plus
        self.defence_plus = defence_plus
        self.crt_rate = crt_rate
        self.crt_damage = crt_damage

    def attack_buff(self, *input):
        # 上がる攻撃力の実数値を返す
        return 0

    def damage_buff(self, *input):  
        # ダメバフ%の値を返す
        return 0

    def defence_buff(self, *input):
        # 上がる防御力の実数値を返す
        return 0


class Kentoushi(Accessory):
    def __init__(self, attack_per=0, defence_per=0, attack_plus=0, defence_plus=0, crt_rate=0, crt_damage=0):
        super().__init__(name='剣闘士', attack_per=attack_per, defence_per=defence_per,
                         attack_plus=attack_plus, defence_plus=defence_plus, crt_rate=crt_rate, crt_damage=crt_damage)

    def damage_buff(self):
        return 35

    def attack_buff(self, noelle):
        return noelle.basic_attack*0.18
    
    def critical_buff(self, noelle):
        return noelle.basic_attack*0.18



class Sengan(Accessory):
    def __init__(self, attack_per=0, defence_per=0, attack_plus=0, defence_plus=0, crt_rate=0, crt_damage=0):
        super().__init__(name='千石', attack_per=attack_per, defence_per=defence_per,
                         attack_plus=attack_plus, defence_plus=defence_plus, crt_rate=crt_rate, crt_damage=crt_damage)

    def attack_buff(self, noelle):
        return noelle.basic_attack*0.2


class Kyuukizoku(Accessory):
    def __init__(self, attack_per=0, defence_per=0, attack_plus=0, defence_plus=0, crt_rate=0, crt_damage=0):
        super().__init__(name='旧貴族', attack_per=attack_per, defence_per=defence_per,
                         attack_plus=attack_plus, defence_plus=defence_plus, crt_rate=crt_rate, crt_damage=crt_damage)

    def attack_buff(self, noelle):
        return noelle.basic_attack*0.2


class Kakan(Accessory):
    def __init__(self, attack_per=0, defence_per=0, attack_plus=0, defence_plus=0, crt_rate=0, crt_damage=0):
        super().__init__(name='華館', attack_per=attack_per, defence_per=defence_per,
                         attack_plus=attack_plus, defence_plus=defence_plus, crt_rate=crt_rate, crt_damage=crt_damage)

    def damage_buff(self):
        return 24

    def defence_buff(self, noelle):
        return noelle.basic_defence*0.54

class Newone(Accessory):
    def __init__(self, attack_per=0, defence_per=0, attack_plus=0, defence_plus=0, crt_rate=0, crt_damage=0):
        super().__init__(name='リーク', attack_per=attack_per, defence_per=defence_per,
                         attack_plus=attack_plus, defence_plus=defence_plus, crt_rate=crt_rate, crt_damage=crt_damage)

    def damage_buff(self):
        return 15

    def defence_buff(self, noelle):
        return noelle.basic_defence*0.54
