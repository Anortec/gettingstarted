import time

reqamount = float(raw_input("Please enter the amount you would like to be paid? "))

# reqamount = 100

sstotal = reqamount * 0.0145
mctotal = reqamount * 0.062

paytotal = reqamount - sstotal - mctotal






print " "
print " "
print "Paycheck issued on ", (time.strftime("%m/%d/%Y"))

print "The orriginal amount requested was $",reqamount
print " "
print "The amount to be withheald for Medicare is $",mctotal
print "The amount to be witheld for Social Security is $", sstotal
print "The final amount to be paid is $",paytotal
print " "
print " "
