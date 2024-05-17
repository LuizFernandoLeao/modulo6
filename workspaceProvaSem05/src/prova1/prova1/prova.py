from rclpy.node import Node
from turtlesim.srv import SetPen, Spawn, Kill
from geometry_msgs.msg import Twist
import rclpy
import time
import typer
from InquirerPy.resolver import prompt
from InquirerPy.utils import InquirerPyKeybindings

app = typer.Typer()

def show_menu():
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': ['front', 'back', 'left', 'right', 'exit', 'stop'],
        },
    ]

    keybindings: InquirerPyKeybindings = {
        "interrupt": [{"key": "q"}, {"key": "c-c"}],
    }

    try:
        return prompt(questions, keybindings=keybindings)['action']
    except KeyboardInterrupt:
        return 'panic'


class Turtle(Node):

    #Define a função de SetPen, Spawn, Kill e as características do desenho
    def __init__(turtle):
        super().__init__('turtle')
        turtle.publisher = turtle.create_publisher(Twist, 'turtle1/cmd_vel', 15)




#Define a função main do nó
def main(args=None):
    rclpy.init(args=args)
    turtle = Turtle()

    while True:
        action = show_menu()
        match action:
            case 'vx':
                print("Escreva a velocidade da tartaruga em x")
                turtle.vx(1.0)
            case 'vy':
                print("Escreva a velocidade da tartaruga em y")
                turtle.vy(0.5)
            case 'vtheta':
                print("Escreva a velocidade angular da tartaruga")
                turtle.vtheta(0.2)
            case 'tempo_em_ms':
                print("Escreva o tempo em que a tartaruga deve executar o comando")
                turtle.tempo_em_ms(2000)

if __name__ == '__main__':
    main()