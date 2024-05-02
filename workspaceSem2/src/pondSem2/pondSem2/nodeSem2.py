from rclpy.node import Node
from turtlesim.srv import SetPen, Spawn, Kill
from geometry_msgs.msg import Twist
import rclpy
import time

class Turtle(Node):

    #Define a função de SetPen, Spawn, Kill e as características do desenho
    def __init__(turtle):
        super().__init__('turtle')
        turtle.publisher_ = turtle.create_publisher(Twist, 'turtle1/cmd_vel', 15)
        turtle.timer_ = turtle.create_timer(1, turtle.draw_square)
        turtle.pen_client = turtle.create_client(SetPen, '/turtle1/set_pen')
        turtle.spawn_client = turtle.create_client(Spawn, 'spawn')
        turtle.kill_client = turtle.create_client(Kill, 'kill')
        turtle.twist_msg_ = Twist()
        turtle.start_time = time.time()  
        turtle.color_changed = False
        turtle.side_length = 1.0  


    #Define a função que desenha a espiral
    def draw_square(turtle):
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - turtle.start_time
        turtle.twist_msg_.linear.x = turtle.side_length*0.7
        turtle.twist_msg_.angular.z = 3.5  
        turtle.publisher_.publish(turtle.twist_msg_)
        turtle.side_length += 1

        # A tartaruga some após 9 segundos
        if tempo_decorrido > 9:
            turtle.stop()
        
        # As cores mudam de 3 em 3 segundos e seguindo um padrão "RGB"
        elif tempo_decorrido <= 3:
            turtle.red()
        elif tempo_decorrido <= 6:
            turtle.twist_msg_.angular.z = 2.5  
            turtle.publisher_.publish(turtle.twist_msg_)
            turtle.green()
        elif tempo_decorrido <= 9:
            turtle.twist_msg_.angular.z = 1.5  
            turtle.publisher_.publish(turtle.twist_msg_)
            turtle.blue()

    
    #Define cores do desenho
    #Red
    def red(turtle):
        request = SetPen.Request()
        request.r = 100  
        request.g = 10    
        request.b = 10    
        request.width = 3

        future = turtle.pen_client.call_async(request)

    #Green
    def green(turtle):
        request = SetPen.Request()
        request.r = 10  
        request.g = 100    
        request.b = 10    
        request.width = 6

        future = turtle.pen_client.call_async(request)

    #Blue
    def blue(turtle):
        request = SetPen.Request()
        request.r = 10  
        request.g = 10    
        request.b = 100    
        request.width = 9

        future = turtle.pen_client.call_async(request)
    
    #Para a tartaruga
    def stop(turtle):
        turtle.twist_msg_.linear.x = 0.0
        turtle.twist_msg_.angular.z = 0.0
        turtle.publisher_.publish(turtle.twist_msg_)
        request = Kill.Request()
        request.name = 'turtle1' 

        turtle.kill_client.call_async(request)

#Define a função de init, spin e shutdown
def main(args=None):
    rclpy.init(args=args)
    turtle1_controller = Turtle()
    rclpy.spin(turtle1_controller)
    turtle1_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()