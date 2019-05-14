# 함수 functions
# 입력값 parameters, 반환값 return

# 데피니션의 약자 def


# 함수가 없어도 대부분의 프로그래밍이 이루어지지만 뭔가 간략하고 보기쉽게 개발을 하기 위한 목적. 이 다음엔 클래스라는 개념을 배우는데 그 때 부터 사람들이 어려워한다. 초보자들 수준에서는 함수와 클래스가 필요가 없기 때문이기도.. 필요성을 느껴야한다.



# 1) 입력값 O, 반환값 O
def sum(a, b): # sum이 더하기 함수인듯.
    return a + b # 반환값은 항상 return으로 표시해줘야함

# 2) 입력값 O, 반환값 X
def hello_friends(name):
    print("hello, {}".format(name)) # 반환값은 항상 return으로 표시해줘야함 그래서 이 부분은 반환값이 아님

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"

# print("hi, {}".format(name1))
# print("hi, {}".format(name2))
# print("hi, {}".format(name3))
# print("hi, {}".format(name4))
# print("hi, {}".format(name5))
# print("hi, {}".format(name6))
# print("hi, {}".format(name7))
# print("hi, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)


# 3) 입력값 X, 반환값 O (반환값이 있다는건 return이 있다는것이고, 변수에 담을 수 있다. 라는 뜻)
def return_1():
    return 1 # 리턴은 변수에다가 담아서 쓸 수 있다.

ba = return_1() #ba는 리턴 넘1이다. 위에 리턴은 1이라고 해놨으니 프린트 ba 하면 1이 나옴.
print(ba)

# 4) 입력값 X, 반환값 X
def hello_world():
    print("hello world")
