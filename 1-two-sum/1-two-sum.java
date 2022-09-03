class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer,Integer> numMap = new HashMap<>();
       for(int i=0; i<nums.length; i++) {
           if(numMap.get(nums[i]) != null) return new int[] {numMap.get(nums[i]), i};
           numMap.put(target- nums[i], i);
       }
        return null;
    }
}


  