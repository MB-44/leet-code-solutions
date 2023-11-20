# 703ms
class Solution(object):
    def garbageCollection(self,garbage,travel):
        travel.insert(0,0)
        truckType = ["P","G","M"]
        indexOfHouse = []
        for truck in truckType:
            for house in range(len(garbage)-1,-1,-1):
                if truck in garbage[house]:
                    indexOfHouse.append(house)
                    break
        travelTIme,collectTime = 0,0
        for index in indexOfHouse:
            for time in travel[:index+1]:
                travelTIme += time
        
        for word in garbage:
            for letter in word:
                collectTime+=1

        return travelTIme+collectTime






if __name__ == "__main__":
    garbage = ["G","P","GP","GG"]
    travel = [2,4,3]
    result = Solution().garbageCollection(garbage,travel)
    print(result)
