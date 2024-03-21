import sys
import praw
import time

curr = 0
start = time.time()
def progress_bar(total, bar_length, current, ind, max):
    fraction = current / total
    arrow = int(fraction * bar_length+1) * '-'
    padding = int(bar_length - len(arrow)) * '='
    sys.stdout.write(f"/rRetrieving Data: [{arrow}{padding}] {round(fraction*100, 2)+0.18}% ({ind+1}/{max})")
reddit = praw.Reddit(client_id="l-m2GkV6Gu-0aIVDkp69_w",
                     client_secret="27eq57VWslbPAUxgZ1tJbpOiQ-qBwg",
                     username = "NoDance54",
                     password = "1a2b3c4d5e6f",
                     user_agent="praw_tut")
ban, unban, subr = [], [], []
filepath = "C:/Users/sfsga/Desktop/NSFW_Subreddits.txt"
f = open(filepath, "r")
for a in f:
  subr.append(a)

for x in subr:
    message = ""
    curr = (subr.index(x)/len(subr))*100
    sub = reddit.subreddit(x)
    try:
        if sub.over18:
            message = "Unbanned NSFW Subreddit: reddit.com/r/" + str(sub) + "/n"
        unban.append(message)
    except:
        message = "Banned NSFW Subreddit: reddit.com/r/" + str(sub)
    progress_bar(100, 50, curr, subr.index(x), len(subr))
    sys.stdout.flush()

f = open(filepath, "wt")
f.write("")
for h in unban:
    f = open(filepath, "at")
    f.write(h)
end = time.time() - start
print(f"/nOperation took: {end} seconds")
print(f"Number of banned subreddits: {len(ban)}")
print(f"Number of not-banned subreddits: {len(unban)}")