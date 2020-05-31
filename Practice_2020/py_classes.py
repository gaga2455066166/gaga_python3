class Hero:
    def __init__(self, name, hp):
        """
        构造函数
        :param name: 英雄名字
        :param hp: 血量
        """
        self.name = name
        self.hp = hp
        pass

    def __del__(self):
        print(self.name + '英雄死亡')
        pass

    @classmethod
    def show_action(cls):
        print('比武')

    @staticmethod
    def show_organizer():
        print('B509')

    def tong(self, enemy):
        enemy.hp -= 10
        info = '[%s]捅了[%s]谁一刀' % (self.name, enemy.name)
        print(info, end='，')
        enemy.show_hp()
        pass

    def kan(self, enemy):
        enemy.hp -= 15
        info = '[%s]捅了[%s]谁一刀' % (self.name, enemy.name)
        print(info, end='，')
        enemy.show_hp()
        pass

    def yao(self):
        self.hp += 20
        info = '[%s]喝了一瓶药，回复20滴血' % self.name
        print(info, end='，')
        self.show_hp()
        pass

    def show_hp(self):
        info = '[%s]还剩[%s]滴血' % (self.name, self.hp)
        print(info)
        pass


hero1 = Hero('h1', 100)
hero2 = Hero('h2', 100)
hero1.tong(hero2)
hero2.kan(hero1)
hero2.yao()
Hero.show_action()
Hero.show_organizer()

if __name__ == '__main__':
    print('main')
