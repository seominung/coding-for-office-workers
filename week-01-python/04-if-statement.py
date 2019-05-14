# # boolean 불리언 = 참과 거짓
# # True, False 앞이 대문자라는거 참고
# # and, or, not
# a = True
# b = False
# # A가 참이거나 혹은 B가 참이라면 (A나 B 둘 중에 하나라도 참)
# print(a and b)
# # A가 참이고 그리고 B가 참이라면 (A와 B가 둘 다 참이어야 된다.)
# print(a or b)




# 프로그래밍 언어 에서는 같다는 표시를 ==로 한다. a = True 처럼 a는True다 라고 할당해줄 때 =을 쓰기 때문에.



# a = True
# print( a == True) # a랑 true랑 같냐
# print(a is True) # a는 true냐




# if 조건문
d = 7
if d > 10: # 말그대로 if문
    print("변수는 10보다 큽니다")
elif d > 5 and d <= 10: # 조건이 중첩된다면 elif
    print("변수는 10보다 작거나 같고, 5보다는 큽니다")
else: # 아니라면 (조건이 일치하지않다면)
    print("변수는 5보다 작거나 같습니다")
