class Solution:
    """
    I: String, 
    O: String, 
    C: constraints
    - 1 <= s.length <= 105
        s consists of lowercase English letters.
    E: edge cases,
    
    DS 스택
    abbc - > s.append(a) -> s[-1] -> next = 중복된 값 x.->b ->  s.append(b) -> s[-1] == next = 
    
    s[-1] == next -> s.pop() if abc
    abc -> if(s[-1] = next) 
    
    ac - > sirng 
    
    time o(n)
    공간복잡도 n -> o(n)
    """
    
    def removeDuplicates(self, s: str) -> str:
        ret = []
        
        ret.append(s[0])
        
        for idx, chr in enumerate(s):
            nextIdx = idx +1 
            if nextIdx < len(s):
                if len(ret) == 0 or ret[-1] != s[nextIdx]:
                    ret.append(s[nextIdx])
                    continue
                    ret.pop()
            
        return "".join(ret)