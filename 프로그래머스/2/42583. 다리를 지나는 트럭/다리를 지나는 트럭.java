import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();

        //초기화
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        int truckIdx = 0;
        int bridgeWeight = 0;
        int time = 0;

        while(truckIdx < truck_weights.length){
            int truckWeight = truck_weights[truckIdx];
            bridgeWeight -= bridge.poll();

            if(bridgeWeight + truckWeight <= weight){
                bridge.add(truckWeight);
                bridgeWeight+= truckWeight;
                truckIdx ++;
            }else {
                bridge.add(0);//시간이 흘러 트럭이 앞으로 이동
            }
            time ++;
        }

        while(bridgeWeight > 0){
            bridgeWeight -= bridge.poll();
            time ++;
        }
        return time;
    }
}