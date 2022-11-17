from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        invalid_indices = set()
        for index, triplet in enumerate(triplets):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                invalid_indices.add(index)

        valid_triplets = [trip for i, trip in enumerate(triplets) if i not in invalid_indices]
        zipped = list(zip(*valid_triplets))
        if not zipped:
            return False
        first = set(zipped[0])
        second = set(zipped[1])
        third = set(zipped[2])

        return target[0] in first and target[1] in second and target[2] in third