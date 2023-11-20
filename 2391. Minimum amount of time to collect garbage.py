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
        



if __name__ == "__main__":
    garbage = ["G","P","GP","GG"]
    travel = [2,4,3]
    result = Solution().garbageCollection(garbage,travel)
    print(result)
