from accessory import Kentoushi, Kyuukizoku, Sengan, Kakan
from character import Noelle, Zhongli, Gorou, Candace, Bennett, Yelan
from weapon import Kikou, Sekikaku
from noelle_expect_damage import noelle_damage_checker



# 聖遺物
# 全体的にかなり低い
one = Kakan(defence_per=11.7+13.9+58.3+13.1, attack_per=4.7+11.1,
            defence_plus=42+23+19, attack_plus=311,
            crt_rate=9.7+9.7+13.2+10.1+31.1, crt_damage=13.2+14.0+7.8+22.5+26.4)
two = Kakan(defence_per=11.7+13.9+58.3+13.1, attack_per=4.7+11.1,
            defence_plus=42+23+19, attack_plus=311,
            crt_rate=9.7+9.7+13.2+10.1+13.2, crt_damage=13.2+14.0+7.8+22.5+62.2)

three = [1248, 1895, 88.6, 169.7]  # 基本最適。これ使っていれば最大値も期待値もほぼ最高
four = [1318, 1743, 91.7, 170.5]  # ゴロー+ベネット時のみ最適だが誤差。最大値は低くなる
five = [1424, 1713, 84.7, 170.5]
kouho = [three]


# サポーター
goro = Gorou(C=0, weapon=None, accessory=Kyuukizoku())
shori = Zhongli(accessory=Sengan())
bennet = Bennett(C=1, basic_attack=747, accessory=Kyuukizoku())
candace = Candace()
yelan = Yelan()
supporters = [shori, goro, bennet]

noelle = Noelle(C=6, weapon=Sekikaku(rank=1), accessory=one)

noelle_damage_checker(noelle, supporters)


# 結果 （聖遺物セット3の場合）

# ゴロー完凸+ベネット1凸だと
# 最大値 61689
# 期待値 56927

# ゴロー無凸+ベネット1凸だと
# 最大値 53721
# 期待値 49868

# ゴロー無凸のみだと
# 最大値 44641
# 期待値 41439

# ゴロー完凸のみだと
# 最大値 51262
# 期待値 47305

# ベネット1凸のみだと
# 最大値 42366
# 期待値 39327


# 現状はノエルが4凸なのと、ゴローがないので
# 最大値 32139
# 期待値 29833
