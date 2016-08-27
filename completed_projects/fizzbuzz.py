#  if (theNumber is divisible by 3) then
#	print "Fizz"
#  else if (theNumber is divisible by 5) then
#	print "Buzz"
#  else /* theNumber is not divisible by 3 or 5 */
#	print theNumber
#  end if



fizztrue = 0
buzztrue = 0

for counter in range(1, 100):


	output = counter


	if counter % 3 == 0:
		output = "Fizz"

	if counter % 5 == 0:
		output = "Buzz"

	if (counter % 3 == 0 and counter % 5 == 0):
		output = "FizzBuzz"

	print output










# for counter in range(1, 100):
#	evalfiz = counter
#	if evalfiz == 3:
#		finaloutput = "fizz"
#	
#	else:
#		finaloutput = counter
#
#	print finaloutput




