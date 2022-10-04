## 나의 풀이
https://school.programmers.co.kr/learn/courses/30/lessons/42577#qna
``` java
import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);//정렬로 인해 짧은값이 앞으로
        for(int i=0; i<phone_book.length-1; i++){         
            if(phone_book[i+1].startsWith(phone_book[i])) return false;          
        }
        return true;
    }
}
```

