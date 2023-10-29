from util import constellation_num2str
def expect_damage(noelle, supporters):

    # 攻撃力計算
    attack = expect_attack(noelle, supporters)

    # 天賦倍率計算
    tenpu_phase = [1.56, 1.45, 1.71, 2.24]

    # 特殊ダメージアップ計算
    special_damage_plus = expect_special_damage_plus(noelle, supporters)

    # ダメバフ計算
    damage_buff = expect_damage_buff(supporters, noelle.weapon, noelle.accessory)
    damage_buff_mul = expect_damage_buff_mul(damage_buff)

    # 会心計算
    crt_damage = expect_critical_damage(noelle, supporters)
    crt_rate = expect_critical_rate(noelle, supporters)
    critical_mul = expect_crtical_mul(crt_rate, crt_damage)

    # 敵耐性計算
    enemy_resistance_mul = expect_enemy_resistance_mul(supporters)

    # 敵防御計算
    enemy_defence = expect_enemy_defence(level=90, enemy_level=90)

    # 計算
    expect_damages = [(attack *
                      tenpu +
                      special_damage_plus) *
                      damage_buff_mul *
                      critical_mul *
                      enemy_resistance_mul *
                      enemy_defence for tenpu in tenpu_phase]
    max_damages = [(attack *
                   tenpu +
                   special_damage_plus) *
                   damage_buff_mul *
                   (1+0.01*crt_damage) *
                   enemy_resistance_mul *
                   enemy_defence for tenpu in tenpu_phase]

    return expect_damages, max_damages, attack, noelle.defence, crt_rate, crt_damage, damage_buff


def expect_defence(noelle, supporters):
    final_defence = noelle.basic_defence
    # ノエルの突破ステータス
    final_defence += noelle.defence_buff(noelle)

    # サポーターの防御バフ
    for supporter in supporters:
        final_defence += supporter.defence_buff(noelle)

    # 聖遺物の防御バフ
    final_defence += noelle.accessory.defence_buff(noelle)
    final_defence += noelle.accessory.defence_per * noelle.basic_defence * 0.01
    final_defence += noelle.accessory.defence_plus

    # 武器の防御バフ
    final_defence += noelle.weapon.defence_buff(noelle)
    noelle.defence = final_defence

    return final_defence


def expect_attack(noelle, supporters):

    #   attack, defence, noelle_C=6,
    #   basic_attack=701, basic_defence=799, seiibutu='剣闘士',

    # サポーターの聖遺物の一覧
    support_accesories = [supporter.accessory for supporter in supporters]
    final_attack = noelle.basic_attack

    # ゴローの防御力上昇効果
    # ノエル突破ステータス
    # 聖遺物・武器による防御上昇
    defence = expect_defence(noelle, supporters)

    # サポーターによる攻撃力バフ
    for supporter in supporters:
        final_attack += supporter.attack_buff(noelle)
    for support_accessory in support_accesories:
        if support_accessory:
            final_attack += support_accessory.attack_buff(noelle)

    # 聖遺物による攻撃力バフ
    final_attack += noelle.accessory.attack_buff(noelle)
    final_attack += noelle.accessory.attack_per * noelle.basic_attack * 0.01
    final_attack += noelle.accessory.attack_plus

    # ノエル元素爆発
    if noelle.C == 6:
        final_attack += defence*1.35
    elif noelle.C == 5:
        final_attack += defence*0.85
    else:
        final_attack += defence*0.72
    noelle.attack = final_attack
    return final_attack


def expect_special_damage_plus(noelle, supporters):
    for supporter in supporters:
        special_damage_plus = supporter.special_damage_plus(noelle)
    special_damage_plus += noelle.weapon.special_damage_plus(noelle)
    return special_damage_plus


def expect_damage_buff(supporters, weapon, accessory):
    # ダメージバフ計算
    damage_buff = 46.6 + 15  # 聖遺物メインステータス+岩元素共鳴

    # キャラダメバフ
    for supporter in supporters:
        damage_buff += supporter.damage_buff()

    # 武器ダメバフ
    damage_buff += weapon.damage_buff()

    # 聖遺物ダメバフ
    damage_buff += accessory.damage_buff()
    return damage_buff


def expect_damage_buff_mul(damage_buff):
    return 1+damage_buff*0.01


def expect_critical_rate(noelle, supporters):
    crt_rate = noelle.crt_rate
    for supporter in supporters:
        crt_rate += supporter.crt_rate_buff()
    crt_rate += noelle.weapon.crt_rate_buff()
    crt_rate += noelle.accessory.crt_rate
    noelle.crt_rate = crt_rate
    return crt_rate


def expect_critical_damage(noelle, supporters):
    crt_damage = noelle.crt_damage
    for supporter in supporters:
        crt_damage += supporter.crt_damage_buff()
    crt_damage += noelle.weapon.crt_damage_buff()
    crt_damage += noelle.accessory.crt_damage
    return crt_damage


def expect_crtical_mul(crt_rate, crt_damage):
    return (1+(crt_rate*0.01) * (crt_damage*0.01))


def expect_enemy_defence(level=90, enemy_level=90):

    #  (キャラレベル+100) / {(1 - 防御無視%)×(1 - 防御デバフ％)×(敵レベル+100)+キャラレベル+100}
    return (level+100)/((enemy_level+100)+level+100)


def expect_enemy_resistance_mul(supporters):
    # 敵対性計算
    resistance = 10
    resistance -= 20  # 岩元素共鳴

    # デバフ
    for supporter in supporters:
        resistance -= supporter.enemy_debuff()

    if resistance < 0:
        resistance /= 2
    resistance_mul = 1-resistance*0.01
    return resistance_mul


def noelle_damage_checker(noelle, supporters):

    expect_damages, max_damages, attack, defence, crt_rate, crt_damage, damage_buff\
        = expect_damage(noelle, supporters)
    print('========条件=========')
    print('ノエル凸数:{}凸'.format(constellation_num2str(noelle.C)))
    print('武器:{}'.format(noelle.weapon.name))
    print('聖遺物:{}'.format(noelle.accessory.name))
    print('攻撃力:{}'.format(int(attack)))
    print('防御力:{}'.format(int(defence)))
    print('ダメージバフ:{:.1f}%'.format(damage_buff))
    print('会心率:{:.1f}%'.format(crt_rate))
    print('会心ダメージ: {:.1f}'.format(crt_damage))
    for supporter in supporters:
        print('{}:{}凸'.format(supporter.name,
              constellation_num2str(supporter.C)))
    print('=====================')

    print("")
    print("期待値")
    for i, damage in enumerate(expect_damages):
        print('ダメージ{}段目:'.format(i+1), int(damage))

    print("")
    print("最大値")
    for i, damage in enumerate(max_damages):
        print('ダメージ{}段目:'.format(i+1), int(damage))
    return damage
