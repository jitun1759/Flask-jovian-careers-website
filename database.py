from sqlalchemy import create_engine, text
# engine = create_engine("mysql+pymysql://user:pass@hostname/dbname")
connection_string = "mysql+pymysql://root:mysql@localhost:3306/jovian" #using My SQL workbench
engine = create_engine(connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append({'id': row[0], 'title': row[1], 'location': row[2], 'salary': row[3],
                         'currency': row[4], 'responsibilities': row[5], 'requirements': row[6],
                         'created_at': row[7], 'updated_at': row[8]})
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {'id': id})
        row = result.fetchone()
        if row:
            return {
                'id': row[0],
                'title': row[1],
                'location': row[2],
                'salary': row[3],
                'currency': row[4],
                'responsibilities': row[5],
                'requirements': row[6],
                'created_at': row[7],
                'updated_at': row[8]
            }
        else:
            return None

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)"
                     " VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        params = {
            'job_id': job_id,
            'full_name': data.get('full_name'),
            'email': data.get('email'),
            'linkedin_url': data.get('linkedin_url'),
            'education': data.get('education'),
            'work_experience': data.get('work_experience'),
            'resume_url': data.get('resume_url')
        }
        try:
            conn.execute(query, params)
            conn.commit()
            print("Data inserted successfully")
        except Exception as e:
            print("Error occurred:", e)
