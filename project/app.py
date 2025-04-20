from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)
groceries = [
    {"name": "Apple", "price": 100, "photo": "images/Apple.avif"},
    {"name": "Banana", "price": 40, "photo": "images/Banana.avif"},
    {"name": "Bread", "price": 50, "photo": "images/Bread.avif"},
    {"name": "Broccoli", "price": 80, "photo": "images/Broccoli.jpg"},
    {"name": "Butter", "price": 120, "photo": "images/Butter.avif"},
    {"name": "Capsicum", "price": 60, "photo": "images/Capsicum.jpg"},
    {"name": "Carrot", "price": 35, "photo": "images/Carrot.avif"},
    {"name": "Cauliflower", "price": 70, "photo": "images/Cauliflower.jpg"},
    {"name": "Cheese", "price": 150, "photo": "images/Cheese.avif"},
    {"name": "Coffee", "price": 300, "photo": "images/Coffee.avif"},
    {"name": "Cooking Oil", "price": 180, "photo": "images/Cooking Oil.avif"},
    {"name": "Curd", "price": 60, "photo": "images/Curd.avif"},
    {"name": "Green Chilli", "price": 20, "photo": "images/Green Chilli.avif"},
    {"name": "Green Cucumber", "price": 25, "photo": "images/Green Cucumber.avif"},
    {"name": "Milk", "price": 55, "photo": "images/Milk.avif"},
    {"name": "Onion", "price": 30, "photo": "images/Onion.jpg"},
    {"name": "Orange", "price": 80, "photo": "images/Orange.avif"},
    {"name": "Paneer", "price": 160, "photo": "images/Paneer.avif"},
    {"name": "Potato", "price": 35, "photo": "images/Potato.avif"},
    {"name": "Rice", "price": 70, "photo": "images/Rice.avif"},
    {"name": "Salt", "price": 20, "photo": "images/Salt.avif"},
    {"name": "Sugar", "price": 45, "photo": "images/Sugar.avif"},
    {"name": "Tea", "price": 120, "photo": "images/Tea.avif"},
    {"name": "Tomato", "price": 40, "photo": "images/Tomato.avif"},
    {"name": "Wheat", "price": 50, "photo": "images/Wheat.avif"}
]
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Grocery Store</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #e0f7fa, #ffffff);
                min-height: 100vh;
                padding: 20px;
            }
            .card {
                transition: transform 0.3s;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            .card:hover {
                transform: scale(1.05);
            }
            .product-img {
                height: 200px;
                object-fit: cover;
            }
            #searchInput {
                max-width: 400px;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="container text-center">
            <h1 class="mb-4">🛒 Fresh Groceries</h1>
            <input type="text" id="searchInput" class="form-control mb-5" placeholder="Search for groceries...">
            <div class="row" id="groceryList">
                {% for item in groceries %}
                <div class="col-md-3 mb-4 grocery-item">
                    <div class="card">
                        <img src="{{ url_for('static', filename=item.photo) }}" class="card-img-top product-img" alt="{{ item.name }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ item.name }}</h5>
                            <p class="card-text">₹{{ item.price }}</p>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <script>
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('keyup', function() {
                let filter = searchInput.value.toLowerCase();
                let items = document.getElementsByClassName('grocery-item');

                Array.from(items).forEach(function(item) {
                    let name = item.getElementsByClassName('card-title')[0].innerText;
                    if (name.toLowerCase().includes(filter)) {
                        item.style.display = '';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        </script>
    </body>
    </html>
    ''', groceries=groceries)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = None
    if request.method == 'POST':
        income = float(request.form.get('income', 0))   
        prediction = income * 0.3
        result = f"Predicted monthly expense: ₹{prediction:.2f}"
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Expense Predictor</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #f9fbe7, #ffffff);
                min-height: 100vh;
                padding: 20px;
            }
            .card {
                max-width: 500px;
                margin: auto;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="text-center mb-4">Expense Predictor</h1>
            <div class="card">
                <form method="post">
                    <div class="mb-3">
                        <label for="income" class="form-label">Enter your monthly income (₹):</label>
                        <input type="number" step="0.01" class="form-control" id="income" name="income" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Predict</button>
                </form>
                {% if result %}
                <div class="alert alert-success mt-4">{{ result }}</div>
                {% endif %}
            </div>
        </div>
    </body>
    </html>
    ''', result=result)


  
                
                

if __name__ == '__main__':
    app.run(debug=True)

