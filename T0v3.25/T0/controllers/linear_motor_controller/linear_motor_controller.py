from protobot.webots import Robot
from protobot.webots.linear_module import LinearModuleFactory

robot = Robot()

motor = robot.add_device('M1', LinearModuleFactory())

motor.set_pos(0.05)

arm.delay(5)

motor.set_pos(0)
