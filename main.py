import re
def search_word(alphabet, s):
    pattern = re.compile((f'b[{alphabet}]a'))
    result = pattern.findall(s)
    return result

alphabet1 = "abc"
s1 = "abccbcbabaabcabbbcccaaacbcbcbcbacbacbabcabcbabaabcabbbbba"
result1 = search_word(alphabet1,s1)
with open("result1.txt", "w") as file:
    file.write(str(result1))
print(result1)

alphabet_input = input("Enter the alphabet: ")
string_input = input("Enter the string: ")
result2 = search_word(alphabet_input, string_input)
with open("result2.txt", "w") as file:
    file.write(str(result2))
print(result2)