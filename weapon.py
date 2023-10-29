class Weapon:
    def __init__(self, name, rank, basic_attack):
        self.rank = rank
        self.name = name
        self.basic_attack = basic_attack

    def attack_buff(self, *inputs):
        # 上がる攻撃力の実数値を返す
        return 0

    def defence_buff(self, *inputs):
        # 上がる防御力の実数値を返す
        return 0

    def damage_buff(self, *inputs):
        # ダメバフ%の値を返す
        return 0

    def special_damage_plus(self, *inputs):
        # 特殊加算実数値の値を返す
        return 0

    def crt_rate_buff(self, *inputs):
        # 会心率の%値を返す
        return 0

    def crt_damage_buff(self, *inputs):
        # 会心ダメージの%値を返す
        return 0

    def enemy_debuff(self, *inputs):
        # 耐性ダウンの%の値を返す
        return 0

    def enemy_defence(self, *inputs):
        # 防御力ダウンの値を返す
        return 0


class Kikou(Weapon):
    def __init__(self, rank):
        super().__init__(rank=rank, name='紀行大剣', basic_attack=510)

    def damage_buff(self, *inputs):
        return (self.rank+5)*5

    def crt_rate_buff(self, *inputs):
        return 27.6


class Sekikaku(Weapon):
    def __init__(self, rank):
        super().__init__(rank=rank, name='赤角', basic_attack=542)

    def defence_buff(self, character):
        return (0.28+0.07*(self.rank-1))*character.basic_defence

    def special_damage_plus(self, character):
        return character.defence*(0.4+0.1*(self.rank-1))

    def crt_damage_buff(self, *inputs):
        return 88.2
