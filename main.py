import praw
import re
import my_token
import telepot
import time
import logging
import datetime
from post import Post

# TO IMPLEMENT
def restore_post() :
    return []

if __name__=="__main__" :
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    reddit = praw.Reddit('goal_bot')
    subreddit = reddit.subreddit("soccer")

    tbot = telepot.Bot(my_token.telegram_bot_token)

    # Regex for goal posts
    pattern = re.compile("^.* ([0-9]+|\[[0-9]+\])( )*-( )*([0-9]+|\[[0-9]+\]) .* ([0-9]+'|[0-9]+'\+[1-9]+')$")

    # List of post posted in the last hour
    posted_last_hour = restore_post()

    logging.info("Starting...")
    # Sleep 1 minute
    while(True) :
        time.sleep(3.0)

        posts = []
        # Put all goal post in a list.
        # It's a list of tuple.
        for post in subreddit.hot(limit=60) :       
            # Check if is a goal post     
            if pattern.match(post.title) is not None and post.link_flair_text=="Media" :
                text="⚽ " + post.title + "\n\nVideo: " + post.url
                p = Post(post.id, datetime.datetime.now(datetime.timezone.utc), text)
                posts.append(p)
        
        # Filter messages. Only messages not published in the last hour
        to_post = [p for p in posts if p not in posted_last_hour]
        
        # Publish post on Telegram
        for p in to_post:
            # tbot.sendMessage(chat_id=my_token.telegram_channel, text=p.text_to_publish)
            posted_last_hour.append(p)
        
        # Remove post older than one hour
        one_hour_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=1)
        posted_last_hour = [p for p in posted_last_hour if p.timestamp > one_hour_ago]