from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 10,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Scientist',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 15,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Python Developer',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 20,00,000'
#     },
#     {
#         'id': 4,
#         'title': 'Fullstock Develover',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 25,00,000'
#     }
# ]

# def load_jobs_form_db():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from jobs"))
#         jobs = []
#         for row in result.all():
#             jobs.append({'id': row[0], 'title': row[1], 'location': row[2], 'salary': row[3]})
#         return jobs

# @app.route("/", methods=['POST'])
@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    # return jsonify(job)
    print(job)
    return render_template('jobpage.html', job=job)



@app.route("/job/<id>/apply", methods = ['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    # return jsonify(data)
    return render_template('application_submitted.html', application=data, job=job)
if __name__ == '__main__':
    app.run(debug=True)
