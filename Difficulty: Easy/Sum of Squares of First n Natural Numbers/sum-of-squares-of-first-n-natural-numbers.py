#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        result = 0
        while number > 0:
            result += number**2
            number-=1
        return result