#files
# 코드를 표현력 있고 가독성 있게, 효율적으로 작성해야 한다. 어설플 최적화는 최선이 아니다
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

print()

with open("my_file.txt", mode="a") as file:
    # contents = file.read()
    file.write("\nthe end")
    # print(contents)

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
