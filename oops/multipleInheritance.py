# Multiple Inheritance
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077462#overview


class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrow = arrows

    def check_arrows(self):
        print(f"{self.arrow} remaining")

    def run(self):
        print("ran really fast")


# When we do multiple inheritance, things can get complicated, And part of this reason that some programing languages don't actually allow you to do multiple inheritance.
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, archer):
        Archer.__init__(self, name, archer)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg("borgie", 500, 4000)

print(hb1.run())
print(hb1.attack())
print(hb1.sign_in())

# Continue with => MRO - Method Resolution Order.
