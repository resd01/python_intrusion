# -*- coding: utf-8 -*-
def calc(value, until):
	i = 0
	j = 1
	temp = 0
	iteration = 0
	if int(value) != 0:
		for x in xrange(0,int(value)):
			temp = i + j
			i = j
			j = temp
			print i
		pass
	else:
		while i < int(until):			
			print i
			temp = i + j
			i = j
			j = temp
			iteration += 1
			pass
		print "Number of iteration(s): %i" % iteration
	pass

def main():
	iteration = raw_input('Number of iteration(s) : ')
	if iteration == '':
		until = raw_input('Until : ')
		calc(0, until)
		pass
	else:
		calc(iteration, 0)
		pass


print unicode("╔", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╗", 'utf-8')
print unicode("║", 'utf-8') + "                        _,.--.                                                " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "    --..,_           .'`__ o  `;__, Fibonacci                                 " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "       `'.'.       .'.'`  '---'`  ' v1                                          " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "          '.`-...-'.'                                                         " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "            `-...-'                                                           " + unicode("║", 'utf-8')
print unicode("╚", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╝", 'utf-8')
main()