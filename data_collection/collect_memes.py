import os
import json
import praw
from dotenv import load_dotenv

load_dotenv()

cwd = os.getcwd()

reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        username=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        user_agent=os.getenv("USER_AGENT")
        )

memes = reddit.subreddit('memes').hot(limit=None)
meme_urls = []
for meme in memes:
    meme_urls.append(meme.url)

with open(cwd + "/../data_raw/meme_urls.txt", "w+") as f:
    f.seek(0)
    for url in meme_urls:
        f.write(url + "\n")
    f.truncate()
