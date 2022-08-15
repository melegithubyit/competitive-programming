class Solution(object):
    def fizzBuzz(self, n):
        output = []
        for i in range(1,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("Fizzbuzz")
            elif i % 5 == 0:
                output.append("Buzz")
            elif i % 3 == 0:
                output.append("Fizz")
            else:
                output.append(i)

        return output


trial = Solution()
print(trial.fizzBuzz(6))