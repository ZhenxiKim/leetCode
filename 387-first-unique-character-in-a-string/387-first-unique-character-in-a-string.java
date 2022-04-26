class Solution {
    public int firstUniqChar(String s) {

       
        String[] arr = s.split("");
        Map<String,Integer> map = new HashMap<>();
        for (String value : arr) {
            int num = 0;
            if(map.get(value) != null){
                num = map.get(value) + 1;
            }
            map.put(value, num);
        }
        for(int i=0; i< arr.length; i++) {
           if(map.get(arr[i]) == 0){
               return i;
           }

        }
        return -1;
        
    }
}
