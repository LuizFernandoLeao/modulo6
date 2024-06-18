from tensorflow.keras.models import load_model # type: ignore
import cv2
import numpy as np

# Carrega o modelo linear
modelo = load_model('modelo_mnist_linear.h5')

# O modelo faz a predição
def predict_linear():
    img = cv2.imread('./upload/number.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28,28))
    img = img / img.max()
    img = img.reshape(1, 28 * 28) 
    predicao = modelo.predict(img)
    resultado = np.argmax(predicao)
    print(resultado)
    print(predicao)
    return resultado