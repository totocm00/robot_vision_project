from indy_lib.indy_lib_function import recover_to_home
from indy_lib.indy_lib_connect import new_robot_ip_name
import sys
print("PYTHON USED:", sys.executable)

def main():
    indy = new_robot_ip_name("192.168.3.4")
    ok = recover_to_home(indy)
    print("던", ok)

if __name__ == "__main__":
    main()