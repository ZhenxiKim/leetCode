class Solution {
    public int maxProfit(int[] prices) {
		    int profit = 0;
				int min = prices[0];//최소값으로 셋팅
				for(int day=1; day<prices.length; day++) {
					//둘째날 부터 마지막날까지 순회
					if(prices[day] < min) {
						//현재 최소값보다 작으면 큰 이윤을 남기므로 min값이 작을 경우 변경
						min = prices[day];
					} else {
						profit = Math.max(profit, prices[day] - min);
					} 
				}  
            return profit;
		}
}