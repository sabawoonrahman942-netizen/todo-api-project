from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Linux öğren", "done": False},
    {"id": 2, "task": "Docker öğren", "done": True}
]

@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD test başarılı"
    })

@app.route("/todos")
def get_todos():
    return jsonify(todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
