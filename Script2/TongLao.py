class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if (name == 'WYZ'):
            print("“师弟！！！！")
        elif (name == '李秋水'):
            print("呸，贱人")
        elif (name == "呸，贱人"):
            print("叛徒！我杀了你")

    def fight_zms(self, hp, name):
        self.hp = self.hp / 2
        self.power = self.power * 10
