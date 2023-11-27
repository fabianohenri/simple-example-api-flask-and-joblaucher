import logging
import os

from flask import Flask
from flask_restful import Api

from utils.logging_format import LoggingFormat
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

VERSION = "0.0"


# Log em debug
logging.basicConfig(level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(threadName)s - %(''message)s')

# DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')
# LoggingFormat.format("Dropbox Token: " + str(DROPBOX_TOKEN), "Info")

LoggingFormat.format(f"Api Online - v {VERSION}", "Sucess")
