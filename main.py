import re
def search_word(alphabet, s):
    pattern = re.compile((f'b[{alphabet}]a'))
    result = pattern.findall(s)
    return result

alphabet1 = "abc"
s1 = "abccbcbabaabcabbbcccaaacbcbcbcbacbacbabcabcbabaabcabbbbba"
result1 = search_word(alphabet1,s1)
print(result1)

alphabet_input = input("Enter the alphabet: ")
string_input = input("Enter the string: ")
result2 = search_word(alphabet_input, string_input)
print(result2)