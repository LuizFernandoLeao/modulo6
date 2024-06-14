import cv2

# Carregar o classificador pré-treinado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializar a captura de vídeo
cap = cv2.VideoCapture('la_cabra.mp4')

while True:
    # Ler um frame do vídeo
    ret, frame = cap.read()
    
    # Se não conseguiu ler o frame, sair do loop
    if not ret:
        break
    
    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Desenhar retângulos em torno dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Mostrar o frame resultante
    cv2.imshow('Video', frame)
    
    # Esperar por 1 ms e sair se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura de vídeo e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
