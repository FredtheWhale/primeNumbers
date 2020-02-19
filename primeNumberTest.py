
#!/bin/python3

import time
import os

prime=[2, 3]
i=1
candidate=5
join = ", "



folderLocation = "c:/primeTest/"
primeName = "primeNumbers.txt"
notPrimeName = "noPrimeNumbers.txt"

primePath=folderLocation + primeName
notPrimePath=folderLocation + notPrimeName

# print (primePath)




# check to see if the prime file has been created
if os.path.isfile(primePath):

	#
	# if the prime file exists, load it
	# candidate will retain the highest value
	# and that's where the testing will start
	#
	with open(os.path.join(primePath), "r") as add2list:
		hold = add2list.read()
		prime = hold.split(", ")
		last=len(prime)
		# convert the string values to integers
		for i in range (0,last):
			prime[i]=int(prime[i])
		candidate=prime[last-1]
		
		
# print (last)
# print (prime[10])
# print (candidate)

	
# check to see if the prime folder has beeen created
if os.path.isdir(folderLocation) is False:
	# if false, create the folder
	os.makedirs(folderLocation)
	# print ("directory created")
	
	# create the file	
	with open(os.path.join(primePath), "w") as add2file:
		content="2, 3"
		add2file.write(content)
		# print ("created prime file")	
		
		
		
# check to see if the non prime file has been created
if os.path.isfile(notPrimeName) is False:
	# if false, create the file
	with open(os.path.join(notPrimePath), "w") as add2file:
		content="4"
		add2file.write(content)
		# print ("created non prime file")







#
#	test4Prime function 
#	this function is the main process where it tests numbers for prime
#



#	prime = [2,3]
#	prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#   prime = [2, 3, 5, 7, 11, 13]

#	long=len(prime)



while i > 0:
	
	i = 1
	x = "True"
	
	# print ("this has been reset")
	# print ("i=",i)
	# print ("x=",x)
	# print ("end of reset message")
	# print ("")

	
	while x=="True": 
		# print ("candidate is", candidate)
		# print ("prime to test is", prime[i])
		
		
		# print(candidate,"/", prime[i],"=",candidate%prime[i])
			
		
		
		# % (aka modulus) returns the remainder from a division
		if candidate%prime[i] == 0:
			# print ("candidate is not prime -->", candidate)
			with open(os.path.join(notPrimePath), "a") as add2file:
				append = join + str(candidate)
				add2file.write(append)
			
		
			print ("candidate is not prime -->", candidate)
			candidate+=2
			x = "False"

		
		
		# increment the counter
		i+=1
		
		
		# test for end of the array
		# if this is the end of the array then candidate is prime
		try:	
			test=prime[i]	
			
		except:
			with open(os.path.join(primePath), "a") as add2file:
				append = ", " + str(candidate)
				add2file.write(append)
			# print ("PRIME IDENTIFIED --->", candidate)
			
			prime.append(candidate)
			print("ARRAY HAS BEEN UPDATED WITH", candidate)			

			x="False"
			candidate+=2



		# print ("i=",i)
		# print ("x=",x)
		# print ("")
		# time.sleep(2)



#
#	end of main program 
#
