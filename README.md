# Automated Resume Matching System

## Overview

The Automated Resume Matching System is a Flask-based web application designed to streamline the recruitment process by matching candidate resumes with job descriptions. Leveraging Natural Language Processing (NLP) techniques such as TF-IDF vectorization and cosine similarity, the system automates resume screening, helping recruiters efficiently identify the best candidates for a job.

---

## Features

- **Upload and Process Files:** Supports PDF, DOCX, and TXT file formats for both job descriptions and resumes.
- **Text Extraction:** Extracts text content from uploaded files.
- **Similarity Calculation:** Uses TF-IDF and cosine similarity to compute the relevance of resumes to the job description.
- **Shortlisting Candidates:** Filters resumes based on a user-defined qualifying score.
- **Feedback on Mismatches:** Provides reasons for unmatched resumes, highlighting missing keywords.
- **Intuitive Web Interface:** User-friendly HTML templates for file uploads and displaying results.

---

## Technologies Used

- **Backend Framework:** Flask
- **NLP Libraries:**
  - scikit-learn (TF-IDF vectorization, cosine similarity)
  - PyPDF2 (PDF text extraction)
  - docx2txt (DOCX text extraction)
- **Frontend:** HTML and Jinja2 templates
- **Programming Language:** Python
- **Deployment:** Local environment (Flask development server)

---

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd automated-resume-matching-system
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create an `uploads/` directory in the project root to store uploaded files:
   ```bash
   mkdir uploads
   ```

4. Run the Flask development server:
   ```bash
   python app.py
   ```

5. Open the application in a web browser:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Navigate to the homepage.
2. Upload a job description file.
3. Upload one or more resume files.
4. Set a qualifying score (default is 55%).
5. Click the "Match Resumes" button.
6. View the results, including:
   - Shortlisted resumes with their matching scores.
   - Unmatched resumes with reasons for rejection.

---

## Folder Structure

```
|-- app.py                   # Main application file
|-- requirements.txt         # Python dependencies
|-- templates/               # HTML templates for the web interface
|-- static/                  # Static files (CSS, JS, images)
|-- uploads/                 # Temporary storage for uploaded files
```

---

## Limitations

- Limited to PDF, DOCX, and TXT file formats.
- Relies heavily on keyword matching, which may overlook semantic context.
- Performance may degrade when processing a large number of resumes.

---

## Future Enhancements

- Implement semantic analysis using Word2Vec or BERT.
- Expand support to additional file formats.
- Optimize performance for large-scale usage.
- Integrate with external Applicant Tracking Systems (ATS).

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or support, please contact:

- **Name:** Arif Khan
- **Email:** auzrimfa@gmail.com
- **GitHub:** https://github.com/Arifkhan71
