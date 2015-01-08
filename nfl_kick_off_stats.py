import csv


file = 'kick_off_return_data.csv'
f = open(file, 'rU')
reader = csv.reader(f)

return_bins = {
				'-10':	[],
				'-9':	[],
				'-8':	[],
				'-7':	[],
				'-6':	[],
				'-5':	[],
				'-4':	[],
				'-3':	[],
				'-2':	[],
				'-1':	[],
				'0':	[],
				'touchback': [],
				'1':	[],
				'2':	[],
				'3':	[],
				'4':	[],
				'5':	[],
				'6':	[],
				'7':	[],
				'8':	[],
				'9':	[],
				'10':	[],
				'11':	[],	
				'12':	[],
				'13':	[],
				'14':	[],
				'15':	[],
				'16':	[],
				'17':	[],
				'18':	[],
				'19':	[],
				'20':	[],
				'20+':	[],
			}


count = -1
for row in reader:
	if count == -1:
		# print(row)
		count = count + 1
		continue
	if (row[1] == 'kicks'):
		continue
	if row[3] == '30':
		kicking_start = 70 - int(row[1])
	elif row[3] == '35':	
		kicking_start = 65 - int(row[1])
	else:
		continue
	# print(row)
	
	return_distance = row[len(row) - 1].rstrip('.')

	return_distance = int(return_distance)

	field_position = int((return_distance)) + int(kicking_start)
	# print(field_position)
	if (kicking_start > 20):
		return_bins['20+'].append(field_position)	
	else:
		return_bins[str(kicking_start)].append(field_position - 20)

	count = count + 1



	
for k in return_bins.items():
	sum_total = sum(k[1])
	count = len(k[1])
	if (count > 0):
		average = sum_total / count
	else:
		average = 'N/A'
	# print(k)
	print(k[0] + " : " + " average: " + str(average) + " " + "count: " + str(count))



print(return_bins['18'])




