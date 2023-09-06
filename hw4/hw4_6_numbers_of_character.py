# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example: If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2 c,2 b,2 e,1 d,1 g,1 f,1
#
# Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.
#
# Use str.join() method and dict comprehension for print result

# input_string = input("Enter your text: ")
input_string = "abcdefgabc"
#
new_dict = {}
for letter in input_string:
    new_dict[letter] = new_dict.get(letter, 0) + 1

# print(new_dict)
print(' '.join([f'{k},{v}' for k, v in new_dict.items()]))
