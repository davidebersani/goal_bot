# Goal bot

A simple bot that retrive goal videos from [r/soccer on Reddit](https://www.reddit.com/r/soccer) and post them on a Telegram channel.
⚽⚽⚽

## 🚀How to run 
Once you have downloaded the source code, install requirements. 
``` python
pip3 install -r requirements.txt
```

After that, edit the *praw.ini* file and insert the credential of your reddit bot.

Then, create a python file called *my_token.py* with these two variables:

  - *telegram_bot_token* = the value of your telegram bot token.
  - *telegram_channel* = id of your channel (Example: @rt_goal_bot) 

## 🔜Todo
- [ ] **Fix first run.** Now the script publishes all goal posts that he retrives on the telegram channel. I want to save permanently the last published post, so at the first run the bot will not re-publishes posts.
