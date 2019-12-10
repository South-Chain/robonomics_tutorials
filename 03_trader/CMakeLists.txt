cmake_minimum_required(VERSION 2.8.3)
project(trader_pkg)

find_package(catkin REQUIRED
    COMPONENTS
        rospy
        robonomics_msgs
)

catkin_python_setup()

catkin_package()

catkin_install_python(
    PROGRAMS
        scripts/trader.py
    DESTINATION
        ${CATKIN_PACKAGE_BIN_DESTINATION}
)

