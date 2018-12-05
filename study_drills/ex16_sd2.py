from sys import argv

script, filename = argv

print "Opening the file %r I wrote to...\n" % filename 
my_file = open(filename)

print "The contents of the file are,\n"
print my_file.read()

print "Closing the file after reading."
my_file.close()
