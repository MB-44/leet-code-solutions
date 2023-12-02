class Solution:
    def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
        exactArriveTime = arrivalTime + delayedTime
        if exactArriveTime >= 24: return abs(24-exactArriveTime)
        return exactArriveTime