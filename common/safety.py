from common.program_maker import JsonProgramComponent
from common import connect as conn

global indy3_4
indy3_2 = conn.new_robot_ip_name("192.168.3.2")
indy3_3 = conn.new_robot_ip_name("192.168.3.3")
indy3_4 = conn.new_robot_ip_name("192.168.3.4")
HOME = "HOME"

# 인디 충돌시 원위치 복귀
def recover_to_home(indy):
    indy.connect()
    indy.set_joint_vel_level(3)
    prog = JsonProgramComponent(policy=1, resume_time=2)  # Init. prgoram
    prog.add_move_home()
    prog.add_move_zero()
    prog.add_move_home()
    prog_json = prog.program_done()    # Program end
    indy.set_and_start_json_program(prog_json) # Execute program
    indy.disconnect()