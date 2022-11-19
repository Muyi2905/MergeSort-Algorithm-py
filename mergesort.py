def merge(listA, listB):
    newlist = list()
      a = 0
    b = 0
      while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
              newlist.append(listA[a])
            a += 1