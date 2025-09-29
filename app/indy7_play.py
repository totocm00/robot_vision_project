from common.program_maker import JsonProgramComponent
from common.connect import new_robot_ip_name  #  new_robot 용도로 사용
from common.safety import recover_to_home
from common.lib_function import *
from robot_a.ops import dodoA # a로봇 임포트 *이나 필요내용
from robot_b.ops import dodoB # b로봇 //      //
from robot_c.ops import dodoC # c로봇 //      //
import sys
print("PYTHON USED:", sys.executable)


def main():
    a = new_robot_ip_name("192.168.3.11")
    b = new_robot_ip_name("192.168.3.12")
    c = new_robot_ip_name("192.168.3.13")

    dodoA(a)
    dodoB(b)
    dodoC(c)

if __name__ == "__main__":
    main()
