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

pics = reddit.subreddit('pics').hot(limit=None)
pic_urls = []
for pic in pics:
    pic_urls.append(pic.url)

with open(cwd + "/data_raw/picture_urls.txt", "w+") as f:
    f.seek(0)
    for url in pic_urls:
        f.write(url + "\n")
    f.truncate()
