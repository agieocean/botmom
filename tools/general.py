from tumblpy import Tumblpy
import os, datetime, json, time, importlib, threading
from bson import json_util


class GThread(object):
    def __init__(self, interval=3600):
        self.interval = interval
        credl = []
        with open("credentials/credentials", "r") as f:
            credl = f.read().split("\n")
        self.t = Tumblpy(
            credl[0],
            credl[1],
            credl[2],
            credl[3]
        )
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
    
    def checkFor(self):
        bdict = {}
        with open("bots/__tdict__.json", "r") as f:
            bdict = json.loads(f.read(), object_hook=json_util.object_hook)
        for bot in os.listdir("bots"):
            if "__" not in bot:
                if bot not in bdict["bots"]:
                    perday = int(input("How often does your queue post a day for {0}: ".format(bot)))
                    queuing = int(input("How many posts do you want to queue at once for {0}: ".format(bot)))
                    enabled = {"y":True, "n":False}[input("Do you want to enable this bot now? (y/n): ")]
                    if enabled:
                        statusd = "Waiting"
                        statusc = "yellow"
                    else:
                        statusd = "Disabled"
                        statusc = "red"
                    bdict["bots"][bot] = {
                        "reload": datetime.datetime.now(),
                        "queuing":queuing,
                        "perday":perday,
                        "enabled": enabled,
                        "status_description": statusd,
                        "status_color": statusc
                    }
        with open("bots/__tdict__.json", "w") as f:
            f.write(json.dumps(bdict, default=json_util.default, indent=4))

    def firstRun(self):
        initDict = {"bots":{}}
        for bot in os.listdir("bots"):
            if "__" not in bot:
                perday = int(input("How often does your queue post a day for {0}: ".format(bot)))
                queuing = int(input("How many posts do you want to queue at once for {0}: ".format(bot)))
                enabled = {"y":True, "n":False}[input("Do you want to enable this bot now? (y/n): ")]
                initDict["bots"][bot] = {
                    "reload": datetime.datetime.now(),
                    "queuing":queuing,
                    "perday":perday,
                    "enabled": enabled
                }
        with open("bots/__tdict__.json", "w") as f:
            f.write(json.dumps(initDict, default=json_util.default, indent=4))

    def update(self):
        nm = 0
        timeDict = {}
        with open("bots/__tdict__.json", "r") as f:
            timeDict = json.loads(f.read(), object_hook=json_util.object_hook)
        bott = timeDict["bots"]
        for bot, meta in bott.items():
            if meta["enabled"] == True:
                if meta["reload"] < datetime.datetime.now(meta["reload"].tzinfo):
                    module = importlib.import_module("bots.{0}.run".format(bot))
                    tmpq = getattr(module, 'queue')
                    tmpq(self.t, meta["queuing"])
                    reloadt = datetime.datetime.now(meta["reload"].tzinfo) + datetime.timedelta(days=int(meta["queuing"]/meta["perday"]))
                    bott[bot]["reload"] = reloadt
                    print(bot + " will be reloaded at " + str(reloadt))
                    nm += 1
        with open("bots/__tdict__.json", "w") as f:
            f.write(json.dumps(timeDict, default=json_util.default, indent=4))
        print("Number of modules reloaded: " + str(nm).zfill(3))

    def run(self):
        if not os.path.exists("bots/__tdict__.json"):
            self.firstRun()
        self.checkFor()
        while True:
            self.update()
            time.sleep(self.interval)