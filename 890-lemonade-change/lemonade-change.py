class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, two = 0, 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif  i == 10:
                ten += 1
                if five ==0:
                    return False
                else:
                    five -= 1
                
            elif  i == 20:
                two += 1
                if ten ==0 :
                    if five < 3:
                        return False
                    else:
                        five -=3
                elif ten != 0:
                    if five == 0:
                        return False
                    else:
                        ten -= 1
                        five -= 1
        return True