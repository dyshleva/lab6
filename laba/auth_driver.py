import auth

# Set up a test user and permission
# auth.authenticator.add_user("joe", "joepassword")
auth.authorizor.add_permission("test program")
auth.authorizor.add_permission("change program")
# auth.authorizor.permit_user("test program", "joe")


class Editor:
    '''class to resemble the interface'''

    def __init__(self):
        '''Construct'''
        Editor.main_user = None
        self.username = None
        self.menu_map = {
            "add": self.add_user,
            "login": self.login,
            "test": self.test,
            "change": self.change,
            'logout': self.logout,
            "quit": self.quit
        }

        self.menu_map_main = {
            "add": self.add_user,
            "login": self.login,
            "test": self.test,
            "change": self.change,
            'logout': self.logout,
            'permit': self.permit_user,
            "quit": self.quit
        }

    def add_user(self):
        '''add user'''
        username = input("username: ")
        password = input("password: ")
        try:
            auth.authenticator.add_user(username, password)
        except auth.UsernameAlreadyExists:
            print("Username already exists")
        except auth.PasswordTooShort:
            print("Password is too short")
        else:
            print('User '+username+'  is registered')

    def login(self):
        '''login into account'''
        # print(list(auth.authenticator.users.keys()), Editor.main_user)
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist. Create a new one")
                break
                # self.menu()
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
                break
            else:
                self.username = username

    def is_permitted(self, permission):
        '''check the permited permissions'''
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        '''check whether test is permitted'''
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        '''check whether change is permitted'''
        if self.is_permitted("change program"):
            print("Changing program now...")

    def permit_user(self):
        '''permit some permitions to user'''
        try:
            if self.username == Editor.main_user:
                print(', '.join(list(auth.authorizor.permissions.keys())))
                username = input("Enter username: ")
                perm_name = input("Permission to give: ")
                auth.authorizor.permit_user(perm_name, username)
        except auth.InvalidUsername:
            print("Sorry, that username does not exist. Try another one")
        except auth.PermissionError:
            print("Sorry, that permission does not exist. Try another one")

    def logout(self):
        '''logout of the account'''
        self.username = None

    def quit(self):
        '''quit the account'''
        raise SystemExit()

    def menu(self):
        '''menu of actions'''
        try:
            answer = ""

            while True:
                if self.username and Editor.main_user and self.username == Editor.main_user:
                    # if self.username == Editor.main_user:
                    print(
                        """
Please enter a command:
\tadd\tAdd user
\tlogin\tLogin
\ttest\tTest the program
\tchange\tChange the program
\tlogout\tLogout
\tpermit\tPermit
\tquit\tQuit
"""
                    )
                else:
                    print(
                        """
Please enter a command:
\tadd\tAdd user
\tlogin\tLogin
\ttest\tTest the program
\tchange\tChange the program
\tlogout\tLogout
\tquit\tQuit
"""
                    )
                answer = input("enter a command: ").lower()
                try:
                    if self.username and Editor.main_user and self.username == Editor.main_user:
                        func = self.menu_map_main[answer]
                    else:
                        func = self.menu_map[answer]
                    if len(list(auth.authenticator.users.keys())) == 1:
                        Editor.main_user = list(
                            auth.authenticator.users.keys())[0]
                        for key in list(auth.authorizor.permissions.keys()):
                            auth.authorizor.permissions[key].add(
                                Editor.main_user)
                    # print(auth.authorizor.permissions)
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


Editor().menu()
