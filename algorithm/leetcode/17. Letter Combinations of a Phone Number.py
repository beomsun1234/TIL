from typing import List


class Solution:
    """
17. Letter Combinations of a Phone Number
    
Input = string containing digits from 2-9 ex) "23"
Output = n all possible letter combination input으로 주어진 각 string요소가 가르키는 심볼의 모든 조합

Constraints
-  0 <= digits.length <= 4
-  digits[i] is a digit in the range ['2', '9'].


DS - dfs , backtracking

1. 각 번호에 해당하는 심볼을 만들어준다. ex 2 -> abc
2. 심볼들을 조합한 문자를 저장할 ret 배열 선언해주고, 마지막으로 정답을 리턴할 answer 배열을 선언해준다
3. input으로 주어진 digits string에 0번째 요소부타 dfs를 수행한다.
4. 주어진 digits의 길이 만큼 선택했으면 ret배열을 확인하여 두문자를 하나로 합쳐준 후 return
5. 만들었던 심볼의 key는 digits 요소값이며 해당 값을 가지고 digits가 가지는 문자를 저장해준다.
6. digits의 다음 요소를 찾아야 하므로 i+1일 해준다
7. 탐색이 끝이나면(2번 뽑으면) 사용한 ret를 마지막 요소를 반환해 준다.

time = o(n)
"""
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        if not digits:
            return []
        size = len(digits)
        ret = []
        answer = []
        def dfs(idx,pick,size, digits,letters, ret):
            if pick == size:
                print(ret)
                answer.append("".join(ret))
                return
            for i in range(idx, size):
                for j in letters[digits[i]]:
                    ret.append(j)
                    dfs(i+1,pick+1,size,digits,letters,ret)
                    ret.pop()
        dfs(0,0,size,digits,letters, ret)
        
        return answer