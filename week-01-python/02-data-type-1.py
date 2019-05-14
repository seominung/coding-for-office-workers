# 정수 int - (integer)
print("정수 int - (integer)")
print(1 + 1)

# 소수 float
print("소수 float")
print(1.5 + 2.1)

# 문자 String
print("문자 String")
print("hello")

# print(int(4 / 2)) 이거는 숫자다. 문자 아니다. print("1") 이라는 문자를 print(int("1")) 이렇게 바꾸는건 숫자로 바꾸는거임. 정수로 바꿨으니까.
print("아래 두개는 결과가 똑같이 나온다. 정수로 표현하라는 뜻. ")
print(4 // 2)
print(int(4 / 2))

#
print("그냥 4 / 2 했으면 이렇게 2.0이라고 뜨니까.")
print(4 / 2)

#
print ("이렇게 하면 소수점 나옴.")
print(float(4 // 2))
print(float(2))

# 소수인 1.5가 문자인경우 정수로 바꿔달라고 하면 에러난다. = 문자열에 소수가 담겨있을 때 숫자로 변경을 하면 에러가 난다.
# print(int("1.5"))
