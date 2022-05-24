class Solution {
    public int romanToInt(String s) {
        //roman 문자에 해당하는 숫자값을 map에 담는다.
        int sumResult = 0; //합계
        Map<String, Integer> numMap = new HashMap<String, Integer>();
        numMap.put("I",1);
        numMap.put("V",5);
        numMap.put("X",10);
        numMap.put("L",50);
        numMap.put("C",100);
        numMap.put("D",500);
        numMap.put("M",1000);
        
        //로만글자를 다 쪼갠다.
        String[] sArr = s.split("");

        for(int i=0; i<s.length(); i++){
           
           String c = sArr[i];
           
           int num = numMap.get(c);
           if(i+1 == s.length()) {
            //마지막 글자라면 더하기 연산만 필요   
            sumResult += num;
            return sumResult;
           }
         
            String next = sArr[i+1];
            if(num < numMap.get(next)) {
                //다음 글자와 비교하여 크면 빼준다.
                sumResult -= num;
            } else {
                //아닌경우 덧셈
                sumResult += num;
            }
            
        }
        return sumResult;
    }
}