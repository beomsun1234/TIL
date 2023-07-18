시간복작도
- O(nlogn)
- 최악(정렬되어있을경우) -> O(n^2)

공간복잡도
- O(n)

## python 코드
    
    def QuickSort(a, low: int, high: int): 
        # 종료 조건 -> 더 이상 나눌게 없을 경우
        if low >= high:
            return
    
        pivot = a[(low+high)//2]
        left = low
        right = high
        """
        교차되면 종료
        """
        while (left <= right):
            #pivot 보다 큰 값 찾기
            while (pivot > a[left]):
                left+=1
            #pivot 보다 작은 값 찾기
            while (pivot < a[right]):
                right-=1
            # 교차되지 않았을 경우
            if left <= right:
                # 스왑
                Swap(a, left, right)
                # 다음으로
                left +=1
                right -=1    
        #print(a)
        # left
        QuickSort(a,low, right)
        # right
        QuickSort(a,left, high)
    
    def Swap(a, left : int, right : int):
        tmp = a[left]
        a[left] = a[right]
        a[right] = tmp
        
    if __name__ == '__main__':
        a = [3,6,2,4,5,9,7,8,1]
        print(a)
        QuickSort(a, 0, len(a)-1)
        print(a)

## Java code 


    public class App {
        public static void main(String[] args) throws Exception {
            int a[] = {3,6,2,4,5,9,7,8,1};
            for(int num : a){
                System.out.print(num);
            }
            System.out.println();
            quickSort(a, 0, a.length-1);
            for(int num : a){
                System.out.print(num);
            }
        }
    
        public static void quickSort(int[] a, int low, int high){
            if (low >= high) {
                return;
            }
    
            int left = low;
            int right = high;
            int pivot = a[(low+high)/2];
            
            while (left <= right){
                while (pivot > a[left]){
                    left++;
                }
                
                while (pivot < a[right]){
                    right--;
                }
    
                if (left <= right) {
                    swap(a, left, right);
                    left++;
                    right--;
                }
            }
    
            //left
            quickSort(a, low, right);
            //right
            quickSort(a, left, high);
        }
    
        public static void swap(int[] a, int left, int right){
            int tmp = a[left];
            a[left] = a[right];
            a[right]= tmp;
        }
    }


## Go code

    package main
    
    import "fmt"
    
    func main() {
    	a := []int{
    		3,
    		6,
    		2,
    		4,
    		5,
    		9,
    		7,
    		8,
    		1,
    	}
    	QuickSort(a, 0, len(a)-1)
    	for _, data := range a {
    		fmt.Println(data)
    	}
    }
    
    func QuickSort(a []int, low int, hi int) {
    	//더이상 쪼갤게 없을 때
    	if low >= hi {
    		return
    	}
    	var pivot int
    	var left int
    	var right int
    
    	left = low
    	right = hi
    
    	pivot = a[(low+hi)/2]
    
    	////교차되기 전까지 반복
    	for left <= right {
    		//low - pivot 보다 큰값
    		for pivot > a[left] {
    			left++
    		}
    		//hi - pivot 보다 작은값
    		for pivot < a[right] {
    			right--
    		}
    		//교차하지 않았으면 교환
    		if left <= right {
    			Swap(a, left, right)
    			//다음으로
    			left++
    			right--
    		}
    
    	}
    	QuickSort(a, low, right)
    	QuickSort(a, left, hi)
    
    }
    
    func Swap(a []int, low int, hi int) {
    	tmp := a[low]
    	a[low] = a[hi]
    	a[hi] = tmp
    }
