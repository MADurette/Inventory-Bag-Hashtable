#Made By Marcus A Durette

import os
import csv
import random
import time

#Path to Python file
dir_path = os.path.dirname(os.path.realpath(__file__))
PATH = dir_path + '\\Input.txt'

class Node():
	def __init__(self,itemnode,nextNode):
		self.itemnode = itemnode
		self.nextNode = nextNode
		
	def getItem(self):
		return self.itemnode

	def setItem(self,value):
		self.itemnode = value

	def getnextNode(self):
		return self.nextNode

	def setnextNode(self,value):
		self.nextNode = value
	#Remember returns memory location need to use str() to change it into a string to see it

class ItemLinkedList():
	def __init__(self,head = None,tail = None):
		self.head = head
		self.tail = tail
		self.size = 0
		
	def addNode(self,node):
		newNode = node
		newNode.nextNode = self.head
		self.tail = self.head
		self.head = newNode
		self.size+=1
		return newNode
			
	def printAllNodes(self):
		curr = self.head
		while curr:
			print(curr.nucleotide, end ="")
			curr = curr.getNextNode()

def Hashingprobe2(closed,inserttotable,sizeofhashingtable,tablenum):
	timebefore = time.time()
	bagcount = 0
	start=0
	list=[]
	counter = 0
	for ite in bags:
		for intem in bags[bagcount]:
			stre = intem[4]
			hash = stre % sizeofhashingtable
			counter = 0
			if(inserttotable[hash]!= 'Empty'):
				while(counter != sizeofhashingtable):
					if(hash<sizeofhashingtable):
						hash=hash+27
					if(hash>sizeofhashingtable):
						hash=start
						start+=1
					if(hash>sizeofhashingtable):
						hash = 0
					if(inserttotable[hash] == 'Empty'):
						if(closed == False):
							inserttotable[hash] = intem
						else:
							list = []
							list.append(intem)
							inserttotable[hash] = list
					counter+=1
			else:
				if(closed == False):
					inserttotable[hash] = intem
				else:
					list.append(intem)
					inserttotable[hash] = list
		bagcount += 1
	print()
	print('Second Probing Method for table:' + str(tablenum))
	print()
	hash = stre % sizeofhashingtable
	itemnotthere = True
	for all in range(sizeofhashingtable):
		if(closed == True):
			if(inserttotable[hash]!='Empty'):
				if(inserttotable[hash][0] == itemcheckname and inserttotable[hash][3] == itemcheckrarity):
					if(itemnotthere == True):
						print('---Found item in Hashtable at slot:'+str(hash)+'---')
					itemnotthere = False
			else:
				if(hash<sizeofhashingtable):
					hash=hash+27
				if(hash>sizeofhashingtable):
					hash=start
					start+=1
				if(hash>sizeofhashingtable):
					hash = 0
		else:
			for all in inserttotable[hash]:
				if(all != 'Empty'):
					if(all[0] == itemcheckname and all[3] == itemcheckrarity):
						if(itemnotthere == True):
							print('---Found item in Hashtable at slot:'+str(hash)+'---')
						itemnotthere = False
				else:
					if(hash<sizeofhashingtable):
						hash=hash+27
					if(hash>sizeofhashingtable):
						hash=start
						start+=1
					if(hash>sizeofhashingtable):
						hash = 0
					
	if(itemnotthere == True):
		print('---Item not located in Hashtable---')
	timeafter = time.time()
	totaltime = timeafter - timebefore
	print()
	print('Time:' + str(totaltime))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def Hashingprobe3(closed,inserttotable,sizeofhashingtable,tablenum):
	timebefore = time.time()
	bagcount = 0
	start=0
	list=[]
	counter = 0
	exit = False
	for ite in bags:
		for intem in bags[bagcount]:
			stre = intem[4]
			hash = stre % sizeofhashingtable
			counter = 0
			if(inserttotable[hash]!= 'Empty'):
				while(counter != sizeofhashingtable or exit == True):
					hash = primes[hash % len(primes)]
					hash = hash % sizeofhashingtable
					if(inserttotable[hash] == 'Empty'):
						if(closed == True):
							inserttotable[hash] = intem
							exit = True
						else:
							list = []
							list.append(intem)
							inserttotable[hash] = list
							exit = True
					counter+=1
			else:
				if(closed == False):
					inserttotable[hash] = intem
				else:
					list.append(intem)
					inserttotable[hash] = list
		bagcount += 1
	print()
	print('Third Probing Method for table:' + str(tablenum))
	print()
	hash = stre % sizeofhashingtable
	itemnotthere = True
	for all in range(sizeofhashingtable):
		if(closed == True):
			if(inserttotable[hash] != 'Empty'):
				if(inserttotable[hash][0] == itemcheckname and inserttotable[hash][3] == itemcheckrarity):
					if(itemnotthere == True):
						print('---Found item in Hashtable at slot:'+str(hash)+'---')
					itemnotthere = False
			else:
				hash = primes[hash % len(primes)]
				hash = hash % sizeofhashingtable
				if(inserttotable[hash] == 'Empty'):
					if(closed == True):
						inserttotable[hash] = intem
						exit = True
					else:
						list = []
						list.append(intem)
						inserttotable[hash] = list
						exit = True
				
		else:
			for all in inserttotable[hash]:
				if(all != 'Empty'):
					if(all[0] == itemcheckname and all[3] == itemcheckrarity):
						if(itemnotthere == True):
							print('---Found item in Hashtable at slot:'+str(hash)+'---')
						itemnotthere = False
				else:
					hash = primes[hash % len(primes)]
				hash = hash % sizeofhashingtable
				if(inserttotable[hash] == 'Empty'):
					if(closed == True):
						inserttotable[hash] = intem
						exit = True
					else:
						list = []
						list.append(intem)
						inserttotable[hash] = list
						exit = True
					
	if(itemnotthere == True):
		print('---Item not located in Hashtable---')
	timeafter = time.time()
	totaltime = timeafter - timebefore
	print()
	print('Time:' + str(totaltime))

itemsarray = []
itemsinbags = []

with open(PATH) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		count = 0
		for row in csv_reader:
			item = list()
			if count == 0:
				count += 1
			else:
				item.append(row[0])
				itemstrmin = row[1]
				itemstrmax = row[2]
				itemstr = random.randint(int(itemstrmin),int(itemstrmax))
				item.append(itemstrmin)
				item.append(itemstrmax)
				item.append(row[3])
				item.append(itemstr)
			#print(item)
			itemsarray.append(item)
#print(itemsarray)

print()
amtbags = int(input('How many Bags do you want made?\n'))
counter = 0
print()
bags = []
#in order to create bag size
while(len(bags) != counter):
	bags.append[counter]
	counter += 1

amtitems = amtbags*125
for n in range(amtbags):
	itemsinbags = []
	counter = 0
	while(counter != 125):
		itemsinbags.append(0)
		counter += 1
	counter = 0
	for i in range(125):
		randomitem = random.randint(1,len(itemsarray)-1)
		#print(itemsarray[randomitem])
		itemsinbags[counter] = itemsarray[randomitem]
		counter+=1
	bags.append(itemsinbags)
#print(bags)	

#Get the Random Item #5
timebefore = time.time()
randomitem = random.randint(0,len(itemsarray))
itemcheckname = itemsarray[randomitem][0]
print('Item Searching for')
print()
print(itemcheckname)
itemcheckrarity = itemsarray[randomitem][3]
print(itemcheckrarity)
print()
bagcount = 0
for ig in bags:
	itemcount=1
	for il in bags[bagcount]:
		name = False
		rarity = False
		if(il[0] == itemcheckname):
			name = True
		if(il[3] == itemcheckrarity):
			rarity = True
		if(name==True and rarity == True):
			print('---Item Found in Bag:' + str(bagcount) +' Slot:'+ str(itemcount)+' ---')
		itemcount+=1
	bagcount+=1

sizeofhashingtable = 199
#Hashingtablessetup
counter = 0
hashtable1=[]
hashtable2=[]
hashtable3=[]
hashtable4=[]
while(counter != sizeofhashingtable+1):
	hashtable1.append('Empty')
	hashtable2.append('Empty')
	hashtable3.append('Empty')
	hashtable4.append('Empty')
	counter += 1
timeafter = time.time()
totaltime = timeafter - timebefore
print()
print('Time:' + str(totaltime))
	
#HashingMethod1, Closed Method
timebefore = time.time()
bagcount = 0
for ite in bags:
	for intem in bags[bagcount]:
		stre = intem[4]
		hash = stre % sizeofhashingtable
		counter = 0
		if(hashtable1[hash] != 'Empty'):
			while(counter != sizeofhashingtable):
				if(hash < sizeofhashingtable):
					hash+=1
				else:
					hash=0
				if(hashtable1[hash] == 'Empty'):
					hashtable1[hash] = intem
				counter+=1
		else:
			hashtable1[hash] = intem
	bagcount += 1
print()
print('First Probing for table:1')
print()
hash = stre % sizeofhashingtable
itemnotthere = True
for all in range(sizeofhashingtable):
	if(hashtable1[hash][0] == itemcheckname and hashtable1[hash][3] == itemcheckrarity):
		if(itemnotthere == True):
			print('---Found item in Hashtable at slot:'+str(hash)+'---')
		itemnotthere = False
	else:
		if(hash < sizeofhashingtable):
			hash+=1
		else:
			hash=0
if(itemnotthere == True):
	print('---Item not located in Hashtable---')
timeafter = time.time()
totaltime = timeafter - timebefore
print()
print('Time:' + str(totaltime))

#HashingMethod2, Closed Method
timebefore = time.time()
bagcount = 0
for ite in bags:
	for intem in bags[bagcount]:
		stre = intem[4]
		hash = stre % sizeofhashingtable
		counter = 0
		if(hashtable2[hash] != 'Empty'):
			while(counter != sizeofhashingtable):
				if(hash>sizeofhashingtable):
					hash=hash+1
				else:
					hash=0
				if(hashtable2[hash] == 'Empty'):
					hashtable2[hash] = intem
				counter+=1
		else:
			hashtable2[hash] = intem
	bagcount += 1
print()
print('First Probing Method for table:2')
print()
hash = stre % sizeofhashingtable
itemnotthere = True
for all in range(sizeofhashingtable):
	if(hashtable2[hash][0] == itemcheckname and hashtable2[hash][3] == itemcheckrarity):
		if(itemnotthere == True):
			print('---Found item in Hashtable at slot:'+str(hash)+'---')
		itemnotthere = False
	else:
		if(hash < sizeofhashingtable):
			hash+=1
		else:
			hash=0
if(itemnotthere == True):
	print('---Item not located in Hashtable---')
timeafter = time.time()
totaltime = timeafter - timebefore
print()
print('Time:' + str(totaltime))

#HashingMethod3, Open Method
timebefore = time.time()
list = []
bagcount = 0
for ite in bags:
	for intem in bags[bagcount]:
		stre = intem[4]
		hash = stre % sizeofhashingtable
		counter = 0
		if(hashtable3[hash] != 'Empty'):
			#hashtable3[hash].addNode(Node(intem,None))
			list.append(intem)
		else:
			#hashtable3[hash] = ItemLinkedList.addNode(0,Node(intem,None))
			list = []
			list.append(intem)
		hashtable3[hash] = list
	bagcount += 1
print()
print('First Probing Method for table:3')
print()
hash = stre % sizeofhashingtable
itemnotthere = True
for all in range(sizeofhashingtable):
	for all in hashtable3[hash]:
		if(all[0] == itemcheckname and all[3] == itemcheckrarity):
			if(itemnotthere == True):
				print('---Found item in Hashtable at slot:'+str(hash)+'---')
				itemnotthere = False
			else:
				if(hash < sizeofhashingtable):
					hash+=1
				else:
					hash=0
if(itemnotthere == True):
	print('---Item not located in Hashtable---')
timeafter = time.time()
totaltime = timeafter - timebefore
print()
print('Time:' + str(totaltime))

#HashingMethod4, Open Method
timebefore = time.time()
list = []
bagcount = 0
for ite in bags:
	for intem in bags[bagcount]:
		stre = intem[4]
		hash = stre % sizeofhashingtable
		counter = 0
		if(hashtable4[hash] != 'Empty'):
			#hashtable4[hash].addNode(Node(intem,None))
			list.append(intem)
		else:
			#hashtable4[hash] = ItemLinkedList.addNode(0,Node(intem,None))
			list =[]
			list.append(intem)
		hashtable4[hash] = list
	bagcount += 1
print()
print('First Probing Method for table:4')
print()
hash = stre % sizeofhashingtable
itemnotthere = True
for all in range(sizeofhashingtable):
	for all in hashtable4[hash]:
		if(all[0] == itemcheckname and all[3] == itemcheckrarity):
			if(itemnotthere == True):
				print('---Found item in Hashtable at slot:'+str(hash)+'---')
				itemnotthere = False
			else:
				if(hash < sizeofhashingtable):
					hash+=1
				else:
					hash=0
if(itemnotthere == True):
	print('---Item not located in Hashtable---')
timeafter = time.time()
totaltime = timeafter - timebefore
print()
print('Time:' + str(totaltime))

Hashingprobe2(True,hashtable1,sizeofhashingtable,1)

Hashingprobe2(True,hashtable2,sizeofhashingtable,2)

Hashingprobe2(False,hashtable3,sizeofhashingtable,3)

Hashingprobe2(False,hashtable4,sizeofhashingtable,4)

Hashingprobe3(True,hashtable1,sizeofhashingtable,1)

Hashingprobe3(True,hashtable2,sizeofhashingtable,2)

Hashingprobe3(False,hashtable3,sizeofhashingtable,3)

Hashingprobe3(False,hashtable4,sizeofhashingtable,4)

