class Solution:
    def countSquares(self, matrix):
        a = matrix
        count = 0
        row_num = len(a)
        col_num = len(a[0])
        mc = 0
        mr = 0

        for mr in range(row_num):
            for mc in range(col_num):
                for side in range(min(row_num-mr, col_num-mc)):
                    heng = 0 in a[mr+side][mc:mc+side+1]
                    shu = 0 in [a[i][mc+side] for i in range(mr,mr+side+1)]
                    if heng or shu:
                        break
                    else:
                        count += 1










        return count

test_matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
#test_matrix = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
test_num = 15
solution = Solution()
result = solution.countSquares(test_matrix)
print(test_matrix)
if result == test_num:
    print("Right! The number of square submatrices is :" + str(result))
else:
    print("Opps...Correct number is " + str(test_num) + ", and your result is " + str(result))