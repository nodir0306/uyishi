#https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(self,marvarid, tosh):
        lst = []
        sum = 0
        lst.extend(marvarid)
        result = ''
        for i in range(len(marvarid)):
            sum += tosh.count(lst[i])
        return sum