from flask import Flask
app = Flask(__name__)

import raspweb.views
import raspweb.models