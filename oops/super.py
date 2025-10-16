# super()


class User(object):  # Parent class
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):  # Sub class
    def __init__(self, name, power, email):
        # User.__init__(self, email)  # One way of doing

        # Super is referring to the superclass or the class above wizard, which is User.
        # This is actually a new addition as of Python 2.2
        # With super, we actually no longer need the self, so our code even cleaner.
        super().__init__(email)  # Second way of doing
        self.name = name
        self.power = power
        # self.email = email

    def attack(self):
        print(f"attacking with power of {self.power}")


wizard1 = Wizard("Gibson", 42, "gibson@yavar.ai")
print(wizard1.email)
