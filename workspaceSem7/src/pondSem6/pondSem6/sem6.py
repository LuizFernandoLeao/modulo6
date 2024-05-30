from sensor_msgs.msg import CompressedImage
import cv2
import os
from datetime import datetime
import typer
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from pynput import keyboard
from std_srvs.srv import Empty

# Cria a interface do usuário
app = typer.Typer()

class TurtleBot(Node):

    #Define a função de inicialização do robô
    def __init__(self):
        super().__init__('turtlebot')
        print("Aguarde...")
        self.connected = True
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 50)
        self.linear_speed = 3.0
        self.angular_speed = 3.0
        self.tecla_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.tecla_listener.start()
        self.current_linear = Vector3(x=0.0)
        self.current_angular = Vector3(z=0.0)
        self.create_timer(0.1, self.display_status)
        
        # Adiciona configuração para a câmera
        self.camera_publisher_ = self.create_publisher(CompressedImage, '/video_frames', 10)
        self.camera_timer = self.create_timer(0.02, self.camera_timer_callback)  # Publish every 0.02 seconds (50 Hz)
        self.cap = cv2.VideoCapture(0)
        self.frame_count = 0

    #Define a função para movimentar e para o robô a partir de teclas do computador
    def on_press(self, tecla):
        try:
            if tecla.char == 'w':
                self.current_linear.x = self.linear_speed
            elif tecla.char == 'a':
                self.current_angular.z = self.angular_speed
            elif tecla.char == 's':
                self.current_linear.x = -self.linear_speed
            elif tecla.char == 'd':
                self.current_angular.z = -self.angular_speed
            elif tecla.char == 'q':
                self.emergency_stop()
                self.connected = False
                self.stop_robot_client()

        except AttributeError:
            pass
        self.update_movement()

    #Define a função de parar o robô quando a tecla é solta
    def on_release(self, tecla):
        try:
            if tecla.char in ['w', 's']:
                self.current_linear.x = 0.0
            elif tecla.char in ['a', 'd']:
                self.current_angular.z = 0.0
        except AttributeError:
            pass
        self.update_movement()
    
    #Define a função da atualização sobre o movimento do robô
    def update_movement(self):
        msg = Twist()
        msg.linear = self.current_linear
        msg.angular = self.current_angular
        self.publisher_.publish(msg)

    #Define a função da parada de emergência
    def emergency_stop(self):
        self.current_linear = Vector3(x=0.0)
        self.current_angular = Vector3(z=0.0)
        self.update_movement()

    #Define a função de exibição dos dados do robô em tempo real
    def display_status(self):
        #Comando para limpar o terminal enquanto o sitema funciona
        print("\033c", end="")
        print(f"O robô foi iniciado com sucesso. O robô está apto e disponível para receber suas mensagens: {self.connected}.")
        print("\nMovimentação do robô")
        print("    W - Frente")
        print("    A - Esquerda")
        print("    S - Trás")
        print("    D - Direita")
        print("Pressione 'Q' para parar o robô e sair.")
        print("\nDados do robô em tempo real:")
        connection_status = "Conectado" if self.connected else "Não Conectado"
        print(f"  Conexão: {connection_status}")
        print(f"  Velocidade Linear: {self.current_linear.x}")
        print(f"  Velocidade Angular: {self.current_angular.z}")

    #Define a função de encerramento da operação do robô
    def stop_robot_client(self):
        print("Chamando o serviço para parar o robô...")
        client = self.create_client(Empty, 'stop_robot')
        if client.wait_for_service(timeout_sec=0.1):
            request = Empty.Request()
            future = client.call_async(request)
            rclpy.spin_until_future_complete(self, future)
            self.get_logger().info('Serviço chamado com sucesso.')
        else:
            self.get_logger().info('Serviço não disponível.')
        self.destroy_node()
        rclpy.shutdown()
        exit()

    #Define a função de captura de imagem da câmera
    def camera_timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            msg = CompressedImage()
            msg.format = "jpeg"
            msg.data = buffer.tobytes()
            self.camera_publisher_.publish(msg)
            
def main(args=None):
    print("Aguarde...")
    rclpy.init(args=args)
    robot = TurtleBot()
    rclpy.spin(robot)
    robot.cap.release()  #A camera é liberada
    cv2.destroyAllWindows()
    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
