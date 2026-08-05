class Solution:
    def average(self, salary: List[int]) -> float:
        nums=[]
        for num in salary:
            if num!=min(salary) and num!=max(salary):
                nums.append(num)
        return sum(nums)/len(nums)