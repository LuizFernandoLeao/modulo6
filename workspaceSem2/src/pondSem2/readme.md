# Ponderada Semana 2 - Luiz Fernando Leão

## Objetivo

&emsp;O objetivo da atividade é aprender os conceitos básicos do ROS, ao interagir com o turtlesim. A partir disso, será possível interagir com o turtlebot em etapas futuras do projeto.

&emsp;Na atividade, a tartaruga deverá aparecer na tela (spawn), fazer um desenho e desaparecer da tela (kill).

## Instalação

&emsp;Para inicializar o projeto no computador, realize os seguintes passos:

1. Clone este repositório em sua máquina, abra o terminal e navegue até a pasta em que o repositório será clonado, e digite:

    ```console
    git clone https://github.com/LuizFernandoLeao/modulo6
    ``` 

2. Navegue até onde a pasta foi criada e digite o seguinte comando para acessar a pasta raíz do workspace:

    ```console
    cd workspaceSem2/src
    ``` 

3. Agora é preciso contruir o pacote, para que o programa tenha as dependências necessárias para funcionar:

   ```console
    colcon build
    ``` 

4. Faça a instalação do setup:

    ```console
	. install/setup.bash
    ``` 

5. Abra um segundo terminal e rode o seguinte comando, para que o ambiente em que a tartagura funcionará apareça: 

    ```console
	ros2 run turtlesim turtlesim_node
    ``` 

6. Finalmente, retorne ao primeiro terminal e rode o nó em que possui o funcionamento da tartaruga: 

    ```console 
    ros2 run pondSem2 nodeSem2 
    ``` 
## Demonstração

&emsp;Para demonstrar o funcionamento da atividade, um vídeo foi criado demonstrando o sistema.

LINK VIDEO AQ

&emsp;No vídeo, é possível ver os comandos da inicialização do programa, a tartaruda spawna e realiza o desenho, e depois ela desaparece