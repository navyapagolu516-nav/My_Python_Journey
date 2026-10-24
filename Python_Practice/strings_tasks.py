# Coding Exercise : 
# Problem: You are given a string "sentence". Print the characters at even indices.
# Example: sentence = "Python is amazing"
# Output: "Pto saaig"

sentence = "Python is amazing"
print(sentence[::2])

###########################################################
# Problem: You are given a string "s" . 
# Replace all spaces in the string with underscores (_) and print the modified string.
# Example: s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

s = "Python is fun and powerful"
modified_string = s.replace(' ','_')
print(modified_string)
###########################################################
# Problem: You are given a string "s" . Check if the string contains only digits.
# Example: s = "12345"

s = "12345"
if s.isdigit():
    print("Yes, The given string containes only digits")
else:
    print("No, The given string does not contains only digits")
################################################################
# Problem:
# You are given a string "s" . Print the string in reverse order
# Example:
# s = "Python is amazing"
# Output: "gnizama si nohtyP

s = "Python is amazing"
print(s[::-1])

################################################################
# Problem:
# You are given a string "s" . 
# Capitalize the first letter of each word in the string and print the modified string.
# Example:
# s = "python programming is fun"
# Output: "Python Programming Is Fun"

s = "python programming is fun"
print(s.title())

