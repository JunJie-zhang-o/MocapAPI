from mocap_api import *
import time 
# import utility_functions as uf
import sys

mocap_app = None
setting = None
upleg_coor = None
leg_coor = None
foot_coor = None
upleg_rot = None
leg_rot = None
foot_coor = None
coor_header = list()
one_frame_coor = list()

def init_mocap_api():
    global mocap_app,setting
    mocap_app = MCPApplication()
    mocap_app.enable_event_cache()
    settings = MCPSettings()
    settings.set_tcp("127.0.0.1", 7001)
    settings.set_calc_data()
    # settings.set_udp(7001)
    mocap_app.set_settings(settings)

def print_joint(joint):
    global leg_coor,foot_coor,upleg_coor,coor_header,one_frame
    joint_name = joint.get_name()
    # print(joint.s())
    # joint_rotation_euler = joint.get_local_rotation_by_euler()
    # joint_roation = joint.get_local_rotation()
    # joint_coordinate = joint.get_local_position()
    # joint_default_location = joint.get_default_local_position()
    
    sensor_module = joint.get_sensor_module()
    acc_data = sensor_module.get_accelerated_velocity()
    gry_data = sensor_module.get_angular_velocity()
    quat_data = sensor_module.get_posture()
    
    # print(joint_name,":",joint_roation,joint_rotation_euler)
    # adding header name
    coor_header.append(joint_name+'.x')
    coor_header.append(joint_name+'.y')
    coor_header.append(joint_name+'.z')
    
    children = joint.get_children()
    for child in children:
        print_joint(child)

def uninit_mocap_api():
    global mocap_app
    if mocap_app.is_opened():
        mocap_app.close()
    mocap_app = None

def connect_mocap():
    global leg_coor,foot_coor,upleg_coor,coor_header,one_frame_coor
    if mocap_app is None:
        init_mocap_api()
    mocap_app.open()
    while True:
        evts = mocap_app.poll_next_event()
        for evt in evts:
            if evt.event_type == MCPEventType.AvatarUpdated:
                avatar = MCPAvatar(evt.event_data.avatar_handle)
                # print(avatar.get_index())
                # print(avatar.get_name())
                print_joint(avatar.get_root_joint())
            elif evt.event_type == MCPEventType.RigidBodyUpdated:
                print('rigid body updated')
            else:
                print('unknow event')
        if leg_coor is not None and foot_coor is not None and upleg_coor is not None:
            print(uf.compute_dist(leg_coor,upleg_coor),uf.compute_dist(leg_coor,foot_coor))

        time.sleep(1)
        
def main():
    connect_mocap()
    

if __name__ == '__main__':
    main()
    # if(joint_name=="LeftUpLeg"):
    #     upleg_coor = joint_coordinate
    # elif(joint_name=="LeftLeg"):
    #     leg_coor = joint_coordinate
    # elif(joint_name=="LeftFoot"):
    #     foot_coor = joint_coordinate