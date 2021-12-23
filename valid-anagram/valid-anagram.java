import java.util.Arrays;
class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()){
            return false;
        }
        boolean result = true;
      String[] sArr = s.split("");
      String[] tArr = t.split("");
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        for(int i=0; i<s.length(); i++){
            if(!sArr[i].equals(tArr[i])){
                result = false;
            }
        }
        return result;

    }
              
}