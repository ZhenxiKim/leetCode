import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();


        for (int num : arr) {
            if(stack.isEmpty()){
                stack.add(num);
            }
            if (stack.peek() != num) {
                stack.add(num);
            }
        }

        
        return stack.stream().mapToInt(Integer::intValue).toArray(); 
    }
}