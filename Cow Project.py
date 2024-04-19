cows = ["G", "H", "H", "G", "G", "H", "G", "H", "H", "H", "G", "H", "H", "G", "G", "G", "H", "G", "H", "G", "G", "H", "H", "G", "H", "H", "H", "G", "G", "H"] #This is the list of the cows
starting = 0                                     #This is a variable that helps to take out the bad pictures at the start
ending = 0                                       #This is a variable that helps to take out the bad pictures at the end
bad = 0                                          #This is the number of bad pictures
count = 30                                       #This is the number of cows

count = len(cows)                                #This defines count as the length of cows
for va in range (1, count - 1):                  #This is a loop that starts at 1 and ends at the count or 30
  for vb in range (va + 2, count + 1):           #This is another loop that adds 2 to the first loop because the starting amount is 2
    starting = va                                #This states that the starting amount is the first loop's variable
    ending = vb                                  #This states that the ending amount is the secong loop's variable
    g = 0                                        #This line of code states that a new variable, g is 0
    h = 0                                        #This line of code states that a new variable, h is 0
    for vc in range (starting, ending + 1):      #This line is another loop that starts at starting, or the first loop and ends at ending, or the secong loop
      if cows[int(vc - 1)] == "G":               #This states that if in a picture, there is a singular cow:
        g = g + 1                                #This line adds one to g
      else:                                      #This line says that if the first criteria doesn't work then:
        h = h + 1                                #This line adds one to h
    if g == 1 or h == 1:                         #This line says that if g or h is equal to 1
      bad = bad + 1                              #This line says to add one to the bad pictures
print("discarded pics = " + str(bad))            #This line says to print "discarded pics  = " plus the number of bad pics.
