from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

sensor_value = 1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sensor", methods=["POST"])
def sensor():
    global sensor_value

    data = request.get_json()

    if data and "value" in data:
        sensor_value = data["value"]

    return jsonify({
        "success": True,
        "value": sensor_value
    })


@app.route("/value")
def value():
    return jsonify({
        "value": sensor_value
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)