class Solution {
    public int findCenter(int[][] edges) {
        int result = 0;
        int nodeCnt = edges.length;
        Map<Integer,Integer> nodeMap = new HashMap<>();
        for(int i=0; i<edges.length; i++){
            for(int j =0; j<edges[i].length; j++){
                int nodeNum = edges[i][j];
                if(nodeMap.get(nodeNum) != null){
                    nodeMap.put(nodeNum, nodeMap.get(nodeNum)+1);
                }else{
                    nodeMap.put(nodeNum, 1);
                }
            }
        }

        for(Integer strKey : nodeMap.keySet()){
            Integer keyValue = nodeMap.get(strKey);
            if(keyValue == nodeCnt){
                result =  strKey;
            }
        }
        return result;
        
    }
}