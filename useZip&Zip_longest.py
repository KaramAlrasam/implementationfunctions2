from itertools import zip_longest
a=["Black", "Red", "Maroon", "Yellow"]
b=["#000000", "#FF0000", "#800000", "#FFFF00"]
def test(a_list, b_list)->dict:
  """It merge two elments togather in dictionary"""
  merge= zip_longest(a_list, b_list, fillvalue="_")
  m_list=[]
  for values in list(merge):
    dic={}
    dic["color_name"]=values[0]
    dic['color_code']=values[1]
    m_list+=[dic]
  return m_list
print(test(a,b))
print("="*20)

def test2(a_list, b_list)->list:
  """It merge two elments togather in dictionary"""
  return [{"color_name":a, "color_code":b}for a, b in zip(a_list, b_list)]
print(test2(a,b))