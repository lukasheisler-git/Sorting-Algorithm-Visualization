from tkinter import *
import numpy as np
from time import sleep



def swap(i,j):
    global rectangles
    x_00, y_00, x_01, y_01 = canvas.coords(rectangles[i])
    x_10, y_10, x_11, y_11 = canvas.coords(rectangles[j])

    canvas.coords(rectangles[i],x_00, y_00, x_01, y_11)
    canvas.coords(rectangles[j],x_10, y_10, x_11, y_01)
    
def quick_sort(left, right):
	global rectangles
	_,_,_,y_11 = canvas.coords(rectangles[left])
	_,_,_,y_21 = canvas.coords(rectangles[right])
	if(y_11 < y_21):
		pivot = partition(left, right)
		quick_sort(left, pivot-1)
		quick_sort(pivot+1, right)

def partition(left,right):
	global rectangles
	i = left
	j = right-1
	_,_,_,pivot = canvas.coords(rectangles[right])
	
	while(i<j):
		_,_,_,y_1i = canvas.coords(rectangles[i])
		while(i < right and y_1i < pivot):
			i=i+1
		_,_,_,y_1j = canvas.coords(rectangles[j])
		while(j > left and y_1j >= pivot):
			j=j+1
		if(i < j):
			swap(i,j)
	_,_,_,y_1i = canvas.coords(rectangles[i])
	if(y_1i > pivot):
		swap(i,right)
	return i

def bubble_sort():
	global rectangles
	for n in range(len(rectangles),1,-1):
		for i in range(0,n-1):
			_,_,_,y11 = canvas.coords(rectangles[i])
			_,_,_,y21 = canvas.coords(rectangles[i+1])
			canvas.itemconfig(rectangles[i], fill='blue')
			canvas.itemconfig(rectangles[i+1], fill='green')
			if(y11 > y21):
				swap(i,i+1)
			canvas.itemconfig(rectangles[i+1], fill='blue')
			canvas.itemconfig(rectangles[i], fill='red')
			sleep(0.0003)	
			root.update()
			
				
def shuffle():
	global rectangles
	for i in rectangles:
		canvas.delete(i)
	rectangles.clear()
	size = 265
	height = 2*np.arange(0,size)
	np.random.shuffle(height)
	
	for i in range(size):
		rectangles.append(canvas.create_rectangle(i*3+1, 0, (i+1)*3+1, height[i], fill='red'))

def set_alg():
	algWindow = Toplevel(root)
	algWindow.title("Choose Algorithm")
	algWindow.geometry("300x100")
	algOption = OptionMenu(algWindow, algVar, *algList)
	algOption.pack()  
	okAlgButton = Button(algWindow,text="Ok",command=switch_func(algVar))
	okAlgButton.pack()
  
#global variables
rectangles = []
  
root = Tk()  
root.title("Sorting Algorithm Visualization")  
root.geometry("800x600")


#create canvas
canvas = Canvas(root,width=800, height=530)
canvas.pack()

# create a toplevel menu  
menubar = Menu(root)  
algmenu = Menu(menubar)
menubar.add_cascade(label="Set Algorithm", menu=algmenu)
algmenu.add_command(label="BubbleSort", command=bubble_sort)
algmenu.add_command(label="QuickSort", command= lambda:quick_sort(0,264))  
menubar.add_command(label="Shuffle",command=shuffle)
menubar.add_command(label="Quit!", command=root.quit)  
  
# display the menu  
root.config(menu=menubar) 
  
root.mainloop()  
