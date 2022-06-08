programmers(12909)

```java
import java.util.*;
class Solution {
    boolean solution(String s) {
        int a=0;
        int b=0;

        char[] arr = s.toCharArray();
        
        for(int i=0; i < arr.length; i++){
            
            if(arr[i] == '('){
                a++;
            } else {
                b++;
            }
            if(b>a){
                break;
            }
        }
        if(b!=a){
            return false;
        }
        return true;
    }
}
```

