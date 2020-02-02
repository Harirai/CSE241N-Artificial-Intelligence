def read_matrix(filename):
	with open(filename, "r") as f:
		matrix = f.readlines()
		for i,row in enumerate(matrix):
			matrix[i] = list(map(int,matrix[i].split(",")))
	return matrix

def write_matrix(filename, solved_matrix):
	with open(filename, "w") as f:
		f.writelines(','.join(str(j) for j in i) + '\n' for i in solved_matrix)
	print(filename+" for backtracking generated.")

class sudoku():
	def __init__(self, filename):
		self.matrix = read_matrix(filename)
	
	def iRow(self, n, row):
		for i in range(9):
			if self.matrix[row][i] == n :
				return True

		return False
			
	def iCol(self, n, col):
		for j in range(9):
			if self.matrix[j][col] == n :
				return True
		return False


	def iBox(self, n, row, col):
		for i in range(3):
			for j in range(3):
				if(self.matrix[i+row][j+col] == n):
					return True
		return False

	def empty(self, a):
		for i in range(9):
			for j in range(9):
				if self.matrix[i][j] == 0 :
					a[0] = i
					a[1] = j
					return True

		return False

	def check(self, row, col, n):
		return not self.iRow(n, row) and not self.iCol(n, col) and not self.iBox(n, row - row%3, col - col%3)

	def solve(self):
		''' WRITE YOUR CODE HERE
			self.matrix contains the 2-D sudoku array.
			Entries having zero need to filled in.
			You can create additional functions that will support this main bactracking function.
		'''
		a = [0, 0]
		if(not self.empty(a)):
			return True

		for n in range(9):
			r, c = a[0], a[1]
			if(self.check(r, c, n+1)):
				self.matrix[r][c] = n+1

				if(self.solve()):
					return True

				self.matrix[r][c] = 0

		return False

	def singleDigit(self):

            for a in range(9):

                    for b in range(9):

                        if(not self.matrix[a][b]):
                            c=0
                            for d in range(1,10):
                                if(self.check(a,b,d)):
                                    c= c + 1
                                    xxx=d
                            if(c==1):
                                self.matrix[a][b]=xxx
                                return True
            return False

	def iiRow(self):

		for i in range(9):
			for d in range(1,10):
					c=0
					for j in range(9):
						if(not self.matrix[i][j] and self.check(i,j,d)):
							x=d 

							c=c+1
							
							l=j
					if(c==1):
						self.matrix[i][l]=x
						return True
		return False

	def iiCol(self):
			for i in range(9):
				for d in range(1,10):
					c=0
					for j in range(9):
						if(not self.matrix[j][i] and self.check(j,i,d)):
							
							x=d
							l=j
							c= c+ 1
					if(c==1):
						self.matrix[l][i]=x
						return True
			return False

	def iiBox(self):
			for i in range(0,9,3):
					for j in range(0,9,3):
						for d in range(1,10):
							cc=0
							for a in range(3):
								for b in range(3):
										if(not self.matrix[i+a][j+b] and self.check(i+a,j+b,d)):
											
											iCol=j+b

											iROW=i+a
											
											x=d
											cc = cc + 1
							if(cc==1):
								self.matrix[iROW][iCol]=d
								return True
			return False

	def fill(self):
			myanswer=10
			for i in range(9):
				for j in range(9):
					cc=0
					if(not self.matrix[i][j]):
						for DD in range(1,10):
							if(self.check(i,j,DD)):
								
								x=DD
								cc= cc + 1
						if(cc<myanswer):
							myanswer=cc
							iROW=i
							iCOL=j
							PUT=x
			if(myanswer==10):
				return False
			self.matrix[iROW][iCOL]=PUT
			return True
			 

	def solve_without_backtracking(self):
		''' WRITE YOUR CODE HERE
			Fill in this function using any algorithm other than backtracking.
			You can implement CSP or any other algo.
		'''
		i = 0

		if(self.singleDigit()):

			self.solve_without_backtracking()
		elif(self.iiRow()):
			self.solve_without_backtracking()
		elif(self.iiCol()):
			self.solve_without_backtracking()
		elif(self.iiBox()):
			self.solve_without_backtracking()
		elif(self.fill()):
			self.solve_without_backtracking()
		else:
            
			return i         
		'''END YOUR CODE HERE'''
		#raise NotImplementedError("You need to fill the non-backtracking function") 

if __name__=="__main__":
	su = sudoku("data.txt")
	su.solve()
	write_matrix("sol.txt", su.matrix)
	try:
		su = sudoku("data.txt")
		su.solve_without_backtracking()
		print("Solved sudoku matrix without backtracking:")
		for i in range(9):
			print(*su.matrix[i], sep=" ")
	except Exception as e:
		print(e)



