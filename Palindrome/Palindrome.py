#############  Checking Palindrome words in Python  ##############
#############  By : s3tanc0d3r@gmail.com  ###################### 




#!/usr/bin/python
import sys


if len(sys.argv) <= 2 or len(sys.argv) > 3 :
 print"usage : ./palindrome [words1] [words2]"
else:
  array = {}
  array[0] = sys.argv[1]
  array[1] = sys.argv[2]
  if len(array[0]) != len(array[1]) :
    print "Is Not Palindrome"
  else:
    i=0
    mark = "true"
    sum = len(array[0])
    while i < sum :
      if array[0][i] != array[1][(sum-1)-i] :
          mark = "false"
          break
      else:
       i+=1
    if mark == "true" :
       print "Palindrome"
    elif mark == "false" :
       print "Is not Palindrome"
