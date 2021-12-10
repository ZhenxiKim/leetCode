class Solution {
    public int maxProduct(int[] nums) {
        
        List<Integer> numValueList = new ArrayList<Integer>();
        
        for(int i=0; i < nums.length; i++){
            for(int j=0; j<nums.length; j++){
                if(i != j){
                   numValueList.add((nums[i]-1)*(nums[j]-1));
                }
            }
            
        }
        
        int max = 0;
        for( int i=0; i<numValueList.size(); i++){
            if(max < numValueList.get(i)){
                max = numValueList.get(i);
            }
        }
        return max;
    }
}