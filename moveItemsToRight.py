a=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
sorted=sorted(a, key= lambda item: not item)
print(sorted)


def moveItemss(m_list:list, item)->list:
  """It is in charge to move whole items in the left of list to the right"""
  #count items in the list and save it in the variable
  if item not in m_list: 
    raise ValueError (f"{item} is not existent")
  num=m_list.count(item)
  #make for loop on the list and delete whole spcified items
  for i in range(len(m_list)-1,-1,-1):
    if m_list[i]==item:
      del m_list[i]
  m_item=[item for _ in range(num)]
  return m_list+m_item
print("="*20)
print(moveItemss(a,0))  

