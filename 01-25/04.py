#프로그래밍은 체육관에 가는 것과 같다. 보기만 한다고 되는 것이 아니고
#직접 앉아서 프로그램을 해 봐야 한다
#디버깅은 좋은 학습 방법이다

#45 Treasure Map
row1 = ["ㅁ","ㅁ","ㅁ"]
row2 = ["ㅁ","ㅁ","ㅁ"]
row3 = ["ㅁ","ㅁ","ㅁ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")


exit()

#44 IndexError, Nested List

#43 list, offset
'''
함수를 모두 암기할 수 없다. 암기할 수 없을 정도로 많은 정보가 존재하기 때문
암기는 효율적이지 않은 학습 방식
중요한 일을 처리하기 위한 뇌의 능력을 낭비하는 것
자료와 구글이 있기 때문이다.
자료를 보고 어떤 작업이 가능할 지 확인 필요. 어떤 것이 가능한지 판단 가능
해야할 일은 구글이 함
우리는 구현하는 것
프로그래밍은 오픈 북 시험
다양한 작업을 하고 돌아가는 프로그램을 구현하는 것에 시간을 투자해야 함
'''
#42
import random

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


exit()

# 41
import random

random_integer = random.randint(1,10)
print(random_integer)

#0.00000 - 0.99999
random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f'Your love score is {love_score}')
