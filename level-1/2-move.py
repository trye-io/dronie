from djitellopy import Tello

drone = Tello()

drone.connect()

drone.takeoff()

drone.move_forward(30)

drone.move_back(30)

drone.rotate_clockwise(30)

drone.move_up(30)

drone.land()
