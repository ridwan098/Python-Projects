class Enemy():
    life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("You're dead")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()

enemy1.attack()
enemy1.checkLife()
