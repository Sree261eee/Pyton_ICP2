class solution:
    def numberofsteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -=1
            steps += 1
        return steps

ans = solution()
print("\n The number of steps to reduce to zero are : ",ans.numberofsteps(14))
