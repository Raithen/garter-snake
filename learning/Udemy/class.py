class User:
    def __init__(self, user_id, username):
        print("New user being created..")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Steve")
user_2 = User("002", "Annie")

user_1.follow(user_2)
print(f"{user_1.username} is following {user_1.following}")
print(f"{user_1.username} has {user_1.followers} followers")
print(f"{user_2.username} is following {user_2.following}")
print(f"{user_2.username} has {user_2.followers} followers")
