```java
class Solution {
    public String solution(int n) {
        String answer = "수박";
        
        String a = answer.repeat(n);
        
        String a2;
        
        int result = n - n/2;
        
        if(n/2 % 2 == 0) {
          a2 = a.substring(0,n);
        } else {
            a2 = a.substring(0,n/2+result);
        }
        
        return a2;
    }
}
```

