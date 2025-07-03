☕ Coffee Products API
A mini REST API built with Flask for managing a coffee product catalog, featuring reusable decorators for logging, timing, and simulating delays.

📁 Project Structure
bash
Copy
Edit
.
├── app.py                # Entry point: creates Flask app and registers the products blueprint.
├── decorators.py         # Custom decorators for logging, timing, and adding delay.
├── models.py             # Mock database and product-related operations.
└── routes.py             # Routes for product management (get & add).
🚀 Features
✅ Get coffee product details by name
✅ Add new coffee products with validation
✅ Reusable decorators:

log_call: logs every function call with arguments

timer: measures execution time

delay: simulates latency for realism
✅ Modular architecture with Flask Blueprints
✅ In-memory mock database

📦 Requirements
Python 3.8+

Install dependencies:

bash
Copy
Edit
pip install Flask
🏁 Running the Application
Start the server:

bash
Copy
Edit
python app.py
API will be available at http://127.0.0.1:5000.

🔗 API Endpoints
GET /products?name=<product_name>
Retrieve a coffee product by name.

Example request:

pgsql
Copy
Edit
GET /products?name=latte
Successful response:

json
Copy
Edit
{
  "data": {
    "name": "Latte",
    "price": 4.0
  }
}
Error responses:

Missing name → {"error": "product name is required"}

Non-string name → {"error": "product name must be a string"}

Nonexistent product → {"error": "product does not exist"}

POST /products/add
Add a new coffee product.

Request body (JSON):

json
Copy
Edit
{
  "name": "Black coffee",
  "cost": 2.75
}
Success: HTTP 200 with empty response.

Error responses:

Missing name → {"error": "product name is required"}

Existing product → {"error": "product already exists"}

Missing cost → {"error": "cost required"}

Invalid cost → {"error": "cost must be a number"}

📖 Example Mock Coffee Menu
Defined in models.py:

python
Copy
Edit
mock_products = {
    "espresso": {"name": "Espresso", "price": 2.50},
    "cappuccino": {"name": "Cappuccino", "price": 3.50},
    ...
}
⚙️ Decorators
All endpoints use these decorators:

log_call: logs every function call with arguments.

timer: logs execution time.

delay(rate=N): delays execution by N seconds.

✅ Notes
Product identifiers are the lowercase product names (e.g., "latte", "mocha").

Artificial delays simulate realistic response times.

Project uses a modular, maintainable Flask Blueprint structure.

🔥 License
This project is open-source for educational and demonstration purposes.
