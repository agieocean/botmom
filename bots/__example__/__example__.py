# Example lorem ipsum text post bot
from tumblpy import Tumblpy
import time

# Required for any bot that has files referenced
name = "example"
def queue(t, ntq):
    # Example procedure to generate queue
    with open("bots/{0}/tq.txt".format(name), "r", encoding="utf-8") as f:
        tmp = f.read().split("\n")
        topost = tmp[:ntq]
        tq = tmp[ntq:]
    # Example procedure to add posts to queue
    for it, emoji in enumerate(topost):
        post = t.post("post", blog_url="emojiaday", params={'type':'text', 'body': '<b>{0}</b>'.format(emoji), 'tags':'lorem ipsum,example', "state":"queue"})
        print("{0}/{1} {2}".format(str(it).zfill(3), str(len(topost)), post), end="\r")
    # Example procedure to dump unqueued posts back to tq file
    with open("bots/{0}/tq.txt".format(name), "w", encoding="utf-8") as f:
        f.write("\n".join(tq))