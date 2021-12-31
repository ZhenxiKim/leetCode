class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        boolean result = false;
        int cnt = 0;
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(stack.empty()){
                stack.push(c);
            }else{
                if(c == '}'){                   
                    if(stack.peek() == '{'){
                        stack.pop();
                    }else{
                        stack.push(c);
                    }
                }else if(c == ']'){
                    
                    if(stack.peek() == '['){                        
                        stack.pop();
                    }else{
                        stack.push(c);
                    }
                }else if(c == ')'){
                    if(stack.peek() == '('){
                        stack.pop();
                    }else{
                        stack.push(c);
                    }
                }else{
                    stack.push(c);
                }
            }


        }
        if(stack.empty()){
            result = true;
        }
        return result;
    }
    
}