# 1.0
while True:
    if get_temperature() >= 100:
        set_alarm(True)
    else:
        set_alarm(False)


# 1.1.1
import time
for i in range(5,-1,-1):
    set_alarm(True)
    time.sleep(i)
    set_alarm(False)
    time.sleep(1)
