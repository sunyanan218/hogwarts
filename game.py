# 一个多回合制游戏，每个角色都有hp
# 和power，
# hp代表血量，power代表攻击力，hp的初始值为1000，
# power的初始值为200。打斗多个回合
# 定义一个fight方法：
# my_hp = hp - enemy_power
# enemy_final_hp = enemy_hp - my_power
# 谁的hp先为0，那么谁就输了
def game():
    my_hp=1000
    my_power=200
    enemy_hp=1500
    enemy_power=300
    while True:
        my_hp=my_hp-enemy_power
        enemy_hp=enemy_hp-my_power
        if my_hp <= 0:
            print("我输了,能量值",my_hp )
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break


game()
