from itertools import groupby
from operator import itemgetter
def test(m_list:list)->list:
  #use dictionary to save the letter as key and the value as the words start
  #with the letter
  for l, words in groupby(sorted(m_list),key=lambda item: item[0]):
    print(l)
    for w in words:
      print(w)
    print("="*5)

word_list = ['be',"body",'have','do','say','get','make','go','know','take','see','come','think',
       'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
test(word_list)