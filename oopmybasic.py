# oopmybasic.py

class Robot:
    def __init__(self, name, wheel, arm):
        self.name = name
        self.wheel = wheel
        self.arm = arm

    def run(self, destination):
        self.destination = destination
        print(f'{self.name} running to {self.destination}')

    def getOrder(self, order):
        self.order = order
        print(f'{self.name} roger that, {self.order}')


class SuperRobot(Robot):
    def __init__(self, name, wheel, arm, wing):
        super().__init__(name, wheel, arm)
        self.wing = wing

    def fly(self, destination):
        self.destination = destination
        print(f'{self.name} fly to {self.destination}')

    def getOrder(self, order):
        self.order = order
        print(f'{self.name} go by fly...')
        print(f'{self.name} roger that, {self.order}')


if __name__ == '__main__':
    robot1 = Robot('AAA', 4, 2)
    robot2 = SuperRobot('BBB', 4, 2, 2)

    robot1.run('ปากซอย')
    robot1.getOrder('ซื้อก๋วยเตี๋ยว 1 ถุง')
    print('-----------------')
    robot2.fly('ตลาด')
    robot2.getOrder('ซื้อข้าวมันไก่ 2 ห่อ')
