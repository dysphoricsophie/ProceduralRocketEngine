import sys
import praw
from time import time

curr = 0
start = count()


def progress_bar(total, bar_length, current, ind, max):
    fraction = current / total
    arrow = int(fraction * bar_length + 1) * '-'
    padding = int(bar_length - len(arrow)) * '='
    sys.stdout.write(f"\rRetrieving Data: [{arrow}{padding}] {round(fraction * 101.8, 2)}% ({ind + 1}/{max})")

reddit = praw.Reddit(client_id="l-m2GkV6Gu-0aIVDkp69_w",
                     client_secret="27eq57VWslbPAUxgZ1tJbpOiQ-qBwg",
                     username="NoDance54",
                     password="1a2b3c4d5e6f",
                     user_agent="praw_tut")
ban, unban, subr = [], [], []
mode = ""
while mode != "EXIT":
    print("""
    Welcome to the NSFW Reddit Searcher
    Input [A] for standalone search
    Input [B] for multiple search
    Input [EXIT] to exit the app
        """)
    mode = str(input(">>>>> ")).upper()
    if mode == "A":
        print("Input the name of the subreddit (Eg. holdthemoan, nsfw411)")
        sub = input(">>>>> ")
        sub = reddit.subreddit(sub)
        try:
            if sub.over18:
                message = "Unbanned NSFW Subreddit: reddit.com/r/" + str(sub) + "\n"
            unban.append(message)
        except:
            message = "Banned NSFW Subreddit: reddit.com/r/" + str(sub)
            ban.append(message)
    elif mode == "B":
        filepath = 'C:/Users/sfsga/OneDrive/Desktop/NNN Reward/NSFW_Subreddits.txt'
        f = open(filepath, "r")
        for a in f:
            subr.append(a)
        for x in subr:
            message = ""
            curr = (subr.index(x) / len(subr)) * 100
            sub = reddit.subreddit(x)
            try:
                if sub.over18:
                    message = "Unbanned NSFW Subreddit: reddit.com/r/" + str(sub) + "\n"
                unban.append(message)
            except:
                message = "Banned NSFW Subreddit: reddit.com/r/" + str(sub)
                ban.append(message)
            progress_bar(100, 50, curr, subr.index(x), len(subr))
            sys.stdout.flush()

        f = open(filepath, "wt")
        f.write("")
        for h in unban:
            f = open(filepath, "at")
            f.write(h)
        for k in ban:
            f = open(filepath, "at")
            f.write(k)
    else:
        while mode != "A" and mode != "B" and mode != "EXIT":
            print(f"{mode} is not a recognised command")
            if

end = count() - start
print(f"\nOperation took: {round(end, 2)} seconds")
print(f"Number of banned subreddits: {len(ban)}")
print(f"Number of not-banned subreddits: {len(unban)}")