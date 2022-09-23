## 나의 풀이
``` java
public static void main(String[] args){
        Test T = new Test();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.println(T.solution(str));

    }

    public String solution(String str) {
        char[] s = str.toCharArray();
        int lt =0;
        int rt = str.length() -1;
        while(lt < rt) {
            if(!Character.isAlphabetic(s[lt])) lt ++;
            else if(!Character.isAlphabetic(s[rt])) rt --;
            else {
                char tmp = s[lt];
                s[lt] =s[rt];
                s[rt] = tmp;
                lt ++;
                rt--;
            }
        }
        return String.valueOf(s);
    }
```


## 답안
```java

```


## TIL
