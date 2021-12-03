"""
22. Generate Parentheses
Input = Given n pairs of parentheses, 괄홍 쌍의 개수인 n-> int
Output = 잘 구성된 괄호의 모든 조합 ex) (), (())

Constraint
    1 <= n <= 8


DS - dfs, backtracking

1. 쌍이기에 주어진 n*2를 하여 총 골화의 갯수를 구한다.
2. 괄호의 조합을 저장할 ret라는 배열을 선언해준다.
3. 괄호의 조합을 구하기 위해서 괄호의 1쌍은 2개의 괄호를 가지고있다.
만약 2개의 괄호 쌍의 조합을 구하라고한다면 (()) 이런식과 ()()  2개가 나올것이다.
패턴을 분석해보면 항상 괄호가 열려있는 것 부터 시작하며 ex) ())(
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        size = n*2
        ret = []
        def dfs(openP,closeP,size,ret,parenthese):
            if openP < closeP:
                return
            if len(ret) == size:
                print("".join(ret))
                answer.append("".join(ret))
                return
            if openP > size//2:
                return
            ret.append(parenthese)
            dfs(openP+1,closeP,size,ret,'(')
            dfs(openP,closeP+1,size,ret,')')
            ret.pop()
        dfs(1,0,size,ret,"(")
        print(answer)
        return answer