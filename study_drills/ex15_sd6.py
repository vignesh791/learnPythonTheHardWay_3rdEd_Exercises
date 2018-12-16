#open a file for writing/reading

filename = "file_hdling.txt"
print "Opening file %s for writing" % filename

txt = open(filename, "w+")

#1. write method
content = """This file is a text file.
It has several lines.
You can write an essay or poem.
You can use punctuation characters.
"""
txt.write(content)
raw_input('>')

#2. writelines method 
content2 = "I prefer poems to essays."
content3 = "\nI also like math."
str_list = [content2, content3]
txt.writelines(str_list)
raw_input('>')

#3. tell method
print "Current file position is %d" % txt.tell()
raw_input('>')

#4. seek method
txt.seek(0) # move to beginning of file
print "Current file position is %d" % txt.tell()
raw_input('>')

#5. readline method
print "First line in the file is: %s" % txt.readline()
txt.seek(0)
print "First 10 bytes of the file is: %s" % txt.readline(10)
raw_input('>')

#6. readlines method
print "Remainder of lines in the file %s" % txt.readlines()
raw_input('>')

#7. truncate method
txt.seek(0)
txt.readline()
txt.truncate()
txt.seek(0)
print "File truncated to first line: %s" % txt.read()
raw_input('>')

#8. flush method 
txt.write("This is the last line.")
txt.flush()
raw_input('>')

#9. close method
print "Closing the file now."
txt.close()



