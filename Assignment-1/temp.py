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

        def solve(self):
                empty=[]
                for i in range(9):
                        for j in range(9):
                                if(not self.matrix[i][j]):
                                        empty.append([i,j])
                self.back_track(0,empty)

        def safe(self,row,col,a):
                #Checking row
                for i in range(9):
                        if(self.matrix[row][i]==a):
                                return False
                #Checking col
                for i in range(9):
                        if(self.matrix[i][col]==a):
                                return False
                #Check box
                rowbox=row-(row%3)
                colbox=col-(col%3)
                for i in range(rowbox,rowbox+3):
                        for j in range(colbox,colbox+3):
                                if(self.matrix[i][j]==a):
                                        return False
                #Kuch galat nahi hua
                return True                

        def back_track(self,i,empty):
                if(i==len(empty)):
                        return True

                idhar=empty[i][0]
                udhar=empty[i][1]
                for j in range(9):
                        if(self.safe(idhar,udhar,j+1)):
                                self.matrix[idhar][udhar]=j+1
                                if(self.back_track(i+1,empty)):
                                        return True
                                self.matrix[idhar][udhar]=0
                return False
                                    

        def onedigitonly(self):
            for i in range(9):
                    for j in range(9):
                        if(not self.matrix[i][j]):
                            counter=0
                            for digit in range(1,10):
                                if(self.safe(i,j,digit)):
                                    counter+=1
                                    x=digit
                            if(counter==1):
                                self.matrix[i][j]=x
                                return True
            return False

        def RowMaiDekho(self):
            for i in range(9):
                for digit in range(1,10):
                    counter=0
                    for j in range(9):
                        if(not self.matrix[i][j] and self.safe(i,j,digit)):
                            counter+=1
                            x=digit
                            l=j
                    if(counter==1):
                        self.matrix[i][l]=x
                        return True
            return False

        def ColMaiDekho(self):
            for i in range(9):
                for digit in range(1,10):
                    counter=0
                    for j in range(9):
                        if(not self.matrix[j][i] and self.safe(j,i,digit)):
                            counter+=1
                            x=digit
                            l=j
                    if(counter==1):
                        self.matrix[l][i]=x
                        return True
            return False
            
        def SquareMaiDekho(self):
            for i in range(0,9,3):
                    for j in range(0,9,3):
                        for digit in range(1,10):
                            counter=0
                            for a in range(3):
                                for b in range(3):
                                        if(not self.matrix[i+a][j+b] and self.safe(i+a,j+b,digit)):
                                            counter+=1
                                            indexrow=i+a
                                            indexcol=j+b
                                            x=digit
                            if(counter==1):
                                self.matrix[indexrow][indexcol]=digit
                                return True
            return False

        def KuchBharo(self):
            ans=10
            for i in range(9):
                for j in range(9):
                    counter=0
                    if(not self.matrix[i][j]):
                        for digit in range(1,10):
                            if(self.safe(i,j,digit)):
                                counter+=1
                                x=digit
                        if(counter<ans):
                            ans=counter
                            indexrow=i
                            indexcol=j
                            put=x
            if(ans==10):
                return False
            self.matrix[indexrow][indexcol]=put
            return True
             

        def solve_without_backtracking(self):
            if(self.onedigitonly()):
                self.solve_without_backtracking()
            elif(self.RowMaiDekho()):
                self.solve_without_backtracking()
            elif(self.ColMaiDekho()):
                self.solve_without_backtracking()
            elif(self.SquareMaiDekho()):
                self.solve_without_backtracking()
            elif(self.KuchBharo()):
                self.solve_without_backtracking()
            else:
                return                           
                                 


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