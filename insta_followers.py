import json
import tkinter as tk
from tkinter import filedialog

# import instaloader
#
# L = instaloader.Instaloader()
# insta_user = input("Enter instagram username: ")
# L.interactive_login(insta_user)

# Create & withdraw root window for filedialog
root = tk.Tk()
root.withdraw()

followers_path = filedialog.askopenfile(
    title="Select followers.json: ", filetypes=[("json", "*.json")]
)
following_path = filedialog.askopenfile(
    title="Select following.json: ", filetypes=[("json", "*.json")]
)

followers_json = json.load(followers_path)
followers_list = [
    item["string_list_data"][0]["value"]
    for item in followers_json
    if "string_list_data" in item and item["string_list_data"]
]
following_json = json.load(following_path)
following_list = [
    item["string_list_data"][0]["value"]
    for item in following_json["relationships_following"]
    if "string_list_data" in item and item["string_list_data"]
]

s = set(followers_list)
bad_followers = [x for x in following_list if x not in s]

print(f"{len(bad_followers)} followers do not follow you back: ")
print(bad_followers)
print("-" * 100)

s = set(following_list)
bad_me = [x for x in followers_list if x not in s]
print(f"{len(bad_me)} following that you do not follow back: ")
print(bad_me)
