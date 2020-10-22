import praw
import re

reddit = praw.Reddit('goal_bot')
subreddit = reddit.subreddit("soccer")

# Regex for goal posts
pattern = re.compile("^.* ([0-9]+|\[[0-9]+\])( )*-( )*([0-9]+|\[[0-9]+\]) .* ([0-9]+'|[0-9]+'\+[1-9]+')$")

for post in subreddit.stream.submissions() :
    if pattern.match(post.title) is not None and post.link_flair_text=="Media" :
        print("⚽ " + post.title + "\n\nVideo: " + post.url)
