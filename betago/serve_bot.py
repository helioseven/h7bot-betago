import os
import sys
import h5py
from flask import redirect, send_from_directory, url_for

# Ignore TF warnings, display only errors.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Include the path to the local version of dlgo.
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from dlgo.httpfrontend import get_web_app

# load model
model_file = h5py.File("betago/agents/predict_net.hdf5", "r")
bot_from_file = load_prediction_agent(model_file)
model_file.close()

# build app
app = get_web_app({'predict': bot_from_file})

# add favicon route
@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(dir_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")

# add home page route
@app.route('/')
def index():
	return redirect(url_for("static", filename="play_predict_19.html"))