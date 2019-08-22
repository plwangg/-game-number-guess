import random
answer = random.randint(1,100)
answer = int(answer)
while True:
	number = input('pls guess what computer think?')
	number = int(number)
	if number == answer:
		print('you win!')
		break
	elif answer > number:
		print('bigger')
	else:
		print('smaller')