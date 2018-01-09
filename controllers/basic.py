# Import BeautifulSoup library
from bs4 import BeautifulSoup
# Import web module from tornado
from tornado import web
# Import Environment and FileSystemLoader modules from jinja2
from jinja2 import Environment, FileSystemLoader


class Handler(web.RequestHandler):
    # Method to reload jinja environment and database connection
    def cr(self):
        # Create jinja2 environment from html templates directory res/html
        self.env = Environment(
            loader=FileSystemLoader("res/html"),
            extensions=["jinja2.ext.do",]
        )
    # Clean html with BeautifulSoup and return it
    def clean(self, html):
        return BeautifulSoup(html, "html.parser").prettify()
    # Default getGen method
    def getGen(self, arguments):
        return "<html><body><h1>Hello world!</h1></body></html>"
    # Get method
    def get(self):
        try:
            # Write cleansed html from getGen
            self.write(
                # Clean html
                self.clean(
                    # Call getGen with get arguments
                    self.getGen(
                        { k: self.get_argument(k) for k in self.request.arguments }
                    )
                )
            )
        except Exception as e:
            print(e)
            raise e
    # Default postGen method
    def postGen(self, arguments):
        return "<html><body><h1>Hello world!</h1></body></html>"
    # Post method
    def post(self):
        try:
            # Write cleansed html from postGen
            self.write(
                # Clean html
                self.clean(
                    # Call postGen with post arguments
                    self.postGen(
                        { k: self.get_argument(k) for k in self.request.arguments }
                    )
                )
            )
        except Exception as e:
            print(e)
            raise e
    # Method to call on error code
    # Receives status code and other args
    def write_error(self, status_code, **kwargs):
        # Reload jinja environmnet and database tools
        self.cr()
        # Log error code
        # Write cleaned redirect to http status cat
        self.write(
            # Clean html
            self.clean(
                self.env.get_template("error/index.html").render(
                    title=str(status_code),
                    info=self._reason
                )
            )
        )
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    # Generate redirect from given url
    # Receives url
    def getRedirect(self, url):
        # Create html redirect
        html="<html><head><meta http-equiv='refresh' content='0; url={0}' /></head></html>".format(
            url)
        # Return redirect
        return html