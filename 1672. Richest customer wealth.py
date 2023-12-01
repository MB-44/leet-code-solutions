class Solution:
    def maximumWealth(accounts):
        eachCustomer = [sum(banks) for banks in accounts]
        return max(eachCustomer)