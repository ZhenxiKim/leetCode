class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        answer = 0
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        for item in items : 
            if ruleKey == 'type':
                if item[0] == ruleValue:
                    answer += 1;
            elif ruleKey == 'color':
                if item[1] == ruleValue:
                    answer += 1;
                    print(answer)
            else:
                if item[2] == ruleValue:
                    answer += 1;
        return answer;