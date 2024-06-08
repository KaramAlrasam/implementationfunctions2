def exersize_using_matrix():
  #make matrix dibands on the size of the number which comes from the user
  size=int(input("Enter the size of the matrix: ").strip())
  #make matrix
  print(f"Enter {size} numbers saperated with spaces in the {size} lines")
  matrix=[[0]*size for _ in range(size)]
  #now make for loop and aske from the user to input number
  for x in range(size):
    line=list(map(int,input().split()))
    #make for loop and fill the matrix with result from line
    for y in range(size):
      matrix[x][y]=line[y]
  #return the sum from the drignal matrix by making fomila to each index
#Ex:
#matrix=[
#[1,2,3]
#[2,3,4]
#[3,4,5]]
#size=3
#matrix[size-0-1][size-0-1]#1
#matrix[size-1-1][size-1-1]#2
#matrix[size-2-1][size-2-1]#3
#
  print("\nThe result:\n")
  return sum(matrix[size-i-1][size-i-1]for i in range(size))


print(exersize_using_matrix())
    