import os 
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from modelo import predict
from modelo_linear import predict_linear


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    resultado = predict()
    return render_template('resultado.html', resultado = resultado)

@app.route("/upload_linear", methods=['POST'])
def upload_linear():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    resultado = predict_linear()
    return render_template('resultado.html', resultado = resultado)


if __name__ == '__main__':
    app.run(debug=True)