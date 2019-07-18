# word = input()

# def palindrome():
#     reverse_word = word[::-1]
#     print(word[::-1])
#     if reverse_word == word:
#         return f'True'
#     else:
#         return f'False'


# print(palindrome())

def palindrome(word):
    reverse_word = word[::-1]
    print(word[::-1])
    if reverse_word == word:
        return f'True'
    else:
        return f'False'

x = input()
print(palindrome(x))
