
## 그리디
 - 욕심쟁이 알고리즘 -> 뒷일 생각없이 당장 이득인 것을 선택

![그리디](https://user-images.githubusercontent.com/68090443/128174232-1f4af092-f9fd-431f-bede-e88dd4389785.PNG)

![그리디2](https://user-images.githubusercontent.com/68090443/128174680-73af60dd-e35c-4ff8-b2dd-55610edab9ef.PNG)

![그리디3](https://user-images.githubusercontent.com/68090443/128174714-328a2ce5-22de-4775-a050-8f587e748a3f.PNG)

![그리디4](https://user-images.githubusercontent.com/68090443/128174769-5a9e626a-88ba-4ae0-8882-8c1546efbb57.PNG)


 그리디 문제를 푸는 방법

1. 그럴듯한 가설을 하나 세운다.

2. 항상 최적해를 만들어내는 풀이인지 증명해본다. 

3. 구현한다.


## 스택

![스택](https://user-images.githubusercontent.com/68090443/128174812-e78ab4ef-11b0-4c27-a0a3-3ab31efcfd29.PNG)

- LIFO : Last In First Out
- 쌓아두고 위쪽부터 뺀다

c++ 사용법

        std::stack

        stack<type> st;와 같이 선언

        stack.top() : 스택의 최상단 원소 (last in)

        stack.push(x) : x 삽입

        stack.pop() : 최상단 원소를 제거

        stack.size() : 스택안의 원소 개수


삽입 O(1)

삭제 O(1)

최상단 원소 조회 O(1)

최상단이 아닌 원소의 변경 : 스택말고 딴거씁시다…

![스택구현](https://user-images.githubusercontent.com/68090443/128174892-aec021d0-156b-4ce4-b48b-c203aa727cbf.PNG)

push()
스택에 원소를 추가한다.
pop()
스택 가장 위에 있는 원소를 삭제하고 그 원소를 반환한다.
peek()
스택 가장 위에 있는 원소를 반환한다. (삭제하지는 않는다.)
empty()
스택이 비어있다면 1, 아니면 0을 반환한다.

파이썬 스택 사용 예)

      stack = [0, 1, 2]

      print(stack)

      stack.append(3)

      print(stack)

      stack.pop()

      print(stack)

      '''
      [0, 1, 2]
      [0, 1, 2, 3]
      [0, 1, 2]
      '''
