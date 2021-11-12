from flask import request, jsonify

from api import app
import json
import pandas as pd

from predictor.kmeans import KMeansModel


@app.route('/getPredictions', methods=['GET', 'POST'])
def add_message():
    print(request.json)
    try:
        numbers = pd.json_normalize(request.json)
        print(numbers)

        try:
            model = KMeansModel(n=4)
            predictions = model.predict(numbers)
            return json.dumps(predictions, ensure_ascii=False)

        except Exception:
            return internal_server_error()

    except Exception:
        return bad_request()


@app.errorhandler(400)
def bad_request():
    message = {
        'status': 400,
        'message': 'Bad Request: Please check your data payload.',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp

@app.errorhandler(500)
def internal_server_error():
    message = {
        'status': 500,
        'message': 'Internal server error.',
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp
