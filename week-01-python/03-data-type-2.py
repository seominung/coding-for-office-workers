# list [ ] 리스트는 대괄호만 해도 인지함.
print("list") # list 라고 쓰인 문자를 출력
print([1, 2, 3]) #1,2,3 이라는 리스트를 출력
print(type([1, 2, 3])) # [1,2,3]은 이런 type이다. (리스트라고 뜨겠지?)

print("-----줄바꿈-----")


list_a = [1,2,3]
print(list_a[1]) #리스트a의 첫번째 리스트를 프린트해라. 프로그래밍은 인덱스가 1부터가 아니고 0부터 시작이기 때문에, 2가 표시돼야 한다.

print(list_a[0:1]) # 리스트a의 0에서1까지 슬라이스 한다는 의미인데 마지막건 표시되지 않는다. 2까지 나오게 하고 싶으면 [0:2] 이렇게 해야함.
# print(list_a[0:2]) #주석 없애보면 1,2 라고 나오는걸 볼 수 있음.

list_a.append(4) # append란 리스트a에 4를 더해(추가)
print(list_a) # [1,2,3,4] 라고 나옴

list_a.remove(2) # 리스트a의 2라는 데이터를 리무브해라.
print(list_a) # 리무브됨.

list_a.clear() # 리스트a를 클리어해라 클리어는 괄호 안에 뭐 넣으면 안됨.
print(list_a) # 클리어됨



print("-----줄바꿈-----")


# 튜플

# tuple (1, ) 리스트는 대괄호만 해도 인지 하지만, 튜블은 최소한 하나 이상의 값을 써야함.
# tupl은 한번 생성 후 내부 값 변경 불가
print("tuple") # 튜플이라는 문자를 출력
print((1, 2, 3)) # (1,2,3)이라는 튜플을 출력
print(type((1, 2, 3))) # (1,2,3)은 이런 타입이다. (튜플이라고 뜸)



print("-----줄바꿈-----")



# 딕셔너리
# 키와 값으로 구분되는게 딕셔너리의 기본

dict_a = {
"apple" : "a type of fruits" ,
"pen" : "a thing to write"
}

print(dict_a) # dict_a를 출력하라
print(dict_a["apple"]) # dict_a의 apple이라는 내용의 값을 알려달라
print(dict_a["pen"]) # dict_a의 pen에 해당하는 내용의 값을 알려달라.

# 값을 변경하고 싶을 때
dict_a["pen"] = "something to write" # 위에있는 내용이 현재의 값으로 바뀐뒤 출력됨.
print(dict_a)




print("-----줄바꿈-----")



# 쎗 = set([]) = 간단히 생각하면 집합이라고 생각하면된다.

# 교집합, 합집합, 차집합, 여집합
# 중복제거! 중복이 자동으로 제거되어 없다. 리스트같은 경우는 그냥 목록이기 때문에 같은값이 계속 중복해서 들어갈 수 있다 단순히 목록을 나열한 것 뿐이니까.
# set_a = ([1, 2, 3, 3, 3, 2]) 이렇게 중복되는 값을 넣어 print(set_a) 해보면 1,2,3만 찍히게 된다.

set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)


print(set_a & set_b) # 교집합
print(set_a | set_b) # 합집합
print(set_a - set_b) # 차집합
