programmers(64061)

```java
import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer=0;
        Stack<Integer> stack = new Stack<>();
        
        for(int move : moves) {
            int rst = move-1;
            
            for(int i=0;i<board[0].length; i++) {
                int result = board[i][rst];
                if(result!=0) {
                    board[i][rst] = 0;
                    
                    if(!stack.isEmpty() && stack.peek() == result) {
                        
                        answer += 2;
                        stack.pop();
                        break;
                    }
                    
                    stack.push(result);
                    break;
                }
            }
        }
        
        return answer;
	}
}
```

---

