def generate_groups(start, end, group_size):
  return [[i for i in range(j,j+group_size)]for j in range(start, end, group_size)]

m_list = generate_groups(1, 26, 5)

print(m_list)
print("="*20)
m_list2=[[5*i+j for j in range(1,6)]for i in range(5)]
print(m_list2)