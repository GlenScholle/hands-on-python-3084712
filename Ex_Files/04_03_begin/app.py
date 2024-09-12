import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    # Your code here!
    search_string = request.args.get("surname").lower().strip()

    for l in laureates:
        if search_string in l["surname"].lower():
            results.append(l)

    return jsonify(results)


app.run(debug=True)
