#함수를 사용하여 프로그래밍을 간단히 보이게 만든다
#함수형 프로그래밍
# 계속 노력하는 한 성공에 가까워질 수 있다. 자책하지 말자.

#Scope

# how to modify variables with global scope
enemies = 1

def increase_enimies():
    global enemies
    enemies += 1
    print(f"enemies: {enemies}")

increase_enimies()
print(f"enemies: {enemies}")
