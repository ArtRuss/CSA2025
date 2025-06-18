def set_alarm(state: bool):
    with open("alarm_state.txt", "w") as f:
        f.write("on" if state else "off")