f = open("log.lammps", "r")
count = 0
version = 0
ls = []
for string in f:
	if string[0] == 't' and string[5] == 'o' and string[6] != '_':
		count += 1
		time = int(string[8:])

	elif string[0] == 'T' and string[3] == 'E':
		count += 1
		ls.append(count)
		ls.append(count+1)
		ls.append(count+2)
		ls.append(count+3)
		version = 1	

	elif string[0] == 'S' and string[5] == 'T':
		count += 1
		lower = count
		version = 2

	elif version == 2 and string[0] == 'L':
		count += 1
		upper = count

	else:
		count += 1
f.close()


f = open("log.lammps", "r")
i = open("thermo.txt","w")
count = 0
n = 0
step = 0
for string in f:
	count += 1
	if count in ls and version == 1:
		if n % 4 == 0:
                	step = str(step)
			i.write('\n\n'+'########################### Step ' + step + '\n')
			step = int(step)
			step += time
		i.write(string[:25] + '\n' + string[26:51] + '\n' + string[52:77] + '\n')
		n += 1
	elif count > lower and count < upper and version == 2:
		step = str(step)
                i.write('\n\n'+'########################### Step ' + step + '\n')
                step = int(step)
                step += time
		i.write('Temp     =' + string[9:21] + '\nE_pair   =' + string[22:34] + '\nE_mol    =' + string[35:47] + '\nTotEng   =' + string[48:60] + '\nPress    =' + string[61:] + '\n')
		
f.close()
i.close()
