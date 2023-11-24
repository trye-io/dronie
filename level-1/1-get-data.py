from djitellopy import Tello

drone = Tello()

drone.connect()

drone.get_battery()

drone.get_temperature()

drone.get_distance_tof()

drone.get_barometer()