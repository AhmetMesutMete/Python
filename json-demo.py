import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.is_logged_in = False
        self.current_user = {}

        # load users from users.json file
        self.load_users()

    def load_users(self):
        if os.path.exists("users.json"):
            with open("users.json") as file:
                user_data = json.load(file)
                for user in user_data:
                    user = json.loads(user)
                    new_user = User(
                        username=user["username"],
                        password=user["password"],
                        email=user["email"],
                    )
                    self.users.append(new_user)
        # self.users = [User(u["username"], u["password"], u["email"]) for u in data]

    def register(self, user: User):
        self.users.append(user)
        self.save_to_file()
        print("A user has been created!")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                self.is_logged_in = True
                print("Logged in!")
                break

    def logout(self):
        self.current_user = {}
        self.is_logged_in = False
        print("Logged out!")

    def identity(self):
        if self.is_logged_in:
            print(f"username: {self.current_user.username}")
        else:
            print("Not yet logged in!")

    def save_to_file(self):
        user_list = [json.dumps(user.__dict__) for user in self.users]

        with open("users.json", "w") as file:
            json.dump(user_list, file)
            # json.dump([user.__dict__ for user in self.users], file)


repository = UserRepository()

while True:
    print(" Menu ".center(50, "*"))
    choice = input(
        "1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour choice: "
    )
    if choice == "5":
        break
    else:
        if choice == "1":  # register
            username = input("username: ")
            usernames = [p.username for p in repository.users]
            if username not in usernames:
                password = input("password: ")
                email = input("email: ")
                user = User(username=username, password=password, email=email)
                repository.register(user=user)
            else:
                print(
                    "The username is already in use, you can try to register again with a different username."
                )
        elif choice == "2":  # login
            if repository.is_logged_in:
                print(
                    "Already logged in! Please logout first to login with another user!"
                )
            else:
                username = input("username: ")
                password = input("password: ")
                repository.login(username, password)
        elif choice == "3":  # logout
            repository.logout()
        elif choice == "4":  # display username
            repository.identity()
        else:
            print("Wrong entry please try again...")
