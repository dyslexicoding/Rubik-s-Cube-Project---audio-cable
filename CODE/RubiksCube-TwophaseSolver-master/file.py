


array = ["U", "U", "U", "U", "U", "U", "R", "R", "R", "D", "R"
         , "R", "D", "R", "R", "D", "R", "R", "F", "F", "F", "F", "F", "F"
         , "F", "F", "F", "L", "L", "L", "D", "D", "D", "D", "D", "D"
         , "L", "L", "U", "L", "L", "U", "L", "L", "U"
         , "B", "B", "B", "B", "B", "B" , "B", "B", "B"]


def run():
     f= open("cubestring.txt","w+")
     for x in range(0, len(array),1):
          print (x)
          print(array[x])
          f.write(array[x])
     f.close()
     return ("yay")
