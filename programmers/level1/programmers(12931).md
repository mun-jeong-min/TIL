programmers(12931)

```java
import java.util.stream.Stream;
import java.util.*;

public class Solution {
    public int solution(int n) {
        int[] s = Stream.of(String.valueOf(n).split("")).mapToInt(Integer::parseInt).toArray();
        
        int rst=0;
        for(int a : s)
            rst+=a;
        
        return rst;
    }
}
```

***