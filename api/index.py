from flask import Flask, request, Response
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process-json', methods=['POST'])
def process_json():
    data = request.get_json()
    url = data.get("url")

    try:
        response = requests.get(url)
        json_data = response.json()
        return Response(
            json.dumps(json_data, ensure_ascii=False),
            mimetype='application/json'
        )
    except Exception as e:
        return Response(
            json.dumps({"error": str(e)}, ensure_ascii=False),
            status=500,
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
