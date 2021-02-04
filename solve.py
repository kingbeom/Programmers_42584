def solution(prices):
    answer=[]
    for x in range(len(prices)):
        cnt = 0
        for y in range(x+1, len(prices)):
            cnt += 1
            if prices[x] > prices[y]:
                break
        answer.append(cnt)
    return answer