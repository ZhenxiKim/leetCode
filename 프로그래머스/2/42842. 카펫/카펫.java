class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0,0};

        int total = brown + yellow;
        //가짓수를 구하는 방법
        for(int width = 3; width <= 5000; width ++) {
            for(int height = 3;height<= width; height++) {
                if ((width -2) * (height - 2) == yellow){
                    if (width * height == total) {
                        answer[0] = width;
                        answer[1] = height;
                    }
                }
            }
        }
        return answer;
    }
}