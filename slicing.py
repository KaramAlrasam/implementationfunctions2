a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def slicing(a_list, step):
  return [a_list[i::step]for i in range(step)]
print(slicing(a,3))