from flask import  Flask,request,jsonify, send_file
from werkzeug.utils import secure_filename
from PIL import Image
from shortuuid import uuid
import os

app=Flask(__name__)

@app.get("/")
def index():

    return {"state":"okey"}

#images API
@app.get('/images/<filename>')
def getImage(filename):
    try:
        return send_file(f"images/{filename}")
    except:
        return jsonify(message="no such file")

@app.post("/images")
def imageUpload():
    try:
        file=request.files['image']
        image=Image.open(file)
        image=image.resize((320,240))
        filename = secure_filename(file.filename)
        ext=filename.rsplit('.',1)[1]
        name=uuid()
        filename=name+'.'+ext
        image.save("images/"+filename)

        return jsonify(message="uploaded file successfully",filename=filename)
    except Exception as e:
        return jsonify(message="failed to uplaod", error=str(e)),406

@app.delete('/images/<filename>')
def deleteImage(filename):
    try:
        os.remove(f"images/{filename}")

        return jsonify(message="delete image successfuly"),200

    except Exception as e:
        return jsonify(message="failed to delete", error=str(e)),406


#pdfs API
@app.get('/pdfs/<filename>')
def getPdf(filename):
    try:
        return send_file(f"pdfs/{filename}")
    except:
        return jsonify(message="no such file")

@app.post('/pdfs')
def pdfUpload():
    try:
        file=request.files['pdf']
        filename=secure_filename(file.filename)
        filename=uuid()+".pdf"
        file.save("pdfs/"+filename)

        return jsonify(message="file saved sucessfuly",filename=filename)
        
    except Exception as e:
        return jsonify(message="failed to uplaod", error=str(e)),406

@app.delete('/pdfs/<filename>')
def deletePdf(filename):
    try:
        os.remove(f"pdfs/{filename}")

        return jsonify(message="delete pdf successfuly"),200

    except Exception as e:
        return jsonify(message="failed to delete", error=str(e)),406

