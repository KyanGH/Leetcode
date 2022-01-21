class Solution(object):
    def subtractProductAndSum(self, n):
        sumn = 0
        product = 1
        while n != 0 :
            sumn += n % 10
            product *= n % 10
            n = n // 10
        return product - sumn
        