from djitellopy import Tello

drone = Tello()

drone.connect()

drone.takeoff()

drone.move_forward(50)

drone.move_right(50)

drone.move_up(20)

drone.get_battery()

drone.get_temperature()

drone.land()
