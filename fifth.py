start, end, step = input("Enter start, end and step value: ").split()
for n in range(int(start), int(end),int(step)):
    #print('{0:<5}{1:<7}{2:<8}'.format(n,n**2,n**3))
    print('{0:>5}{1:>7}{2:>8}'.format(n,n**2,n**3))
