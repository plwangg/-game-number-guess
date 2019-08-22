import random
end = input('upper bound is:')
end = int(end)
answer = random.randint(1,end)
answer = int(answer)
i = 0
while True:
	i = i + 1
	number = input('pls guess what computer think?')
	number = int(number)
	if number == answer:
		print('you win in', i,'times')
		break
	elif answer > number:
		print('bigger,this is', i,'time you guess')
	else:
		print('smaller,this is', i,'time you guess')