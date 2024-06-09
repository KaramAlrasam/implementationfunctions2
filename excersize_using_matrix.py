def excersize_using_matrix():
  #we will twke two inputs from the user to create the size of the matrix
  rows=int(input("Enter the number row of matrix size: ").strip())
  columns=int(input("Enter the number column of matrix size: ").strip())
  #create matrix
  matrix=[[0]*columns for _ in range(rows)]
  #create for loop to ask the user enter numbers even to update matrix
  print("Enter numbers saperated with spaces\n")
  for x in range(rows):
    line=list(map(int,input().split()))
    #make another for loop to update matrix with the result of line
    for y in range(columns):
      matrix[x][y]=line[y]
  #to sum the matrix thier colcumns make list its name sum and update it 
  sum=[0]*columns
  #make for loop to update the items of sum 
  for col in range(columns):
    for row in range(rows):
      sum[col]+=matrix[row][col]
  print("The result\n")
  return sum

print(excersize_using_matrix())