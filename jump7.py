for real_time_data in range(0,101):
	if real_time_data%7 == 0:
		continue
	elif real_time_data % 10 == 7:
		continue
	elif real_time_data //10 == 7:
		continue
	else:
		print(real_time_data)
