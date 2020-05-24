from djitellopy import Tello
import time
i = input()
tello = Tello()
try:
    if i == 'terbang':
        tello.connect()
        tello.takeoff()
        time.sleep(6)          
        tello.move_down(60)
    if i == 'hindar':
        tello.connect()
        tello.takeoff()
        time.sleep(6)  
        tello.move_forward(100)
        tello.move_up(40)
        tello.rotate_clockwise(90)
        tello.move_forward(20)
        tello.rotate_counter_clockwise(180)
        tello.move_forward(100)
    if i == 'kamera' :
        tello.takeoff()
        time.sleep(6) 
        tello.get_frame_read()
        Tello.get_video_capture

except Exception as e:

    print('error')
tello.land()
tello.get_battery()
