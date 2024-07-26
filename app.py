from flask import Flask, render_template
import json

app = Flask(__name__)    

@app.route('/')
def jobs():
    with open("jobs.json", "r") as jobs_file:
        jobs = json.load(jobs_file)
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)
