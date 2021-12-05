import statistics
from flask import Flask, request
import json
from statistics import mean, median

app=Flask(__name__)

## returns the mean of a given list
@app.route('/stat/mean', methods=['POST'])
def get_mean():

    return str(mean(json.loads(request.data)))

## returns the median of a given list
@app.route('/stat/median', methods=['POST'])
def get_median():

    return str(median(json.loads(request.data)))