from rclpy.node import Node
from turtlesim.srv import SetPen, Spawn, Kill
from geometry_msgs.msg import Twist
import rclpy
import time

class Turtle(Node):

    #Define a função de SetPen, Spawn, Kill e as características do desenho
    def __init__(turtle):
        super().__init__('turtle')
        turtle.pen = turtle.create_client(SetPen, '/turtle1/set_pen')
        turtle.spawn = turtle.create_client(Spawn, 'spawn')
        turtle.kill = turtle.create_client(Kill, 'kill')
        turtle.publisher = turtle.create_publisher(Twist, 'turtle1/cmd_vel', 15)
        turtle.timer = turtle.create_timer(1, turtle.draw_square)
        turtle.twist = Twist()
        turtle.start = time.time()  
        turtle.color = False
        turtle.side_length = 1.0  


    #Define a função que desenha a espiral
    def draw_square(turtle):
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - turtle.start
        turtle.twist.linear.y = turtle.side_length*0.6
        turtle.twist.angular.z = - 3.5  
        turtle.publisher.publish(turtle.twist)
        turtle.side_length += 1

        #A tartaruga some após 9 segundos
        if tempo_decorrido > 9:
            turtle.stop()
        
        #As cores mudam de 3 em 3 segundos e seguindo um padrão "RGB"
        elif tempo_decorrido <= 3:
            turtle.red()
        elif tempo_decorrido <= 6:
            turtle.twist.angular.z = - 3.0  
            turtle.publisher.publish(turtle.twist)
            turtle.green()
        elif tempo_decorrido <= 9:
            turtle.twist.angular.z = - 2.5  
            turtle.publisher.publish(turtle.twist)
            turtle.blue()

    
    #Define cores do desenho
    #Red
    def red(turtle):
        request = SetPen.Request()
        request.r = 100  
        request.g = 10    
        request.b = 10    
        request.width = 3

        future = turtle.pen.call_async(request)

    #Green
    def green(turtle):
        request = SetPen.Request()
        request.r = 10  
        request.g = 100    
        request.b = 10    
        request.width = 6

        future = turtle.pen.call_async(request)

    #Blue
    def blue(turtle):
        request = SetPen.Request()
        request.r = 10  
        request.g = 10    
        request.b = 100    
        request.width = 9

        future = turtle.pen.call_async(request)
    
    #Para a tartaruga
    def stop(turtle):
        turtle.twist.linear.y = 0.0
        turtle.twist.angular.z = 0.0
        turtle.publisher.publish(turtle.twist)
        request = Kill.Request()
        request.name = 'turtle1' 
        turtle.kill.call_async(request)

#Define a função main do nó
def main(args=None):
    rclpy.init(args=args)
    turtle1_controller = Turtle()
    rclpy.spin(turtle1_controller)
    turtle1_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()