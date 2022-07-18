from flask import jsonify
from main import app
from business.routes import business

app.register_blueprint(blueprint=business)

@app.route('/')
def healthCheck():

    return jsonify(message="application running successfully !")

if __name__=="__main__":
    app.run(debug=True)