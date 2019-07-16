'''

dictionary 구축하기 (for, if)
다음과 같은 리스트가 있을 때 각각의 요소의 개수를 value 값으로 갖는 딕셔너리를 만드시오.

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
출력 예시

{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

'''

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
# 여기에 코드를 작성하시오.

# 1 for if
title_counter = {}
for title in book_title:
    # 리스트 요소가 딕셔너리에 이미 존재하는 키라면
    if title in title_counter:
        # title_counter[title] += 1
        title_counter[title] = title_counter[title] + 1
    # 없으면 (즉 새로들어가는 키라면) value 1을 가지고 들어감
    else:
        title_counter[title] = 1
print(title_counter)