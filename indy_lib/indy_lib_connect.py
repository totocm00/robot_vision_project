from indy_utils.indydcp_client import IndyDCPClient as DCPClient
from indy_utils.indy_program_maker import JsonProgramComponent


def new_robot_ip_name(ip):
    # Set robot (server) IP 
    robot_ip = ip  # 192.168.3.2    3.3   3.3

    # Set robot name
    robot_name = "NRMK-Indy7"

    # Create class object
    return DCPClient(robot_ip, robot_name)