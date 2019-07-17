'''
장바구니에 아래와 같은 과일이 들어있고 과일 판별 리스트가 있습니다.

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
현재 장바구니에는 과일이 몇개이고 과일이 아닌 것은 몇개인지 출력하시오.

예시 출력)
과일은 23개이고, 11개는 과일이 아닙니다..
'''

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# 아래에 코드를 작성하세요.

count_1 = 0
count_2 = 0

for key, value in basket_items.items():
    if key in fruits:
        count_1  = count_1 + value
    else:
        count_2 = count_2  + value 
print(f' 과일은 {count_1}개이고, {count_2}개는 과일이 아닙니다..')