from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'email': request.form['email']
        }
        return render_template('index.html', user=user_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


