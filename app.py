# app.py

from flask import Flask, render_template, request
from feeds.remoteok import get_remoteok_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    if request.method == "POST":
        keywords_input = request.form.get("keywords", "")
        keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
        jobs = get_remoteok_jobs(keywords)
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
