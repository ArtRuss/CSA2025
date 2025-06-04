def run_the_path():
    for i in range(19): # 0-18
        if i % 2 == 0:
            MoveForward() for i in range(2)
            TurnLeft()
        else:
            MoveForward()
            TurnRight()
