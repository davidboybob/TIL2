Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.



단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

```python
def palindrome(word):
    reverse_word = word[::-1]
    print(word[::-1])
    if reverse_word == word:
        return f'True'
    else:
        return f'False'

x = input()
print(palindrome(x))

```



```python
#짝수 - NA/AN
			## str을 list로 만들기 list(word)

#홀수 - S/AS
#method 1.
def is_palindrome(word):
    list_word = list(word) # ['N','A','A','N']
    # 리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
    for i in range(len(list_word)//2):# 2 짝수 1 홀수
        if list_word[i] != list_word[-i-1]:
            return False
    return True

is_palindrome('tktktkt')
#method 2.
def is_palindrome(word):
    word == word[::-1]
```

