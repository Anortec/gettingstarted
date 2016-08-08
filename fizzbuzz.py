#  if (theNumber is divisible by 3) then
#	print "Fizz"
#  else if (theNumber is divisible by 5) then
#	print "Buzz"
#  else /* theNumber is not divisible by 3 or 5 */
#	print theNumber
#  end if

finaloutput = 0
evalfiz = 0

for counter in range(1, 10):


	evalfiz = counter
	if evalfiz == 3:
		finaloutput = "fizz"
	
	else:
		finaloutput = counter

	print finaloutput




#	print "%d" %(counter)

# if eval == 0:
#	print eval




