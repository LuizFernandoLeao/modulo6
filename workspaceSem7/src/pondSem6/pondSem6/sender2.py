import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import os
from datetime import datetime

class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(CompressedImage, '/video_frames', 10)
        self.timer = self.create_timer(0.02, self.timer_callback)  # Publish every 0.02 seconds (50 Hz)
        self.cap = cv2.VideoCapture(0)
        self.image_save_path = 'saved_images'
        if not os.path.exists(self.image_save_path):
            os.makedirs(self.image_save_path)
        self.frame_count = 0

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # Encode frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            msg = CompressedImage()
            msg.format = "jpeg"
            msg.data = buffer.tobytes()
            self.publisher_.publish(msg)
            
            # Save the image every 100 frames
            self.frame_count += 1
            if self.frame_count % 100 == 0:
                self.save_image(frame)

    def save_image(self, frame):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(self.image_save_path, f'frame_{timestamp}.jpg')
        cv2.imwrite(filename, frame)
        self.get_logger().info(f'Image saved: {filename}')

def main(args=None):
    rclpy.init(args=args)
    webcam_publisher = WebcamPublisher()
    rclpy.spin(webcam_publisher)
    webcam_publisher.destroy_node()
    rclpy.shutdown()

cap = cv2.VideoCapture(0)
while True:
    # Captura o quadro
    ret, frame = cap.read()
        
    # Verifica se a captura foi bem-sucedida
    if not ret:
        break
        
    # Exibe o quadro em uma janela
    cv2.imshow('Webcam', frame)
        
    # Aguarda a tecla 'x' para sair
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Libera a captura e fecha as janelas
cap.release()
cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
