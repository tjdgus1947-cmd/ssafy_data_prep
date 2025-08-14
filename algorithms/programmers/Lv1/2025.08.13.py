## 📝 프로그래머스 Lv1 

- PB_42576 완주하지 못한 선수   
def solution(participant, completion):
    answer = ''
    # 1. 두 리스트를 sorting 한다
    participant.sort()
    completion.sort()
    # 2. completion list의 length 만큼 돌면서 participant에 존재하지 않는 참가자를 찾는다
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 3. 전부 다 돌아도 없을 경우 마지막 주자가 완주하지 못한 것이다
    return participant[len(participant) - 1]
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

- PB_12947 하샤드 수   
def solution(x):
    return True if x % sum([int(char) for char in str(x)]) == 0 else False

- PB_12954 x만큼 간격이 있는 n개의 숫자  
def solution(x, n):
    return[x*i for i in range(1,n+1)]

- PB_12944 평균 구하기 
def solution(arr):
    return sum(arr)/len(arr)
