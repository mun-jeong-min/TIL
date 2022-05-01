***

programmers(12922)

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

***

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

programmers(86051)

```java
class Solution {
    public int solution(int[] numbers) {
        
        int rst=0;
        for(int number : numbers)
            rst+=number;
        
        return 45-rst;
    }
}
```

***

programmers(12937)

```java
class Solution {
    public String solution(int num) {
        if(num % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    }
}
```

***

programmers(12944)

```java
class Solution {
    public double solution(int[] arr) {
        int s=0;
        int a=0;
        for(int j=0; j<arr.length; j++) {
            s = arr[j]+s;
            a++;
        }
        double result = s / (double)a;
        return result;
    }
}
```

***

programmers(12947)

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

***

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

programmers(76501)

```java
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int result=0;
        
        for(int i=0; i<absolutes.length; i++) {
            if(signs[i] == false) {
                absolutes[i] = absolutes[i] - absolutes[i]*2;
            }
            result+=absolutes[i];
        }
        
        return result;
    }
}
```

---

programmers(12954)

```java
class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        for(int i=1; i<=n; i++) {
            answer[i-1] = (long)x*i;
        }
        
        return answer;
    }
}
```

