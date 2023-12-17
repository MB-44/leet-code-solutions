from collections import defaultdict
import heapq
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.cuisine2Heap = defaultdict(list)
        self.food2Cuisine = {}
        self.food2Rating = defaultdict(int)
        for i in range(len(foods)):
            self.food2Cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine2Heap[cuisines[i]], (-ratings[i], foods[i]))
            self.food2Rating[foods[i]] = -ratings[i]
        

    def changeRating(self, food, newRating):
        cuisine = self.food2Cuisine[food]
        heapq.heappush(self.cuisine2Heap[cuisine], (-newRating, food))
        self.food2Rating[food] = -newRating

    def highestRated(self, cuisine):
        smallestLexico = None
        while len(self.cuisine2Heap[cuisine]) > 0:
            curr = self.cuisine2Heap[cuisine][0]
            if curr[0] != self.food2Rating[curr[1]]:
                # delete old data
                heapq.heappop(self.cuisine2Heap[cuisine])
                continue
            smallestLexico = curr[1]
            break
        return smallestLexico