# Prova 1 - Luiz Fernando Leão

## Objetivo

&emsp;O objetivo da atividade é desenvolver uma interface de linha de comando (CLI) para controlar um simulador de robô tartaruga, o Turtlesim, utilizando o ROS2 (Robot Operating System 2).

## Instalação

&emsp;Para inicializar o projeto no computador, realize os seguintes passos:

1. Clone este repositório em sua máquina, abra o terminal e navegue até a pasta em que o repositório será clonado, e digite:

    ```console
    git clone https://github.com/LuizFernandoLeao/modulo6
    ``` 

2. Navegue até onde a pasta foi criada e digite o seguinte comando para acessar a pasta raíz do workspace:

    ```console
    cd workspaceProvaSem05/src
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
    ros2 run prova1 prova
    ``` 
