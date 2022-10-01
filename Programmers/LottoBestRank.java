/**
 * @author jhkim
 * @since 2022-06-01
 * https://school.programmers.co.kr/learn/courses/30/lessons/77484
 */
public class LottoBestRank {
    public int[] solution(int[] lottos, int[] win_nums) {
        int luckyCnt = 0;//당첨수
        int zeroCnt = 0;//0으로 표기된 수
        int zeroAvail = 1;
        int[] answer = new int[2];

        for(int i  : lottos) {
            if(i == 0) zeroCnt ++; //0의 개수 체크
            else {
                for(int winNum : win_nums) {
                    if(winNum == i) {
                        luckyCnt ++; //당첨 수
                    }
                }

            }
        }
        answer[0] = num(luckyCnt + zeroCnt);
        answer[1] = num(luckyCnt);//최소 당첨 수
        return answer;
    }

    public Integer num (int cnt) {
        switch(cnt) {
            case 2 :
                return 5;
            case 3 :
                return 4;
            case 4 :
                return 3;
            case 5 :
                return 2;
            case 6 :
                return 1;
            default :
                return 6;
        }
    }
}
