a=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
def flatting_list(m_list:list)->list:
  """It is in charge to convert shalow list into flat list"""
  #make empty list
  res=[]
  #make condition if the list is False
  if not m_list:
    return res
  #convert the stack into lis if it was something else
  stack=[list(m_list)]
  #make while loop and let the stack its condition
  while stack:
    #use pop()twice to git rid of the brackets
    c_num=stack.pop()
    #use pop() one more time for the nested list
    next=c_num.pop()
    #make condition for the c_num if it was list and append it to the stack again
    if c_num:
      stack.append(c_num)
    if isinstance(next,list):
      if next:
        stack.append(next)
    else:
      res.append(next)
  res.reverse()
  return res
# print(flatting_list(a))
