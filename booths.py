def flip(s): #flips bits
  if s == "0":
    return "1"
  else:
    return "0"

def mul(A, B):
  nA = A.bit_length() #bits of A
  nB = B.bit_length() #bits of B

  toReturn = ""
  toReturn += "A: " + str(A) + "\n"
  toReturn += "B: " + str(B) + "\n"
  toReturn += "Actual Answer: " + str(A*B) + "\n"*2

  
  formatter = "{0:0" + str(nA + nB + 2) + "b}" #define formatter

  A = A * 2**(nB+2) #nB + 2 of space

  P = B << 1 #P = B, fill in LSB with a 0

  spaceOffset = len(str(nB)) #for formatting output

  for x in range(nB+1):
    test = P & 3 #gets the last 2 bits

    if test == 2: #10
      P -= A
    if test == 1: #01
      P += A
    
    P = P >> 1
    temp = P
    toPrint = str(formatter.format(temp))
    s = str(toPrint)
    if P < 0:
      temp = map(flip, s)
      temp = "".join(temp)
      news = formatter.format(int(temp, 2) + 1)
      toPrint = news

    spaceUnOffset = len(str(x))
    toReturn += "Pass " + str(x) + ((spaceOffset - spaceUnOffset) * " ") + " -- Binary P: " + toPrint + " -- Actual P: " + str(P) + "\n"

  mask = 2**(nA + nB + 1 + 1) - 1 #make the mask
  P = P & mask #mask nA + nB + 1 bits
  P = P >> 1 #remove myth bit_length

  toReturn += "Calculated Answer: " + str(P)
  return toReturn
