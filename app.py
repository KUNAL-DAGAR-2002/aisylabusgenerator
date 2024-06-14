from flask import Flask, render_template, request, jsonify
from boltiotai import openai
app = Flask(__name__)

openai.api_key = 'UVO3uaZybJTl1ZjnKyA1yjVrNUpyfCvg-Rrn2UR-wYg'
def get_plan(subject,grade):
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant and I have good knowledge in teaching students and making session and syllabus plans for them from class nursery(play school) to college level."
        }, {
            "role": "user",
            "content": f'''Hey Please generate educational content for class {grade} and subject {subject}.
            Please ensure you will be covering these areas and generate output in the following manner:
            1. Objective of the Course: A concise statement that describes the purpose and goals of the course.
            2.Sample Syllabus: An AI-generated syllabus outline that covers the main topics and modules to be taught.
            3.Three Measurable Outcomes: Specific, measurable learning outcomes categorized according to Bloom's Taxonomy levels: Knowledge, Comprehension, and Application.
            4.Assessment Methods: Suggestions on how to evaluate the learning outcomes through various forms of assessment.
            5.Recommended Readings and Textbooks: A list of AI-recommended resources, including books, articles, and other materials relevant to the course content.
            
            Please generate a content that will cover all these 5 topics'''
        }]
    )

    # Extracting the content from the response
    content = response['choices'][0]['message']['content']
    
    return content

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit',methods=["GET","POST"])
def submit():
    data = request.json
    comp = list(data.values())[0]
    data = list(comp.values())
    subject = data[0]
    grade = data[1]
    print(f"The grade is {grade} and subject is {subject}")
    
    plan = get_plan(subject,grade)
    print(plan)
   
    
    return jsonify({'status':True,'plan':plan})
    
if __name__ == "__main__":
    app.run(port=5050,debug=True)