#import groupby
from itertools import groupby 
def test(m_list):
  # it is in charge to find out the length of list[0]greader than 1 or not 
  def test2(group):
    if len(group[0])>1:
      return [len(group[0]),group[1]]
    else:
      return group[1]
  return [test2([list(g),k])for k, g in groupby(m_list)]

a=[1, 1, 2, 3, 4, 4, 5, 1]
b="aabcddddadnss"
print(test(a))
print(test(b))
