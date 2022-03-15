from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
    pir.wait_for_motion(4)
    print("Moved")
    pir.wait_for_no_motion()