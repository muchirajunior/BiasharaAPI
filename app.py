from flask import jsonify
from main import app
from business.routes import business
from products.routes import products
from users.routes import users
from orders.routes import orders

app.register_blueprint(blueprint=products)
app.register_blueprint(blueprint=business)
app.register_blueprint(blueprint=users)
app.register_blueprint(blueprint=orders)

@app.route('/')
def healthCheck():

    return jsonify(message="application running successfully !")

if __name__=="__main__":
    app.run(debug=True)