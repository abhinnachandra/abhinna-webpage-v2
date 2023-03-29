from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Manager',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 25,000'
}, {
  'id': 2,
  'title': 'Senior Consultant',
  'location': 'Delhi, India',
  'salary': 'Rs. 35,000'
}, {
  'id': 3,
  'title': 'Consultant',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Trainee Consultant',
  'location': 'San Francisco, USA',
  'salary': 'INR 15,000'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Abhinna')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
