width = int(input("type the retangle's width: "))
height = int(input("type the retangle's height: "))
for i in range(0,height,1):
  if(i ==0 or i==(height-1)):
    for j in range(0, width, 1):
      print("* ", end="")
    print()
  else:
    for j in range(0, width, 1):
      if(j==0 or j==(width-1)):
        print("* ", end="")
      else:
        print("  ", end="")
    print()

