import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> cntMap = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            if(cntMap.get(nums[i]) == null){
                cntMap.put(nums[i], 1);
            }else{
                cntMap.put(nums[i], cntMap.get(nums[i]) + 1);
            }
            
            System.out.println(cntMap.get(nums[i]));
        }
        
        boolean result = false;
        
        for(Integer key : cntMap.keySet()){
            if(cntMap.get(key) > 1){
                result = true;
            }
        }
        return result;
    }
}