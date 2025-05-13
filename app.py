from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/control", methods=["POST"])
def control():
    action = request.form["action"]
    if action == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif action == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
