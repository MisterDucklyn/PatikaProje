def reverse(liste):
        for eleman in range(len(liste)):
          liste.reverse()
          if isinstance(liste[eleman], list):
            liste[eleman].reverse()
            return liste
       
list1 = [[1, 2], [3, 4], [5, 6, 7]]        
print(reverse(list1))
