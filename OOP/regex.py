# import re
# #
# # names = ["Katherine Anne", "George bush", "Chris", "Karen", "Kristen"]
# #
# #
# #
# # regex = "\w*\s"
# #
# # for name in names:
# #     match = re.search(regex, name, re.IGNORECASE)
# #     if match:
# #         print(name)
# pattern = r'^K\w*'
#
# # Compile the regex pattern into a regex object
# regex_pattern = re.compile(pattern, re.IGNORECASE)
#
# print(regex_pattern)

import re

# Define a regex pattern
# pattern = r'\d+'
#
# # Compile the pattern into a regex object
# regex_object = re.compile(pattern)
#
# # Example string
# text = "123456"
# # apples and 123 oranges.
# print(len(text))
#
#
# pattern = re.finditer(r"4634",text)
#
# for match in pattern:
#     print(match)


# my_string = "12345abc65.69abc1011ABC"

# pattern = re.compile("\w+")
# my_string = ["kelvin123", "kelvin", "123jioj" "mum", "6453efaf", "23good","boy2424", "okoye23132"]
#
# # match for letters that start with digits and ones that also ends with digits .
#
# # solution
#
# regex = "[$\d + \d$]"
#
# for name in my_string:
#     if re.match(regex, name):
#         print(name)

# import re
#
# my_string = ["kelvin123", "Kelvin", "123jioj", "mum","***@", "##$^DFF", "6453efaf", "23good", "boy2424", "okoye23132"]
#
# # Solution
# regex = re.compile(r'[0-9]')
#
# for name in my_string:
#     matches = regex.finditer(name)
#     for match in matches:
#         print(match.span())


x = [1,2,3,4,5]
y = x[1:4:2]

print(y)


# for name in text:
#     match_result = regex_object.search(text)
#     if match_result:
#         print("Match found:", match_result.group())
#     else:
#         print("No match.")


