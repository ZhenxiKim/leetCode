import java.util.*;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //Integer[] result = new Integer[m + n];
        //for(int i=0; i<nums1.length; i++){
        //   if(nums1[i] > 0){
        //        //System.out.println("num1:" + nums1[i]);
         //       result[i] = nums1[i];
         //   }
       // }

       // for(int i=0; i<nums2.length; i++){
       //     if(nums2[i] > 0){
       //         result[i+m] = nums2[i];
       //     }
      //  }


        
       //Arrays.sort(result);
        for (int i=m; i<nums1.length; i++){
            nums1[i] = nums2[i-m];
        }
        
        
        
       Arrays.sort(nums1);
       
    }
}