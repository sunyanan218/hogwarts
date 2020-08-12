class Dog:
    def __init__(self,name,age,male,hobby,weight):
        self.name=name
        self.age=age
        self.male=male
        self.hobby=hobby
        self.weight=weight
        # print("姓名{name}\n年龄{age}\n性别{male}\n爱好{hobby}\n体重{weight}")
    def play(self,name):
        print(f"{name}玩游戏")

dog=Dog("小白","2","公","玩","30")

print(f"姓名:{dog.name}\n年龄:{dog.age}\n性别:{dog.male}\n爱好:{dog.hobby}\n体重:{dog.weight}")
dog.play(dog.name)

