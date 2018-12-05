from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
print "... and the file object is %r\n" % txt
print "Contents of your file are,\n"
print txt.read()

print "Now closing the file %r" % filename
txt.close()
print "... and the file object is %r" % txt

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print "Here's your file %r: " % filename
print "... and the file object is %r\n" % txt_again
print "Contents of your file are,\n"
print txt_again.read()

print "Now closing the file %r" % filename
txt_again.close()
print "... and the file object is %r" % txt_again