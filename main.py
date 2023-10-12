from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None

    # Check if a POST request is made (i.e., user submits a question)
    if request.method == 'POST':
        image = request.files['image']
        question = request.form['question']

        # You would pass the image and question to your VQA model here.
        # For now, just returning a dummy answer.
        answer = "This is a dummy answer for the question: " + question

    return render_template('home.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(500)  # catch internal server errors
def internal_server_error(e):
    return render_template('error.html', error=str(e)), 500