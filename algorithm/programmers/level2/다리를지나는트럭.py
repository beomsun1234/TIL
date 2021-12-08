from collections import deque
"""
level2 다리를 지나는 트럭
어려웠다... 생각을 못한것 같다.. 다리를 건너는 트럭을 어떤식으로 표현할지 잘 몰랐다.
여러 사람이 작성한 코드를 확인해 보았더니 다리를 건너는 트럭(다리 위의 트럭)을 큐로 만들어 주었고 트럭이 빠지면 현재 브릿지의 값과 기다리는 트럭의 첫번째 값을 더한 값이 weights보다 작을 경우 다리에 들어갈 수 있라는 방식으로 접근하면 되는 문제였다. 
## 문제를 잘 읽자, 문제대로 구현하면 될 것 같은데 먼가 생각을 잘 못하겠다.. 주어진 표대로 구현하면 되는 것 같다

Input  = 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights 

Output = 다리를 건너려면 최소 몇 초가 걸리는지 return

DS - deque

1. 다리를 건너는 트럭과 대기트럭을 큐로 만들어준다.
1.1 다리를 건너는 트럭은 주어진 bridge_length만큼 0으로 초기화 해준다.(0초에는 아무것도 들어올 수 없다. 1마다 움직일 수 있다.) -> 0은 들어올 수 없다는 뜻으로 해석하자
2. 반복문을 다리에 아무것도 없을 경우 종료시킨다.
3. 반복문을 순회하면서 초를 증가시켜주고 각 초마다 truck_on_bridge의 값을 꺼내서 현재 다리위의 무개에 꺼낸 값을 빼준 후 현재 다리위의 무게와 기다리는 트럭의 무게를 더한값이 다리가 견딜 수 있는 무게보다 작거나 같을 경우 기다리는 첫번째 트럭을 다리위로 넣어준다.
3.1 만약 위의 경우가 아니라면 다리위에는 들어갈 수 없으므로 0으로 값을 넣어준다.
"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_truck = deque(truck_weights)
    truck_on_bridge = deque([0 for _ in range(bridge_length)])
    bridgeWeight = 0
    
    time = 0
    
    # [0,7]
    while len(truck_on_bridge):
        out = truck_on_bridge.popleft()
        bridgeWeight -= out
        time+=1
        if wait_truck:
            if  bridgeWeight + wait_truck[0] <= weight:
                inTruckWeight = wait_truck.popleft()
                truck_on_bridge.append(inTruckWeight)
                bridgeWeight+=inTruckWeight
            else:
                truck_on_bridge.append(0)
    print(time)
    return time
    
