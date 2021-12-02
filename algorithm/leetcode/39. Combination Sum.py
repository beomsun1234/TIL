"""
8:44 ~ 9:58
39. Combination Sum
Input = array of distinct integers -> 1차원 정수형 배열(중복x)
Output =  a list of all unique combinations of candidates -> 더해서 타켓을 만들수 있는 조합을 리턴 1차원 정수 배열

Constraints:

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    All elements of candidates are distinct.
    1 <= target <= 500
    

DS - dfs, backtracking


1. 처음위치 0을 index로 잡아준다,
2. 현재 값을 저장하고, 이전 값과 현재값을 더하고 dfs를 수행한
2.1 현재 값을 저장해준다.
3. 더한 값이 target보다 크면 return
4. 같으면 리스트에 값 저장 후 리턴
5. 인덱스를 인자로 받아 dfs를 수행한다.(중복 방지를 위해(조합에서 사용함))
6. 수행 종료 후 결과 값을 저장한 배열을 빼준다(백트래킹)

time = o(n)

"""

from collections import defaultdict
class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        visited = defaultdict(list)
        answer = []
        ret = []
        for i in candidates:
            visited[i] = False
        def dfs(idx,candidates,target,mSum, ret):
            if mSum > target:
                return
            if mSum == target:
                answer.append(ret[:])
                print(ret)
            for i in range(idx,len(candidates)):
                ret.append(candidates[i])
                dfs(i,candidates,target,mSum+candidates[i],ret)
                ret.pop()
        
        dfs(0,candidates,target,0,ret)
        
        print(answer)
        
        return answer
        
