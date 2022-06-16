class Solution:
    def neighbours_count(self,arr, r,c):
        rows = len(arr)
        cols = len(arr[0])
        neighbours = 0
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if ((i==r) and (j==c)) or i<0 or j<0 or i==rows or j==cols:
                    continue
                if arr[i][j] in [1,3]:
                    neighbours += 1
        return neighbours
    def game_of_life(self,array):
        for row in range(0,len(array)):
            for col in range(0,len(array[0])):
                neighbours = self.neighbours_count(array,row,col)
                if array[row][col]:
                    if neighbours in [2,3]:
                        array[row][col] = 3
                elif neighbours == 3:
                        array[row][col] = 2
        for row in range(0,len(array)):
            for col in range(0,len(array[0])):
                if array[row][col] == 1:
                    array[row][col] = 0
                elif array[row][col] == 2 or array[row][col] == 3:
                    array[row][col] = 1
        print(f"Next State: {array}")


co_ordinates = []
num_of_co_ordinates = int(input("enter number of co-ordinates: "))
for x in range(0,num_of_co_ordinates):
    co_ordinates.append([int(i) for i in input(f"enter co-ordinate {x+1}: ").split(",")])
size_of_board = max(map(max, co_ordinates)) + 1
board = [[0 for i in range(0,size_of_board)] for j in range(0,size_of_board)]
for co_ordinate in co_ordinates:
    board[co_ordinate[0]][co_ordinate[1]] = 1
print(f"Initial State: {board}")
sol = Solution()
sol.game_of_life(board)