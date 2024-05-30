# Ponderada Semana 7 - Luiz Fernando Leão

## Objetivo

&emsp;O objetivo da atividade é incrementar o sistema do turtlebot teleoperado (da atividade ponderada anterior) para incluir conceitos de streaming de imagens.

&emsp;Na atividade, foi preciso revisar a implementação original do turtlebot teleoperado, modificar a interface de usuário para que exiba a imagem transmitida e criar o código necessário para transferir a imagem em tempo real.

## Instalação

&emsp;Para inicializar o projeto no computador, realize os seguintes passos:

1. Clone este repositório em sua máquina, abra o terminal e navegue até a pasta em que o repositório será clonado, e digite:

    ```console
    git clone https://github.com/LuizFernandoLeao/modulo6
    ``` 

2. Navegue até onde a pasta foi criada e digite o seguinte comando para acessar a pasta raíz do workspace:

    ```console
    cd workspaceSem7/src
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

6. Agora abra um terceiro terminal e rode os seguintes comandos, para que o server rosbridge da transmissão das imagens seja ativado

    ```console
	sudo apt install ros-humble-rosbridge-suite

    ros2 launch rosbridge_server rosbridge_websocket_launch.xml
    ``` 

7. Abra o arquivo imagens.html, (presente no caminho /workspaceSem7/src/pondSem6/pondSem6/imagens.html), para ver o funcionamento da câmera, quando for ativada no próximo passo

8. Finalmente, retorne ao primeiro terminal e rode o nó em que possui o funcionamento do robô (este nó também ligará a câmera): 

    ```console 
    ros2 run pondSem6 sem6 
    ``` 
## Demonstração

&emsp;Para demonstrar o funcionamento da atividade, um vídeo foi criado demonstrando o sistema.

&emsp;<a href="https://www.youtube.com/watch?v=j8ijmBNiyPI">LINK DO VÍDEO</a>

&emsp;No vídeo, é possível ver a inicialização do sistema, em que informa o usuário de o sistema foi iniciado corretamente e se está apto para receber mensagens. Também, é possível utilizar as teclas do computador para controlar o robô, e ter uma resposta deste controle em tempo real. Além disso, há o funcionamento da transmissão de imagens, que foi simulada utilizando a câmera do computador, e utilizando o protocolo rosbridge.

&emsp;Vale destacar que a solução desta atividade foi altamente inspirada na solução do projeto em grupo. Segue o link como referência para o repositório do grupo: https://github.com/Inteli-College/2024-1b-t08-ec06-g01 . Além disso, sites de IA generativa como o ChatGPT foram utilizados, com a finalidade de ampliar os estudos sobre o assunto e aumentar a qualidade da entrega da atividade
