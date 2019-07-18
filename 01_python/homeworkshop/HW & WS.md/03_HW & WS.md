1. ## homework

2. 

3. 

4. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.

```python
dir(__builtins__)
```



2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.

   3번은 키워드 인자 활용한 뒤에 위치 인자를 사용할 수 없다.

3. 

4. 

5. 

6. 

7. 

8. 

9. 

   다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.

None(낚시엿다) return이 없는 함수임





## workshop



v Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.
v 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.



```python
def is_palindrome(word): # NAAN
    list_word = list(word) # ['N', 'A', 'A', 'N']
    # 리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
    for i in range(len(list_word) // 2): #2
        if list_word[i] != list_word[-i-1]:
            return False
    return True
is_palindrome('ㅗㅑㅗㅑㅗㅑㅗㅑㅗㅑㅗㅑ')
```



```python
word = 'ㅗㅑㅗㅑㅗㅑㅗ'
word == word[::-1]
0, 1
#처음부터 끝까지 -1씩 증가한다.=역순
```







