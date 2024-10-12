import instaloader


class Insta_info:
    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(
            self.loader.context, self.username
        )

    def Login(self):
        login = self.loader.load_session_from_file(self.username)
        return login

    def get_my_followers(self):
        for followers in self.profile.get_followers():
            with open("followers.txt", "a+") as f:
                file = f.write(followers.username + "\n")

        print("Writing followers...")
        print(file)


insta_user = input("Enter instagram username: ")
insta_info = Insta_info(insta_user)

insta_info.Login()
insta_info.get_my_followers()
