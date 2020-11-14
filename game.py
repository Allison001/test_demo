import random


def fight(d_hp,d_power):
    m_hp = 1000
    m_power = 200

    while True:
        m_hp = m_hp - d_power
        d_hp = d_hp - m_power
        if m_hp <=0:
            print("敌人赢了")
            print(f"我的剩余血量：{m_hp}")
            print(f"敌人的剩余血量:{d_hp}")
            break
        elif d_hp <=0:
            print("我赢了")
            print(f"我的剩余血量：{m_hp}")
            print(f"敌人的剩余血量:{d_hp}")
            break

if __name__ == '__main__':
    #使用列表推导式生产一列随机数
    hp = [x for x in range(900,1100)]
    #敌人的血量在以上列表中随机选择一个数字
    d_hp = random.choice(hp)
    #敌人的攻击力在100-2000随机选择一个数字
    d_power = random.randint(100,200)
    #调用函数fight
    fight(d_hp,d_power)