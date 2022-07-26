----

programmers(12982)

```java
import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);
        int rst=0;
        
        for(int a : d) {
            budget=budget-a;
            if(budget < 0) {
                return rst;
            }
            rst++;
        }
        return rst;
    }
}
```

