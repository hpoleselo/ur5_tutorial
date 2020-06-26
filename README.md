# Tutorial Manipulador Robótico UR5
Repositório com os comandos para instalação e com os codigos utilizados nos videos tutoriais do BR_Robotics.

[br robotics](https://user-images.githubusercontent.com/24254286/85817081-5d0c4b00-b743-11ea-8f33-0691193f59f5.png)

## Ambiente Utilizado para o Tutorial
- Ubuntu 16.04
- ROS Kinetic

## Comandos utilizados no tutorial

[Link para download do URSim](https://www.universal-robots.com/download/?option=50483#section16632)


##### Comandos utilizados no video de instalação (Parte 2):
**Lembrando que o ``` $ ``` que precede os comandos abaixo são apenas um indicativo/padrão de que o que vem depois dele é um comando de terminal**

``` $ sudo apt-get install ros-kinetic-moveit ```

``` $ sudo apt-get install ros-kinetic-industrial-msgs ```

``` $ git clone -b kinetic-devel git@github.com:ros-industrial/ur_modern_driver.git ```

``` $ git clone -b kinetic-devel https://github.com/ros-industrial/universal_robot.git ```

``` $ rosdep update ```

``` $ rosdep install --from-paths src --ignore-src --rosdistro kinetic ```

``` $ roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=127.0.0.1 ```

Para adicionar o alias do UR5 no seu bash (supondo que este esteja no diretório home):

``` $ echo "alias ur5='cd ~/ursim-3.9.0.64176 ; ./start-ursim.sh ;'" >> .bashrc ```

Para rodar o simulador então basta abrir um novo terminal e:

``` $ ur5 ```

##### Comandos utilizados na Parte 5

``` $ rostopic echo -n1 /joint_states ```

Tornar o nosso programa para controlar o robô executável:
``` $ chmod +x mover_ur5.py ```

Rodar o nosso programa utilizando o comando ``` rosrun ```:
``` $ rosrun interface_ur5 mover_ur5.py ```

##### Comandos utilizados na Parte 6
Além dos comandos para rodar a interface com o URSim/robô real, para controlarmos usando o MoveIt! precisamos rodar esses dois comandos:

``` $ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch ```

``` $ roslaunch ```


## Instalação
Caso queira já pegar o código funcional, realize um clone deste repositório dentro do seu diretório catkin:

``` cd ~/catkin_ws/src ```

e

``` git clone https://github.com/hpoleselo/ur5_tutorial.git ```

ou (caso você use SSH):

``` git clone git@github.com:hpoleselo/ur5_tutorial.git ```


## Uso

São os mesmos comandos utilizados na parte 5 dos tutoriais:

Rodar o URSim:

``` $ ur5 ```

Interface do ROS com o UR5:

``` $ roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=127.0.0.1 ```

Rodar o nosso programa utilizando o comando ``` rosrun ```:
``` $ rosrun interface_ur5 mover_ur5.py ```


