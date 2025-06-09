import random

_counter = [0]
_behaviour = ["increasing"]
random.seed(40)

def get_temperature(i: int = 0):
	# global _counter
	# global _behaviour

	while True:
		if len(_counter) > i:
			break
		else:
			_counter.append(0)
			_behaviour.append("increasing")
	
	if _counter[i]%10 == 0:
		_behaviour[i] = "increasing"
	if _counter[i]%10 == 9:
		_behaviour[i] = "decreasing"

	if _behaviour[i] == "increasing":
		_counter[i]+=1
	else:
		_counter[i]-=1

	random_integer = random.randint(1,101)
	if random_integer >= 100:
		return float(random_integer)
	else:
		return float(20+_counter[i])

def set_heat(i: int, state: bool):
	if state:
		print(f"Heating system id:{i} turned ON.")
	else:
		print(f"Heating system id:{i} turned OFF.")
	return None

def set_cool(i: int, state: bool):
	if state:
		print(f"Cooling system id:{i} turned ON.")
	else:
		print(f"Cooling system id:{i} turned OFF.")
	return None

if __name__ == "__main__":
	for i in range(100):
		print(get_temperature())