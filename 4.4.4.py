#defining the factorial function to use in exponential function
def pro(x):
 fact=1
 for i in range(x):
     fact = fact*(i+1)
 return fact

  y = input('power of exponential')
  for j in range(10):
        y=(y**j)/pro(j)
  print(y)

