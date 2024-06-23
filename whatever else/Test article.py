import praw

reddit = praw.Reddit(client_id="l-m2GkV6Gu-0aIVDkp69_w",
                     client_secret="27eq57VWslbPAUxgZ1tJbpOiQ-qBwg",
                     username = "NoDance54",
                     password = "1a2b3c4d5e6f",
                     user_agent="praw_tut")
sub = reddit.subreddit("plugged")
try:
    if sub.over18: print("Subreddit not banned")
except:
    print("Subreddit banned")