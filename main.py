import praw
import re
import my_token
import telepot
import time
import logging
import datetime

    
if __name__=="__main__" :
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    reddit = praw.Reddit('goal_bot')
    subreddit = reddit.subreddit("soccer")

    tbot = telepot.Bot(my_token.telegram_bot_token)

    # Regex for goal posts
    pattern = re.compile("^.* ([0-9]+|\[[0-9]+\])( )*-( )*([0-9]+|\[[0-9]+\]) .* ([0-9]+'|[0-9]+'\+[1-9]+')$")

    # Timestamp of last post published on the Telegram channel
    last_posted = datetime.datetime.utcnow()

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
                posts.append((datetime.datetime.fromtimestamp(post.created_utc), text))   # Tuple <timestamp, text message>
        
        # Filter messages. Only messages more recent than the last post published.
        messages = [(ts, text) for ts, text in posts if ts > last_posted]
        
        # Order messages by timestamp
        messages = sorted(messages, key=lambda tup: tup[0])
        # Publish post on Telegram
        for _,text in messages:
            tbot.sendMessage(chat_id=my_token.telegram_channel, text=text)
        
        # Update last timestamp
        if len(messages)>0: last_posted = messages[0][0]            