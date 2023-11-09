class Group():
    """
    Create groups of users.
    """

    def __init__(self, users = [], name = 'some_name', id = 1):
        self.users = users
        self.group_name = name
        self.id = id

    def set_name(self, name: str):
        self.name = name
    
    def add_new_user(self, user, id):
        if self.id == id:
            self.users.append(user)
        else:
            print("Sorry, there's no project.")

