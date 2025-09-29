from common.dcp_client import IndyDCPClient as DCPClient
from common.program_maker import JsonProgramComponent


def new_robot_ip_name(ip):
    # Set robot (server) IP 
    robot_ip = ip  # 192.168.3.2    3.3   3.3

    # Set robot name
    robot_name = "NRMK-Indy7"

    # Create class object
    return DCPClient(robot_ip, robot_name)