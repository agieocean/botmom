# Import basic controller template
from controllers import basic
from bson import json_util
import json
# Define handler based on basic handler template
class Handler(basic.Handler):
    # Get handler
    def getGen(self, arguments):
        # Reload jinja environment and database tool
        self.cr()
        bots = {}
        with open("bots/__tdict__.json", "r") as f:
            bots = json.loads(f.read(), object_hook=json_util.object_hook)["bots"]
        # Load login template
        html = self.env.get_template("index/index.html")
        # Render login template with title
        html = html.render(
            title="Home",
            nav=False,
            bots=bots
        )
        # Return html to get handler to be written
        return html