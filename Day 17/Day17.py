class User():
    def __init__(self,Id,userName):
        self.id = Id
        self.UserName = userName
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers += 1
        self.following += 1
        

user1 = User("31","Captin_Jo")
user2 = User("33","Captin_Jo22")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)