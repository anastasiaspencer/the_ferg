import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/anastasiaspencer/ros2_ws/the_ferg/install/the_ferg'
