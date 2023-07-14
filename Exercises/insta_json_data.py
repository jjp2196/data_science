import json

# For analyzing Instagram Follower/Following Data by .json

# Organize Follower Data

# Change read in file according to your system
followers_file = open("followers_1.json")
followers_json = json.load(followers_file)

followers = []
for follower in followers_json:
    followers.append(follower["string_list_data"][0]["value"])

# Organize Following Data

following_file = open("following.json")
following_json = json.load(following_file)

not_following_back = []
for following in following_json["relationships_following"]:
    temp = following(["string_list_data"][0]["value"])
    if temp not in followers:
        not_following_back.append(temp)

print(not_following_back)