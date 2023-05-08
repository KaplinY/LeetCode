class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for i in range(len(accounts)):
            wealth.append(sum(accounts[i]))
        result = max(wealth)
        return(result)