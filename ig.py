import json
from datetime import datetime

# Get the file
f = open('ig.json')
ig = json.load(f)
f.close()


class Branch:
    epoch: str
    followers: list
    following: list

    def __init__(self, epoch: str) -> None:
        self.epoch = epoch

    def __str__(self) -> str:
        return f"{datetime.fromtimestamp(float(self.epoch)).date()}"

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


def print_differences(comparingFrom, comparingTo):
    print(
        "From ", comparingFrom, " to ", comparingTo, "\n", "I lost the followers: ", comparingFrom.compare_followers(
            comparingTo), "\n",
        "And the following ", comparingFrom.compare_following(
            comparingTo), "\n",
        "And gained the followers: ", comparingTo.compare_followers(
            comparingFrom), "\n",
        "And the following ", comparingTo.compare_following(comparingFrom)
    )


# Creates all the branches and the epoch that it has
branches = []
for epoch in ig:
    branches.append(Branch(epoch))
for branch in branches:
    followers = ig[branch.get_epoch()]["followers"]
    following = ig[branch.get_epoch()]["following"]
    branch.set_followers(followers)
    branch.set_following(following)

while True:
    method = input()

    if method == "list" or method == "l":
        for x in range(len(branches)-1):
            print_differences(branches[x], branches[x+1])

    if method == "last" or method == "r":
        last, before = len(branches)-1, len(branches)-2
        print_differences(branches[before], branches[last])

    if method == "quit" or method == "q":
        break

    if method == "help" or method == "h":
        print("list(l), view(v), last(r) or quit(q)")

    if method == "view" or method == "v":
        for x in range(len(branches)):
            print(x, branches[x])
        key = int(input())
        print(f"On the {branches[key]} I had {len(branches[key].followers)} followers and {
              len(branches[key].following)} following.")

# print(datetime.now().timestamp())
