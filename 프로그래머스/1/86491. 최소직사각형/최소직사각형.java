class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int longer_max = 1;
        int shorter_max = 1;
        
        for(int i = 0; i < sizes.length; i++){
            int longer = Math.max(sizes[i][0], sizes[i][1]);
            int shorter = Math.min(sizes[i][0], sizes[i][1]);
            
            if (longer > longer_max) {
                longer_max = longer;
            }
            if (shorter > shorter_max) {
                shorter_max = shorter;
            }
        }
        answer = shorter_max * longer_max;
        return answer;
    }
}