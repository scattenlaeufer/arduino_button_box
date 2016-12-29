#=====================================================================#
# Author:  Björn Guth                                                 #
# Date:    13.12.2016                                                 #
#                                                                     #
# Description: Code to control WS2812b chips with an Arduino          #
#                                                                     #
#=====================================================================#


set(CMAKE_TOOLCHAIN_FILE arduino-cmake/cmake/ArduinoToolchain.cmake)

cmake_minimum_required(VERSION 3.6)

project(ArduinoButtonBox C CXX)

set(button_box_BOARD nano328)
set(button_box_SKETCH buttonbox_sketch.ino)
set(button_box_PORT /dev/ttyUSB0)

generate_arduino_firmware(button_box)

print_board_list()
