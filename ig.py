import json
from datetime import datetime

# Get the file
f = open('ig.json')
ig = json.load(f)
f.close()

# Creates multiple instances of branches
class Branch:
    epoch: str
    followers: list
    following: list

    def __init__(self, epoch: str) -> None:
        self.epoch = epoch

    def compare_followers(self, other) -> list:
        return list(set(self.get_followers()) - set(other.get_followers()))
    def compare_following(self, other) -> list:
        return list(set(self.get_following()) - set(other.get_following()))

    def set_followers(self, followers) -> None:
        self.followers = followers
    def set_following(self, following) -> None:
        self.following = following

    def get_epoch(self) -> str:
        return self.epoch

    def get_followers(self) -> list:
        return self.followers
    def get_following(self) -> list:
        return self.following

# Creates all the branches and the epoch that it has
branches = []
for epochs in ig:
    branches.append(Branch(epochs))
for branch in branches:
    followers = ig[branch.get_epoch()]["followers"]
    following = ig[branch.get_epoch()]["following"]
    branch.set_followers(followers)
    branch.set_following(following)

for x in range(len(branches)-1):
    print("From ", branches[x], " to ", branches[x+1], " I lost the followers: ", branches[x].compare_followers(branches[x-1]), " and the following ", branches[x].compare_following(branches[x-1]))
