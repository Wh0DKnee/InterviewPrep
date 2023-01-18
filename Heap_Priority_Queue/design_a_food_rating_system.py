from typing import List
from collections import defaultdict
import heapq


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # for each cuisine we maintain a heap with (rating, food) entries
        self.cuisines = defaultdict(list)
        # so that we know what cuisine a food belongs to in changeRating
        self.food_to_cuisine = {}
        # for each cuisine heap, we keep an entry_finder to find an entry in constant time
        self.entry_finders = defaultdict(dict)
        self.removed = '<removed>'

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_to_cuisine[food] = cuisine

            entry = [-rating, food]
            self.entry_finders[cuisine][food] = entry
            heapq.heappush(self.cuisines[cuisine], entry)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        entry = self.entry_finders[cuisine][food]
        entry[1] = self.removed
        new_entry = [-newRating, food]
        self.entry_finders[cuisine][food] = new_entry
        heapq.heappush(self.cuisines[cuisine], new_entry)

    def highestRated(self, cuisine: str) -> str:
        while self.cuisines[cuisine]:
            rating, food = self.cuisines[cuisine][0]
            rating *= -1
            if food == self.removed:
                heapq.heappop(self.cuisines[cuisine])
            else:
                return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)