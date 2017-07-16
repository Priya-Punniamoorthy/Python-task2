import csv
fields=['S.no','Name','Price','No of items']
class billing:


	def display(self):
		n=0
		with open("list1.csv",'r') as ope:
				r = csv.DictReader(ope)
				for row in r:
					print (row)
					n+=1


	def add(self):
		name=input('Enter the item to be added:')
		cost=input('Enter the cost of the item:')
		stack=input('Enter the no of pieces in the stack:')
		n=0
		with open("list1.csv",'r') as ope:
				r = csv.DictReader(ope)
				for row in r:
					n+=1

		add=[{'S.no':int(n)+1,'Name':str(name),'Price':int(cost),'No of items':int(stack)}]
		with open("list1.csv",'a') as ope:
			a=csv.DictWriter(ope,fieldnames=fields)
			a.writerow(add[0])

		with open("list1.csv",'r') as ope:
				r = csv.DictReader(ope)
				for row in r:
					print (row)


	def update(self):
		li=[]
		i=0
		flag=0
		nm=input('Enter the item to be update:')
		with open("list1.csv",'r') as ope:
			u=csv.DictReader(ope)
			for row in u:	
				i+=1	
				if(row['Name']==nm):
					flag+=1
					n=input('Enter 1 to update price\n Enter 2 to update the number of items:')	
					if int(n)==1:
						pr=input('Enter the price to update:')
						row['Price']=pr
						li.append(row)
					elif int(n)==2:
						st=input('Enter the no of items to update:')	
						row['No of items']=st
						li.append(row)	
					else:
						li.append(row)		
				else:
					li.append(row)
			if(flag==0):
				print("\nThe item is not found in the store\n")
		with open ("list1.csv",'w') as ope:
			w=csv.DictWriter(ope,fieldnames=fields)
			w.writeheader()
			w.writerows(li)
		with open("list1.csv",'r') as ope:
				r = csv.DictReader(ope)
				for row in r:
					print (row)

	def search(self):
		ser=0
		nm1=input('Enter the item to be search:')
		with open("list1.csv",'r') as ope:
			s=csv.DictReader(ope)
			for row in s:		
				if(row['Name']==nm1):
						print (row)
						ser=1
			if(ser==0):
				print("\nThe item is not found in the stack")
	def delete(self):		
		dli=[]
		i=0
		nm2=input('Enter the item to delete:')
		with open("list1.csv",'r') as ope:
			d=csv.DictReader(ope)
			for row in d:	
				if(row['Name']==nm2):
					i+=1
				else:	
					if(i==0):
						dli.append(row)
					else:
						row['S.no']=int(row['S.no'])-1
						dli.append(row)
			if(i==0):
				print("\nThe item is not found in the store")
		with open ("list1.csv",'w') as ope:
			w=csv.DictWriter(ope,fieldnames=fields)
			w.writeheader()
			w.writerows(dli)
		with open("list1.csv",'r') as ope:
				r = csv.DictReader(ope)
				for row in r:
					print (row)

	def bill(self):
		total=0
		num=input('Enter the number of items to bill:')
		for e in range(0,int(num)):
			with open("list1.csv",'r') as ope:
				b=csv.DictReader(ope)
				item=input('Enter the item:')
				bill=0
				for row in b:		
					if(row['Name']==item):
						mon=input('Enter the number of pieces:')
						row['No of items']=int(row['No of items'])-int(mon)
						p1=int(mon)*int(row['Price'])
						total=total+p1
						bill=1
				if(bill==0):
					print("\nThe item is not found in the store")
		print('\nTotal bill='+str(total))
b=billing()	
while(1):
	print("\n1.Enter 1 to list all the items\n2.Enter 2 to add any item\n3.Enter 3 to delete any item\n4.Enter 4 to update an item\n5.Enter 5 to search about an item\n6.Enter 6 to billing\n7.Enter any number to exit\n")
	choice=input('Enter your choice:')
	if int(choice)==1:
		b.display()
	elif int(choice)==2:
		b.add()
	elif int(choice)==3:
		b.delete()
	elif int(choice)==4:
		b.update()
	elif int(choice)==5:
		b.search()
	elif int(choice)==6:
		b.bill()
	else:
		exit()






