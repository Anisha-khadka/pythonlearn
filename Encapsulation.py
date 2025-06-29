# Encapsulation

class User:
    email = 'Ram'
    __password = 'Ram123'

    def __get_email(self):
        print(self.email)

user1 = User()
user1.__get_email()
print(user1.__password)
