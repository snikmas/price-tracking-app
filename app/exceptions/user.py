class UserAlreadyExist(Exception):
    def __init__(self, nickname, message="User already exists"):
        self.nickname = nickname
        self.message = f"{message}: {nickname}"
        super().__init__(self.message)