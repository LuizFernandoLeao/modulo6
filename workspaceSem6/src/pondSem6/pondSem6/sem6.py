import typer
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from pynput import keyboard
from std_srvs.srv import Empty

#Cria a interface do usuário
app = typer.Typer()

class TurtleBot(Node):

    #Define a função de inicialização do robô
    def __init__(robo):
        super().__init__('turtlebot')
        print("Aguarde...")
        robo.connected = True
        robo.publisher_ = robo.create_publisher(Twist, 'cmd_vel', 50)
        robo.linear_speed = 3.0
        robo.angular_speed = 3.0
        robo.tecla_listener = keyboard.Listener(on_press=robo.on_press, on_release=robo.on_release)
        robo.tecla_listener.start()
        robo.current_linear = Vector3(x=0.0)
        robo.current_angular = Vector3(z=0.0)
        robo.create_timer(0.1, robo.display_status)

    #Define a função para movimentar e para o robô a partir de teclas do computador
    def on_press(robo, tecla):
        try:
            if tecla.char == 'w':
                robo.current_linear.x = robo.linear_speed
            elif tecla.char == 's':
                robo.current_linear.x = -robo.linear_speed
            elif tecla.char == 'a':
                robo.current_angular.z = robo.angular_speed
            elif tecla.char == 'd':
                robo.current_angular.z = -robo.angular_speed
            elif tecla.char == 'q':
                robo.emergency_stop()
                robo.connected = False
                robo.stop_robot_client()

        except AttributeError:
            pass
        robo.update_movement()

    #Define a função de parar o robô quando a tecla é solta
    def on_release(robo, tecla):
        try:
            if tecla.char in ['w', 's']:
                robo.current_linear.x = 0.0
            elif tecla.char in ['a', 'd']:
                robo.current_angular.z = 0.0
        except AttributeError:
            pass
        robo.update_movement()
    
    #Define a função da atualização sobre o movimento do robô
    def update_movement(robo):
        msg = Twist()
        msg.linear = robo.current_linear
        msg.angular = robo.current_angular
        robo.publisher_.publish(msg)

    #Define a função da parada de emergência
    def emergency_stop(robo):
        robo.current_linear = Vector3(x=0.0)
        robo.current_angular = Vector3(z=0.0)
        robo.update_movement()

    #Define a função de exibição dos dados do robô em tempo real
    def display_status(robo):
        #Comando para limpar o terminal enquanto o sitema funciona
        print("\033c", end="")
        print(f"O robô foi iniciado com sucesso. O robô está apto e disponível para receber suas mensagens: {robo.connected}.")
        print("\nMovimentação do robô")
        print("    W - Frente")
        print("    A - Esquerda")
        print("    S - Trás")
        print("    D - Direita")
        print("Pressione 'Q' para parar o robô e sair.")
        print("\nDados do robô em tempo real:")
        connection_status = "Conectado" if robo.connected else "Não Conectado"
        print(f"  Conexão: {connection_status}")
        print(f"  Velocidade Linear: {robo.current_linear.x}")
        print(f"  Velocidade Angular: {robo.current_angular.z}")

    # Função para chamar o serviço de parar o robô
    def stop_robot_client(robo):
        print("Chamando o serviço para parar o robô...")
        client = robo.create_client(Empty, 'stop_robot')
        if client.wait_for_service(timeout_sec=0.1):
            request = Empty.Request()
            future = client.call_async(request)
            rclpy.spin_until_future_complete(robo, future)
            robo.get_logger().info('Serviço chamado com sucesso.')
        else:
            robo.get_logger().info('Serviço não disponível.')
        robo.destroy_node()
        rclpy.shutdown()
        exit()


# Função principal para inicializar o robô e controlá-lo
def main():
    print("Aguarde...")
    rclpy.init(args=None)
    robot = TurtleBot()
    rclpy.spin(robot)

# Função para chamar o app ao rodar o pacote 
if __name__ == "__main__":
    main()