//1. 더하여 target 값을 구할 num1, num2를 구한다.
//2. num1은 nums를 순서대로 돌면서 하나의 값을 셋팅한다.
//3. num2는 num1에 셋팅된 다음 순번의 값을 순서대로 셋팅한다.
//4. num1과 num2를 더한값이 target값과 동일하면 리턴할 배열에서 num1, num2의 index를 찾은 후 셋팅하여 리턴한다.

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int num1Index = 0;
        int num2Index = 0;
        int[] resultArr = new int[2];
        for(int i=0; i<nums.length; i++){
           int num1 = nums[i];
           num1Index = i;
            for(int j=i+1; j<nums.length; j++){
               int num2 = nums[j];
                num2Index = j;
                if(num1 + num2 == target){
                                
                    resultArr[0] = num1Index;
                    resultArr[1] = num2Index;
                    
                    
                }
            }
        } 
        return resultArr;
    }
}