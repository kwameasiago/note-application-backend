# declare variables

from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

from app import views