# Import web and ioloop from tornado
from tornado import web, ioloop
# Import views module
import views
# Import all submodules from views
from views import *

# Method to create web application
def make_app():
    # Listen of handlers
    handlers = []
    # Iterate through views
    for mod in views.__all__:
        # If the views name does not contain "__"
        # This is a double check as it should already be handled
        if "__" not in mod:
            # If the view is name index make it the root handler
            if (mod == "index"):
                # Append handler (eval is necessary to allowing 
                # handler to be appended)
                handlers.append((r"/", eval(mod + ".Handler")))
            else:
                # Append handler with endpoint of the name of the handler
                # ex. example would be /example
                handlers.append((r"/" + mod, eval(mod + ".Handler")))
    # Add handler for static files
    handlers.append(
        (
            # Map directory res/public to /
            r"/(.*)",
            web.StaticFileHandler,
            {
                'path':'res/public'
            }
        )
    )
    # Create web application
    t =  web.Application(
        # Define handlers
        handlers,
        # Add cookie secret to encrypt cookies
        cookie_secret="uSuFxXYK8E4$e7UQrGSQx0ZyUBI#&f6odB18IDt@LKp!2Xq4Ji",
        max_buffer_size=2097152
    )
    # Return web application
    return t

def run():
    # Generate web app
    app = make_app()
    # Have the app listen on port 8888
    app.listen(8888)
    # Start the ioloop which runs the app
    ioloop.IOLoop.current().start()