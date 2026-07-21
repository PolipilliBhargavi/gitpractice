from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)
@app.route('/' , methods =['GET'])
def home():   
    return jsonify({"message": "Application running!"}), 200
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0"
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug = True)

