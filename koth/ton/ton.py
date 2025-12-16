i = input()
if '"' in i or "'" in i:
	exit()
eval(i, {'__builtins__': {}}) # output must be tuaoqwoixiqw
