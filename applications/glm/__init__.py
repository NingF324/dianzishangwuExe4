from flask import Blueprint

gpt = Blueprint('glm', __name__)

from .glm import *
