def count_characters_in_string(mystring):
    return sum(not c.isspace() for c in mystring)
mystring=input()
print(count_characters_in_string(mystring))