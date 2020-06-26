#!/usr/bin/env python
import rospy
import actionlib

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

client = 0

def mover_robo():
    objetivo = FollowJointTrajectoryGoal()
    objetivo.trajectory = JointTrajectory()
    nome_das_juntas = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
    objetivo.trajectory.joint_names = nome_das_juntas


    configuracao1 = [-1.6007002035724085, -1.7092064062701624, -2.193479839955465, 0.7397122383117676, 1.5503000020980835, -0.3213999907123011]
    configuracao2 = [-1.9594710508929651, -2.008972946797506, -1.692899529133932, 0.5376193523406982, 1.9089858531951904, -0.32935792604555303]
    configuracao3 = [-1.9594710508929651, -1.86066180864443, -1.3566702047931116, 0.0530785471200943, 1.9089858531951904, -0.32935792604555303]
    configuracao4 = [-1.4995549360858362, -1.6098640600787562, -1.6520655790912073, 0.09880108386278152, 1.4491780996322632, -0.3192251364337366]

    objetivo.trajectory.points = [
        JointTrajectoryPoint(positions=configuracao1, velocities=[0]*6, time_from_start=rospy.Duration(2.0)),
        JointTrajectoryPoint(positions=configuracao2, velocities=[0]*6, time_from_start=rospy.Duration(4.0)),
        JointTrajectoryPoint(positions=configuracao3, velocities=[0]*6, time_from_start=rospy.Duration(6.0)),
        JointTrajectoryPoint(positions=configuracao4, velocities=[0]*6, time_from_start=rospy.Duration(8.0)),
        JointTrajectoryPoint(positions=configuracao1, velocities=[0]*6, time_from_start=rospy.Duration(20.0))]
    
    try:
        client.send_goal(objetivo)
        client.wait_for_result()
    except(KeyboardInterrupt):
        client.cancel_goal()
        rospy.logerr("Usuario pressionou ctrl-c para sair!")


def main():
    global client
    try:
        rospy.init_node("teste_movimento_ur5", disable_signals=True)
        client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        client.wait_for_server()
        mover_robo()
    except(KeyboardInterrupt):
        rospy.signal_shutdown("Interrupcao do teclado pelo usuario, fechando o no.")
        raise

if __name__ == "__main__":
    main()
