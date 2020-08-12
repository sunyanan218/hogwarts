from Script2.TongLao import TongLao
from Script2.XuZhu import XuZhu


def game():
    tonglao = TongLao(2000, 30)
    xuzhu = XuZhu(3000, 10)
    while True:
        tonglao.hp = tonglao.hp - xuzhu.power
        xuzhu.hp = xuzhu.hp - tonglao.power
        #print(f"虚竹的剩余能量{xuzhu.hp}，童姥的剩余能量{tonglao.hp}")
        if tonglao.hp <= 0:
            print(f"虚竹赢了,虚竹的剩余能量{xuzhu.hp}，童姥的剩余能量{tonglao.hp}")
            break
        elif xuzhu.hp <= 0:
            print(f"童姥赢了,虚竹的剩余能量{xuzhu.hp}，童姥的剩余能量{tonglao.hp}")
            break


game()
