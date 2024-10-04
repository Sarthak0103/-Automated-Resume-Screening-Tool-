from flask import Flask, request, render_template
import spacy

# Load the small English NLP model
nlp = spacy.load('en_core_web_sm')

# Now you can proceed with your NLP tasks


app = Flask(__name__, template_folder='ht')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/screen', methods=['POST'])
def screen_resume():
    resume_text = request.form['resume']
    job_description = request.form['job_description']
    
    # Use NLP model to score the resume against the job description
    score, matched_keywords = nlp.score_resume(resume_text, job_description)
    
    return render_template('index.html', score=score, matched_keywords=matched_keywords)

if __name__ == "__main__":
    app.run(debug=True)
