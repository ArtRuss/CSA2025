import time

def alarmState(measured_temperature):

    
    alarm_state = False

    while measured_temperature >= 100:
      for i in range(5,0,-1):
        alarm_state = True
        time.sleep(i)
        alarm_state = False