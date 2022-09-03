
class Solution {
    public boolean isPalindrome(String s) {
        boolean result = true;
        String str = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        
        System.out.println(str);
        for(int i=0; i<(str.length()/2); i++) {
           
           if(str.charAt(i) != str.charAt((str.length() - 1) - i)){
                result = false;
            } 
        }
        return result;
    }
}