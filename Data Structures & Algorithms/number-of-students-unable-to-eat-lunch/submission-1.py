class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        want_0 = 0
        want_1 = 0
        for st in students:
            if st == 0:
                want_0 += 1
            else:
                want_1 += 1
        for s in sandwiches:    
            if s == 0:
                if want_0 > 0:
                    want_0 -= 1
                else:
                    return want_1
            else:
                if want_1 > 0:
                    want_1 -= 1
                else:
                    return want_0
        return 0
