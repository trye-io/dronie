from djitellopy import Tello
import time

drone = Tello()

drone.connect()

drone.takeoff()

drone.send_rc_control(0, 50, 0, 0)
time.sleep(1)
drone.send_rc_control(0, 0, 0, 0)


drone.land()
