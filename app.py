from flask import jsonify
from main import app
from business.routes import business,db
from products.routes import products,db
from users.routes import users,db
from orders.routes import orders,db

app.register_blueprint(blueprint=products)
app.register_blueprint(blueprint=business)
app.register_blueprint(blueprint=users)
app.register_blueprint(blueprint=orders)

@app.route('/')
def healthCheck():

    return jsonify(message="application running successfully !")

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)