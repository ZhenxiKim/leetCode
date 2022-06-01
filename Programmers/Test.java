import java.util.*;
/**
 * @author jhkim
 * @since 2022-06-01
 */
public class Test {


        public String solution(int[] numbers, String hand) {

            Map<Integer,String> numMap = new HashMap<Integer,String>();
            numMap.put(1,"L");
            numMap.put(4,"L");
            numMap.put(7,"L");
            numMap.put(3,"R");
            numMap.put(6,"R");
            numMap.put(9,"R");
            int left = 0;
            int right = 0;
            String result = "";

            for(int i=0; i<numbers.length; i++){
                if(numMap.get(numbers[i]) != null){
                    result += numMap.get(numbers[i]);
                    if(numMap.get(numbers[i]).equals("L")){
                        left = numbers[i];
                    }else {
                        right = numbers[i];
                    }
                } else{
                    int leftX = (left - 1)/3;
                    int leftY = (left - 1)% 3;
                    int rightX = (right -1)/3;
                    int rightY = (right -1)%3;


                    if((numbers[i] - left) < (right - numbers[i])) {
                        if((right - numbers[i]) != 3){
                            result += "R";
                            right = numbers[i];
                        }

                    } else if (Math.abs((right - numbers[i])) == Math.abs((left - numbers[i]))){
                        if(hand.equals("right")){
                            result += "R";
                        }else {
                            result += "L";
                        }
                    } else {
                        result += "L";
                        left = numbers[i];
                    }

                }
            }
            System.out.println(result);

            // String answer = "";
            return result;
        }

        public double getDistance(int leftX, int leftY, int rightX, int rightY) {
            double dx, dy;
            double result;

            dx = Math.pow(rightX - leftX, 2.0);
            dy = Math.pow(rightY - leftY, 2.0);

            result = Math.sqrt(dy + dx);
            return result;
        }
    }
