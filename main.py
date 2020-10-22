import praw
import re
import my_token
import telepot
import time
import logging

if __name__=="__main__" : 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    reddit = praw.Reddit('goal_bot')
    subreddit = reddit.subreddit("soccer")

    tbot = telepot.Bot(my_token.telegram_bot_token)

    # Regex for goal posts
    pattern = re.compile("^.* ([0-9]+|\[[0-9]+\])( )*-( )*([0-9]+|\[[0-9]+\]) .* ([0-9]+'|[0-9]+'\+[1-9]+')$")

    # Last title post posted on the channel
    last_title_posted = ""
    # New last title posted on the channel
    new_last_title_posted = ""

    # Sleep 1 minute
    while(True) :
        time.sleep(60.0)

        # Check for new posts
        first_post = True
        for post in subreddit.hot(limit=20) :       
            # Check if is a goal post     
            if pattern.match(post.title) is not None and post.link_flair_text=="Media" :
                text="⚽ " + post.title + "\n\nVideo: " + post.url
                if first_post :
                    new_last_title_posted = post.title
                    first_post = False
                if post.title!=last_title_posted :
                    logging.info("Sending message on channel: " + text)
                    tbot.sendMessage(chat_id="@rt_soccer_goals", text=text)
                else:
                    break
        
        last_title_posted = new_last_title_posted
        logging.info("Last post published: " + last_title_posted)
