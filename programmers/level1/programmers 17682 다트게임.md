programmers 17682 다트게임

```java
import java.util.*;
class Solution {
    public int solution(String dartResult) {
        char[] arr = dartResult.toCharArray();
        int q = 0;
        int rst=0;
        int value=0;
        
        int dam = 0;
        int check=0;
        int i = -1;
        int tib = 0;
        
        for(char a : arr) {
            switch(a) {
                case 'T':
                if(q == 0) {
                    dam = value*value*value;
                }
                if(q >= 1) {
                    tib = value*value*value;
                }
                q++;
                rst=rst+(value*value*value);
                    break;
                    
                case 'D':
                if(q == 0) {
                    dam = value*value;
                }
                if(q >= 1) {
                    tib = value*value;
                }
                q++;
                rst=rst+(value*value);
                    break;
                    
                case 'S':
                if(q == 0) {
                    dam = value;
                }
                if(q >= 1) {
                    tib = value;
                }
                q++;
                rst=rst+value;
                    break;
                    
                case '*':
                if(q == 3) {
                    rst=(rst-dam)*2 + dam;
                } else {
                    dam=dam*2;
                    rst = rst*2;
                }
                    break;
                    
                case '#':
                if(q==1) {
                    rst = rst * (-1);
                } else {
                    rst = (rst-tib) + ((-1) * tib);
                }
                    break;
                    
                default:
                if(value == 1 && Character.getNumericValue(a) == 0) {
                    value = 10;
                } else {
                    value = Character.getNumericValue(a);
                }
                    break;
            }
            i++;
        }
        
        return rst;
    }
}
```

