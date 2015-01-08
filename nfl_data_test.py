import csv 

total_count = 0

def decipher_kick_off_description(kick_off, writer):
	# print(kick_off)
	stats_string = kick_off.split(' ')
	kicker = stats_string[0]
	# kick_distance: 65 = touchback, could be onside
	kick_distance = stats_string[2]
	kicking_team_name = stats_string[5]
	kicking_place = stats_string[6]
	# zone for touchback, otherwise <0 for depth into endzone, otherwise >0 for spot
	kick_start = stats_string[9]
	kick_name = stats_string[10]
	# print(stats_string[2] + " " + stats_string[3] + " " + stats_string[4] + " " + stats_string[5] + " " + stats_string[6] + 
	# 	" " + stats_string[9] + " " + stats_string[10])

	# len = 11 when out of the back of the endzone
	# len = 12 when normal touchback (Caught)
	# len = 18 for return
	if (len(stats_string) == 18):
		return_distance = stats_string[len(stats_string) - 3]
	elif (len(stats_string) == 12):
		return_distance = 'touchback'
	elif (len(stats_string) == 11):
		return_distance = 'touchback'
	elif (len(stats_string) == 15):
		if (kick_off.find('Touchback') != -1):
			return_distance = 'touchback'
		else:
			return_distance = stats_string[len(stats_string) - 3]
	elif (len(stats_string) == 20):
		return_distance = stats_string[len(stats_string) - 3]
	elif (len(stats_string) == 19):
		if (stats_string[len(stats_string) - 4]) == 'for':
			return_distance = stats_string[len(stats_string) - 3]
		else:
			return_distance = stats_string[len(stats_string) - 4]
	else:
		# ignore offside, penalties, ob kicks, other wacky stuff
		return -1

	
	try:
		test = int(return_distance)
		writer.writerow([kicker] + [kick_distance] + [kicking_team_name] + [kicking_place] + [kick_start] + [kick_name] + [return_distance])
		return 0
	except:
		return -1
	


def nfl_kick_off_file_reader(file, writer):
	f = open(file, 'rU')
	reader = csv.reader(f)
	count = 0				
	for row in reader:
		if count == 0:
			count = 1 
			continue
		description_string = row[len(row) - 4]
		is_description_kick_off = (description_string.find('kicks') != -1) and (description_string.find('35') != -1)
		is_play_data_kick_off = ((row[6] == '') and (row[7] == '') and (description_string.find('extra') == -1) and (description_string.find('onside') == -1))
		is_kick_off = (is_play_data_kick_off and is_description_kick_off)
		if (is_kick_off):
			kick_off_stats = decipher_kick_off_description(description_string, writer)
			# print(description_string)
		count = count + 1



write_file = open('kick_off_return_data.csv', 'w+')
writer = csv.writer(write_file)
writer.writerow(['kicker_name'] + ['kick_distance'] + ['kicking_team'] + ['kick_off_yard_line'] + ['kicking_start'] + ['kick_name'] + ['return_distance'])
nfl_kick_off_file_reader('2012_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2002_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2003_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2004_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2005_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2006_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2007_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2008_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2009_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2010_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2011_nfl_pbp_data.csv', writer)
nfl_kick_off_file_reader('2013_nfl_pbp_data_through_wk_12.csv', writer)	
