from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import random
from faker import Faker

app = Flask(__name__)


fake = Faker()
categories = ['Groceries', 'Rent', 'Transportation', 'Entertainment', 'Education', 'Utilities', 'Miscellaneous']

def generate_student_expenses(num_entries):
    student_expenses = []
    for _ in range(num_entries):
        student = {
            'name': fake.name(),
            'age': random.randint(18, 25),  
            'income': random.randint(20000, 50000),  
            'expenses': {}
        }

        for category in categories:
            student['expenses'][category] = random.randint(1000, 10000)  

        student_expenses.append(student)
    return student_expenses


students = generate_student_expenses(100)


data = []
for student in students:
    student_data = {
        'name': student['name'],
        'age': student['age'],
        'income': student['income'],
        'groceries': student['expenses']['Groceries'],
        'rent': student['expenses']['Rent'],
        'transportation': student['expenses']['Transportation'],
        'entertainment': student['expenses']['Entertainment'],
        'education': student['expenses']['Education'],
        'utilities': student['expenses']['Utilities'],
        'miscellaneous': student['expenses']['Miscellaneous']
    }
    data.append(student_data)

df = pd.DataFrame(data)


X = df[['age', 'income']]  
y = df['groceries']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    
    student_data = df.to_dict(orient='records')
    return render_template('index.html', students=student_data)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        income = int(request.form['income'])

        prediction = model.predict([[age, income]])[0]

        return render_template('predict.html', prediction=prediction, age=age, income=income)

    return render_template('predict.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)

