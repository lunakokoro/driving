country = input('Where are you from?')
age = input('How old are you?')
if country == 'Taiwan':
	if int(age) >= 18: # 整数才能跟整数比较
		print('You may drive.')
	else:
		print('You can not drive.')
elif country == 'USA':
	if int(age) >= 16:
		print('You may drive.')
	else:
		print('You can not drive.')
