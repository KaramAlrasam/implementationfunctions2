def uniqueItems(a_list:list, b_list:list)->list:
  set1=set(a_list)
  set2=set(b_list)
  res1=set1 - set2
  res2=set2 - set1
  return f"Missing values in second list: {', '.join(list(res1))}\nAdditional values in second list: {', '.join(list(res2))}"
a=['a', 'b', 'c']
b=['g', 'h']
print(uniqueItems(a, b))

def uniqueItems2(a_list:list, b_list:list)->list:
  uni=set(a_list).difference(b_list)
  idd=set(b_list).difference(a_list)
  return (
f"""
Missing values in second list: {', '.join(uni)}
Additional values in second list: {', '.join(idd)}
"""    
  )
print(uniqueItems2(a,b))