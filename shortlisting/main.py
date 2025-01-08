from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

@app.route("/")
def matchresume():
    return render_template('match.html')

@app.route('/match', methods=['POST'])
def match():
    if request.method == 'POST':
        job_description_file = request.files.get('job_description_file')
        resume_files = request.files.getlist('resumes')
        qualifying_score = float(request.form.get('qualifying_score', 55))

        if not job_description_file or not resume_files:
            return render_template('match.html', message="Please upload a job description and resumes.")

        # Extract text from job description file
        job_description_path = os.path.join(app.config['UPLOAD_FOLDER'], job_description_file.filename)
        job_description_file.save(job_description_path)
        job_description = extract_text(job_description_path)

        # Extract text from resumes
        resumes = []
        filenames = []
        for resume_file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            resumes.append(extract_text(filename))
            filenames.append(resume_file.filename)

        # Vectorize job description and resumes
        vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
        vectors = vectorizer.toarray()

        # Calculate cosine similarities
        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity([job_vector], resume_vectors)[0]

        # Filter resumes based on the qualifying score
        shortlisted_resumes = []
        unmatched_resumes = []

        job_keywords = set(job_description.split())
        for i, score in enumerate(similarities):
            if score * 100 >= qualifying_score:
                shortlisted_resumes.append((filenames[i], round(score * 100, 2)))
            else:
                resume_keywords = set(resumes[i].split())
                missing_keywords = job_keywords - resume_keywords
                reason = f"Low similarity score. Missing keywords: {', '.join(missing_keywords)}"
                unmatched_resumes.append((filenames[i], round(score * 100, 2), reason))

        total_resumes = len(filenames)
        print('total resumes ',total_resumes)

        return render_template(
            'match.html',
            message="Resume matching completed.",
            shortlisted_resumes=shortlisted_resumes,
            unmatched_resumes=sorted(unmatched_resumes, key=lambda x: x[1], reverse=True),
            qualifying_score=qualifying_score,
            total_resumes=total_resumes
        )

    return render_template('match.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
