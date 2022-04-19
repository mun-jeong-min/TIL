```java
import java.util.Arrays;
import java.util.stream.Stream;
class Solution {
    public boolean solution(int x) {
        int a[] = Stream.of(String.valueOf(x).split("")).mapToInt(Integer::parseInt).toArray();
        
        int rst=0;
        boolean s = true;
        
        for(int i=0; i<a.length; i++) {
            rst=rst+a[i];
        }
        if(x%rst == 0) {
            s=true;
        } else {
            s=false;
        }
        
        return s;
    }
}
```

