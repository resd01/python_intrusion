art = '''
______ _ _             _____       _ _       
|  ___(_) |           /  ___|     (_) |      
| |_   _| |__   ___   \ `--. _   _ _| |_ ___ 
|  _| | | '_ \ / _ \   `--. \ | | | | __/ _ \\
| |   | | |_) | (_) | /\__/ / |_| | | ||  __/
\_|   |_|_.__/ \___/  \____/ \__,_|_|\__\___|

            ________   .==.
by cuicui  [________>c((_  )
                       '=='
'''

a = 0							#Variables
b = 1
c = a + b
print art
limit = raw_input('Limite :')	#Ask, which limit ?
print ('%i\n%i') % (a,b)		#Print firsts variables
while c < int(limit) :			#Print until limit is reached
	print (c)
	a = b
	b = c
	c = a + b
