# Modify the Flask App ('app.py'):
from flask import Flask, request, render_template
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.calculatorDB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            value1 = float(request.form['value1'])
            value2 = float(request.form['value2'])
            operator = request.form['operator']
            result = calculate(value1, value2, operator)

            # Insert the calculation into MongoDB
            db.calculations.insert_one({
                'value1': value1,
                'value2': value2,
                'operator': operator,
                'result': result,
                'timestamp': datetime.datetime.now()
            })
        except ValueError:
            result = "Invalid input"
        except Exception as e:
            result = str(e)
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

# check validity