x=print;a=lambda:x("MoveForward");b=lambda:x("TurnLeft");c=lambda:x("TurnRight")
for _ in[0]*5:a();a();b();a();c();a();a();

# or even shorter:
s='MoveForward\n';print((s*2+'TurnLeft\n'+s+'TurnRight\n'+s*2)*5,end='')
