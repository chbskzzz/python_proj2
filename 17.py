'''
PascalCase
camalCase
snake_case

CONSTRUCTOR
class Car:
    def __init__(self):
    #initialise attributes

METHOD
class Car:
    def enter_race_mode():
        self.seats = 2

노력은 멈추지 않아야 한다다
'''

class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(100, "bbss")
user_2 = User(200, "sskk")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)