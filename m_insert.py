def m_insert(m_list:list, item, index:int)->list:
  """It is in charge to insert item to the list dibands on the user's index"""
  if index not in range(len(m_list)):
    return

  return m_list[:index]+[item]+m_list[index:]
item = 12
a=[1, 1, 2, 3, 4, 4, 5, 1]
print(a)
print(m_insert(a,item,2))