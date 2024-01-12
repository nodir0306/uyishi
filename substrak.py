#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
def subtractProductAndSum(self, n):
        sum = 0
        multiple = 1
        while n > 0:
            digit = n % 10
            multiple *= digit
            sum += digit
            n //= 10
        return (multiple - sum)