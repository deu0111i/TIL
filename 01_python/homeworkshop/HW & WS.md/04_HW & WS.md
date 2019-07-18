1. ### HOMEWORK

   ---

   

   1. 파이썬에서 변수를 찾을 때 접근하는 이름공간을 순서대로 작성하세요.

Local scope



Enclosed scope



Global scope



Built-in scope

2. 다음 중 틀린 것은?
(1) 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다. (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다. (3) 함수의 인자(parameter)는 함수 선언시 설정한 값이며, 인수(argument)는 함수 호출시 넘겨주는 값이다. (4) 가변 인자를 설정할 때는 인자 앞에서 *을 붙이고, 이때는 함수 내에서 tuple로 처리된다.

(1)return a, b처럼 사용가능.

2개를 리턴하는 것처럼 보이지만 실제로는 튜플 1개가 리턴되는 것이고 이는 하나의 튜플 객체입니다.



3. 재귀함수를 쓰는 장점과 단점을 작성하세요.

   장점 : 직관적이고 이해하기 쉬운 경우가 많음(알고리즘의 경우)

   단점 : 작성하기 어려움, 메모리 스택이 넘치거나 프로그램이 느려지는 문제.

### WORKSHOP

----



 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요.

 sqrt() 사용 금지

----

![1563418024166](C:\Users\student\Desktop\1563418024166.png)



----

```python
# 양의 정수 n을 입력 받아 제곱근의 근사값(제곱했을 때 n이 되는 수)을 반환하는 함수를 작성

def my_sqrt(n):
    x, y = 1, n
    result = 1
    
    # 제곱근의 제곱(result**2)과 입력 값(n)의 차이가 적어도 이 정도 차이보다 작아지면
    
    while abs(result**2 - n) > 1e-10: # 0.0000000001
        result = (x+y)/2 #양쪽 끝 값을 더해서 2로 나누기
    # 위 근사치에 따라 x 또는 y 값을 바꾼다.
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))
```

