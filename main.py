from flask import Flask, render_template, jsonify

#jsnoify helps represent dynamic data using an API via a JSON

app = Flask(__name__)  # create an object of the class

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Kathmandu',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Kathmandu',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'ML',
  'location': 'Remote',
  'salary': 'Rs. 20,00,000'
}, {
  'id': 4,
  'title': 'Backend',
  'location': 'SF, USA'
}]


@app.route("/")  #path of the url after the url
def hello_world():
  return render_template('home_css_bootstrap.html', jobs=JOBS)
  #render_template('home.html') # this was with original CSS that was manually input

@app.route("/api/jobs")
#put api before the page to differentiate between html and json
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
