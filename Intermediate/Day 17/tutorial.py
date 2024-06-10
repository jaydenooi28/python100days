class User:
    def __init__(self,id,name):
        print(f"User {name} being created")
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
    def sign_in(self):
        print("logged in")

    def follow(self, user):
        user.followers += 1
        user.following += 1
        
user_1 =User("001","Jayden")
user_2 =User("002","Ooi")

# print(user_1.name)
# print(user_2.name)

user_1.follow(user_2)
print(user_1.followers)
print(user_2.following)
print(user_1.followers)
print(user_2.followers)