programmers(70128)

```java
class Solution {
    public int solution(int[] a, int[] b) {
        int len = a.length;
        
        int result=0;
        for(int i=0; i<len; i++) {
            result = result+a[i]*b[i];
        }
        
        return result;
    }
}
```

***

