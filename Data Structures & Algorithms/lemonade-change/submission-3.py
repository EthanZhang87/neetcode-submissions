class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5: 0, 10: 0, 20: 0}

        for x in bills:
            if x == 5:
                count[5] += 1

            elif x == 10:
                if count[5] > 0:
                    count[10] += 1
                    count[5] -= 1

                else:
                    return False
            else:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1

                elif count[10] <= 0 and count[5] > 2:
                    count[5] -= 3
                else:
                    return False

        return True

        