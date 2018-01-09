from tools import general, serve
import sys

print(sys.argv[1])
if sys.argv[1] == "test":
    g = general.GThread(test=True)
else:
    g = general.GThread()
serve.run()
if sys.argv[1] == "test":
    exit()