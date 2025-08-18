S = "hello world" # strings are immutable

# name[0] = "R" # You cannot do this

a = len(S)
print(a)
# print(S.upper(), S)
print(S.lower())
print(S.capitalize())
print(S.title())

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

text = "Python is fun and fun and fun"
print(text.find("is")) # Output: 7 Index of first occurence
print(text.replace("fun", "awesome"))


# text = "Apples,Bnanas,Pineapples"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'pineapples']))

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False