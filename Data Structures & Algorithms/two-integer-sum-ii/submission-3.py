class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l + 1, r + 1]  # Return 1-based indices
            elif current_sum < target:
                l += 1  # Move left pointer to the right to increase the sum
            else:
                r -= 1  # Move right pointer to the left to decrease the sum
        return []  # If no solution is found, return an empty list

