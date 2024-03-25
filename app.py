# Modify the Flask App ('app.py'):
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value1 = int(request.form['value1'])
        value2 = int(request.form['value2'])
        operator = request.form['operator']
        result = calculate(value1, value2, operator)
        return render_template('index.html', result=result)
    return render_template('index.html')

def calculate(value1, value2, operator):
        if operator == '+':
            return value1 + value2
        elif operator == '-':
            return value1 - value2
        elif operator == '*':
            return value1 * value2 
        elif operator == '/':
            if value2 != 0:
                return value1 / value2
        else:
            return "Error: Division by zero"
    

if __name__ == '__main__':
    app.run(debug=True)


