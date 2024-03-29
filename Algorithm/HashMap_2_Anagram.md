## 나의 풀이
``` java
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;

/**
 * @author jhkim
 * @since 2022-09-20
 */
public class Test {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        String input1 = in.nextLine();
        String input2 = in.nextLine();
        Test t = new Test();
        System.out.println(t.solution(input1, input2));
    }

    public String solution(String input1, String input2) {
        Map<String,Integer> cntMap = new HashMap<>();
        for (String c: input1.split("")) {
            cntMap.put(c.toLowerCase(Locale.ROOT), cntMap.getOrDefault(c.toLowerCase(Locale.ROOT), 0) + 1);
        }

        for (String c: input2.split("")) {
            if(!cntMap.containsKey(c.toLowerCase(Locale.ROOT))) return "NO";
            cntMap.put(c.toLowerCase(Locale.ROOT), cntMap.getOrDefault(c.toLowerCase(Locale.ROOT), 0) - 1);
        }
        for (String c: input2.split("")) {
            int num = cntMap.get(c.toLowerCase(Locale.ROOT));
            if(num > 0) {
                return "NO";
            }
        }
        return "YES";
    }
}
```



## 답안
```java
public class Test {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        String input1 = in.next();
        String input2 = in.next();
        Test t = new Test();
        System.out.println(t.solution(input1, input2));
    }

    public String solution(String input1, String input2) {
        Map<Character,Integer> cntMap = new HashMap<>();
        for (char c: input1.toCharArray()) {
            cntMap.put(c, cntMap.getOrDefault(c, 0) + 1);
        }

        for (char c: input2.toCharArray()) {
            if(!cntMap.containsKey(c) || cntMap.get(c) == 0) return "NO";
            cntMap.put(c, cntMap.getOrDefault(c, 0) - 1);
        }
        return "YES";
    }
}
```


## TIL
