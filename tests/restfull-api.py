from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students/", methods=['GET'])
def hello():
    return jsonify({'urls' : [s.get_url() for s in Student.query.all()]})

if __name__ == "__main__":
    app.run(debug=True)