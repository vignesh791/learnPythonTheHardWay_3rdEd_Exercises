# converting inches to centimeters and pounds to kilos

num_inches = 15
num_pounds = 160

inch_to_cm_mul_factor = 2.54
pound_to_kilo_mul_factor = 0.45

num_centimeters = num_inches * inch_to_cm_mul_factor
num_kilos = num_pounds * pound_to_kilo_mul_factor 

print "Length of this rope is %.1f in inches and %.1f in centimeters." % (num_inches, num_centimeters)
print "Weight of this suitcase is %.1f in pounds and %.1f in kilos." % (num_pounds, num_kilos)


