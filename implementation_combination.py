def combination(n:int , m_list:list)->list:
  """It is in charge to generate every sublist posiable"""
  #create condition if the n is less or == to zeron it gets out of the function
  if n<=0:
    yield []
    return
  #make nested for loop 
  for i in range(len(m_list)):
    pr1=m_list[i:i+1]#is gives you one element

    for x in combination(n-1,m_list[i+1:]):
      yield pr1+x


a= [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for x in combination(3,a):
  print(x)