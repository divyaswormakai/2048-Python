from array import *
from matplotlib import colors
import random,tkinter

a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[2,0,0,0]]
top = tkinter.Tk()

def printData():
	for i in range(0,4):
		text = str(a[i][0])+","+str(a[i][1])+","+str(a[i][2])+","+str(a[i][3])
		print(text+"\n")
	print("\n")

def goLeft(event):
	#for the find and add part
	for row in range(0,4):
		col = 0
		while col<=3:
			if(a[row][col]==0):
				col+=1
				continue
			else:
				col2=col+1
				while(col2<=3):
					if(a[row][col2]==0):
						col2+=1
						continue
					else:
						if(a[row][col]==a[row][col2]):
							a[row][col] = 2*a[row][col2]
							a[row][col2] = 0
							break
						else:
							break
				col+=1
	#for the plaecment part
	for row in range(0,4):
		col=0
		changeFlag=0
		while col<=3:
			if(a[row][col]==0):
				col+=1
				continue
			else:
				col2 = col-1
				while col2>=0:
					if(a[row][col2]==0):
						minCol = col2
						changeFlag=1
					col2-=1
				if(changeFlag == 1):
					a[row][minCol] = a[row][col]
					a[row][col] = 0
					changeFlag=0
				col+=1
				continue
	insertNew()
	updateData()


def goRight(event):
	#for the find and add part
	for row in range(0,4):
		col = 3
		while col>=0:
			if(a[row][col]==0):
				col-=1
				continue
			else:
				col2=col-1
				while(col2>=0):
					if(a[row][col2]==0):
						col2-=1
						continue
					else:
						if(a[row][col]==a[row][col2]):
							a[row][col] = 2*a[row][col2]
							a[row][col2] = 0
							break
						else:
							break
				col-=1
	#for the plaecment part
	for row in range(0,4):
		col=3
		changeFlag=0
		while col>=0:
			if(a[row][col]==0):
				col-=1
				continue
			else:
				col2 = col+1
				while col2<=3:
					if(a[row][col2]==0):
						minCol = col2
						changeFlag=1
					col2+=1
				if(changeFlag == 1):
					a[row][minCol] = a[row][col]
					a[row][col] = 0
					changeFlag=0
				col-=1
				continue
	insertNew()
	updateData()

def goUp(event):
	#for the find and add part
	for col in range(0,4):
		row = 0
		while row<=3:
			if(a[row][col]==0):
				row+=1
				continue
			else:
				row2=row+1
				while(row2<=3):
					if(a[row2][col]==0):
						row2+=1
						continue
					else:
						if(a[row][col]==a[row2][col]):
							a[row][col] = 2*a[row2][col]
							a[row2][col] = 0
							break
						else:
							break
				row+=1
	#for the plaecment part
	for col in range(0,4):
		row=0
		changeFlag=0
		while row<=3:
			if(a[row][col]==0):
				row+=1
				continue
			else:
				row2 = row-1
				while row2>=0:
					if(a[row2][col]==0):
						minRow = row2
						changeFlag=1
					row2-=1
				if(changeFlag == 1):
					a[minRow][col] = a[row][col]
					a[row][col] = 0
					changeFlag=0
				row+=1
				continue
	insertNew()
	updateData()

def goDown(event):
	for col in range(0,4):
		row = 3
		while row>=0:
			if(a[row][col]==0):
				row-=1
				continue
			else:
				row2=row-1
				while(row2>=0):
					if(a[row2][col]==0):
						row2-=1
						continue
					else:
						if(a[row][col]==a[row2][col]):
							a[row][col] = 2*a[row2][col]
							a[row2][col] = 0
							break
						else:
							break
				row-=1
	#for the plaecment part
	for col in range(0,4):
		row=3
		changeFlag=0
		while row>=0:
			if(a[row][col]==0):
				row-=1
				continue
			else:
				row2 = row+1
				while row2<=3:
					if(a[row2][col]==0):
						minRow = row2
						changeFlag=1
					row2+=1
				if(changeFlag == 1):
					a[minRow][col] = a[row][col]
					a[row][col] = 0
					changeFlag=0
				row-=1
				continue
	insertNew()
	updateData()

def insertNew():
	flag = True
	counter =0
	while(flag==True):
		one = random.randint(0,3)
		two = random.randint(0,3)

		if(a[one][two] == 0):
			a[one][two]=2
			flag=False
		counter+=1
		if(counter == 16):
			flag= False
			print("game over")
	updateData()

def updateData():
	for i in range(0,4):
		for j in range(0,4):
			labelstr="label"+str(i)+str(j)
			xpos=55*i+80
			ypos=55*j+80
			label = tkinter.Label(top,text=str(a[j][i]),relief="groove")
			label.place(x=xpos,y=ypos,width=50,height=50)
			if(a[j][i]==2):
				label.config(bg="gray")
			elif(a[j][i]==4):
				label.config(bg="yellow")


if __name__ =="__main__":
	top.geometry('400x400')

	frame = tkinter.Frame(top,width=100,height=100)
	frame.bind("<KeyPress-a>",goLeft)
	frame.bind("<KeyPress-d>",goRight)
	frame.bind("<KeyPress-w>",goUp)
	frame.bind("<KeyPress-s>",goDown)
	frame.pack()
	frame.focus_set()

	instruction = tkinter.Label(top,text="W for UP,D for Down,A for Left and D for R for Right")
	instruction.place(x=50,y=0,height=100,width=300)

	insertNew()
	updateData()
	top.mainloop()