class Solution:
	def neighbours_count(self,arr, r, c):
		rows = len(arr)
		cols = len(arr[0])
		neighbours = 0
		for i in range(r-1, r+2):
			for j in range(c-1, c+2):
				if ((i == r) and (j == c)) or i < 0 or j < 0 or i == rows or j == cols:
					continue
				if arr[i][j] == 1:
					neighbours += 1
		return neighbours

	def game_of_life(self,array, board_size):
		sol_arr = [[0 for i in range(0,board_size)] for j in range(0,board_size)]
		for row in range(0,len(array)):
			for col in range(0,len(array[0])):
				nei = self.neighbours_count(array,row,col)
				if array[row][col] == 1:
					if nei in [2,3]:
						sol_arr[row][col] = 1
					elif nei < 1 or nei > 3:
						sol_arr[row][col] = 0
				else:
					if nei == 3:
						sol_arr[row][col] = 1
		print(f"Next State: {sol_arr}")





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
sol.game_of_life(board,size_of_board)