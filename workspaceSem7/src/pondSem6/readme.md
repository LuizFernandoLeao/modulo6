# Ponderada Semana 6 - Luiz Fernando Leão

## Objetivo

&emsp;O objetivo da atividade é fazer um setup de interação com o turtlebot, compreendendo os conceitos básico para uso do ROS em rede e dos pacotes para interação com o robô.

&emsp;Na atividade, foi preciso desenvolver uma interface de usuário para detectar os botões pressionados pelo usuário e dar um feedback da velocidade do robô em tempo real. Também, um nó de ROS 2 foi feito com a capacidade de comandar o robô e que seja capaz de verificar se o robô está inicializado e disponível para receber suas mensagens antes de enviá-las.

## Instalação

&emsp;Para inicializar o projeto no computador, realize os seguintes passos:

1. Clone este repositório em sua máquina, abra o terminal e navegue até a pasta em que o repositório será clonado, e digite:

    ```console
    git clone https://github.com/LuizFernandoLeao/modulo6
    ``` 

2. Navegue até onde a pasta foi criada e digite o seguinte comando para acessar a pasta raíz do workspace:

    ```console
    cd workspaceSem6/src
    ``` 

3. Agora é preciso contruir o pacote, para que o programa tenha as dependências necessárias para funcionar:

   ```console
    colcon build
    ``` 

4. Faça a instalação do setup:

    ```console
	. install/setup.bash
    ``` 

5. Abra um segundo terminal e rode o seguinte comando, para que o ambiente em que o robô funcionará apareça: 

    ```console
	ros2 launch webots_ros2_turtlebot robot_launch.py
    ``` 

6. Finalmente, retorne ao primeiro terminal e rode o nó em que possui o funcionamento do robô: 

    ```console 
    ros2 run pondSem6 sem6 
    ``` 
## Demonstração

&emsp;Para demonstrar o funcionamento da atividade, um vídeo foi criado demonstrando o sistema.

&emsp;<a href="https://www.youtube.com/watch?v=B1PH7GKhZqo">LINK DO VÍDEO</a>

&emsp;No vídeo, é possível ver a inicialização do sistema, em que informa o usuário de o sistema foi iniciado corretamente e se está apto para receber mensagens. Também, é possível utilizar as teclas do computador para controlar o robô, e ter uma resposta deste controle em tempo real.

&emsp;Vale destacar que a solução desta atividade foi altamente inspirada na solução do projeto em grupo. Segue o link como referência para o repositório do grupo: https://github.com/Inteli-College/2024-1b-t08-ec06-g01 . Além disso, sites de IA generativa como o ChatGPT foram utilizados, com a finalidade de ampliar os estudos sobre o assunto e aumentar a qualidade da entrega da atividade
