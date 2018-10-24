# examples with all python format characters

num_books = 64
num_cookies = 240
negative_num = -100
pi_short = 3.14
pi_long = 3.14159
alphabet = 'Z'
num_glasses = '2'
comment = 'good'
num_flights = 800
list = [1, 2, 3]

# %d (or %i) - signed decimal
print "I have %d books." % num_books
print "I have %i books." % num_books
print "%d is a negative integer." % negative_num

# %o - signed octal (octal number format)
print "I have %o books in octal number system." % num_books

# %x - signed hex (hexadecimal number format); %X for uppercase
print "I have %x cookies in hexadecimal number system." % num_cookies
print "I HAVE %X COOKIES." % num_cookies

# %f (or %F) - Floating point number decimal format
print "Value of pi is %f." % pi_short
print "Value of pi is %F." % pi_short

# %e - Floating point number exponential format; %E for uppercase
print "Value of pi is %e." % pi_long
print "Value of pi is %E." % pi_long

# %c - SIngle character (integer or single character string)
print "Last letter of alphabet is %c." % alphabet
print "I have %c pairs of glasses." % num_glasses

# %s - String (converts any python object to str using str() method)
# %r - String (converts any python object to str using repr() method)
print  "The lasagna was %s." % comment 
print "Around %s flights fly each day." % num_flights
print "This is how a list in python looks %s." % list

print  "The lasagna was %r." % comment 
print "Around %r flights fly each day." % num_flights
print "This is how a list in python looks %r." % list

# % - prints '%' character in the string 
print "I scored a 100% in math." 

