from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    rollno = request.form['rollno']
    email = request.form['email']
    year = request.form['year']
    return render_template('result.html', username=username, rollno=rollno, email=email, year=year)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
