from flask import Flask, request, jsonify, render_template
from loglens.parsers.auth_parser import AuthParser
from loglens.analyzers.stats import summary
from loglens.analyzers.detections import run_all_detections

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze_logs():

    """
    Accept a log file and returns listed analysis in JSON. 
    """ 

    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400


    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    try:
        content = file.read().decode("utf-8")

        lines = content.splitlines()

        parser = AuthParser()
        events = []
        for line in lines:

            event = parser.parse_line(line)
            if event:
                events.append(event)
        stats_report=summary(events)
        detections_report = run_all_detections(events)

        report = {
        "summary": stats_report,
        "detections": detections_report
        }

        return jsonify(report)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


