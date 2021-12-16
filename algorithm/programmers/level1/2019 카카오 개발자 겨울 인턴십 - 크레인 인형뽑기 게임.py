"""
level 1 크레인 인형뽑기

시간이 조금 걸렸지만 해결할 수 있었다.. bucket을 어떤식으로 빼야할지 고민을 많이 한 것 같다...

---- 좋은 풀이---
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
"""
def solution(board, moves):
    answer = 0
    orderGrid = []
    bucket = []
    deleteCount = 0
    for _ in range(len(board)):
        orderGrid.append([])
        
    ## 주어진 board에 있는 인형들을 orderGrid 스택에 넣는다.
    for i in range(len(board)-1,-1,-1):
        for j in range(0,len(board)):
            if board[j][i] != 0:
                orderGrid[i].append(board[j][i])
        orderGrid[i].reverse()
    
    ## 2개 이상의 인형을 버킷으로 이동시키고 버킷의 마지막과 마지막-1의 값을 비교해서 같으면 두개다 pop시켜준다.
    for i in moves:
        if orderGrid[i-1]:
            bucket.append(orderGrid[i-1].pop())
            if len(bucket)>=2 and bucket[-1] == bucket[-2]:
                bucket.pop()
                bucket.pop()
                deleteCount+=1
    return deleteCount*2
    
