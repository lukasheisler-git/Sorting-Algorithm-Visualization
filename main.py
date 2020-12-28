from tkinter import *
import numpy as np
from time import sleep



def swap(i,j):
    global rectangles
    x_00, y_00, x_01, y_01 = canvas.coords(rectangles[i])
    x_10, y_10, x_11, y_11 = canvas.coords(rectangles[j])

    canvas.coords(rectangles[i],x_00, y_00, x_01, y_11)
    canvas.coords(rectangles[j],x_10, y_10, x_11, y_01)

def get_Gap(gap):
	gap = (gap * 10) / 13
	if gap < 1: 
		return 1
	return gap
    
def comb_sort():
	global rectangles
	n = len(rectangles)
	
	#Initialize gap
	gap = n 
	swapped = True
	while(gap != 1 or swapped == 1):
		gap = int(get_Gap(gap))
		swapped = False
		
		for i in range (0, n - gap):
			_,_,_,y_1i = canvas.coords(rectangles[i])
			_,_,_,y_1gap = canvas.coords(rectangles[i + gap])
			canvas.itemconfig(rectangles[i], fill='blue')
			canvas.itemconfig(rectangles[i+gap], fill='green')
			if(y_1i > y_1gap):
				swap(i,i + gap)
				root.update()
				sleep(0.005)
				swapped=True
			canvas.itemconfig(rectangles[i+gap], fill='blue')
			canvas.itemconfig(rectangles[i], fill='red')
 
    
def quick_sort(left, right):
	global rectangles
	if(left < right):
		pivot = partition(left, right)
		quick_sort(left, pivot-1)
		quick_sort(pivot+1, right)

def partition(left,right):
	global rectangles
	i = left-1
	_,_,_,pivot = canvas.coords(rectangles[right])
	canvas.itemconfig(rectangles[right], fill='green')
	for j in range(left,right):
		_,_,_,y_1j = canvas.coords(rectangles[j])
		if(y_1j < pivot):
			i = i+1
			swap(i,j)
			root.update()
			sleep(0.005)
	swap(i+1,right)
	canvas.itemconfig(rectangles[i+1], fill='blue')
	root.update()
	sleep(0.005)
	return (i+1)
	

def bubble_sort():
	global rectangles, comparisons,swaps
	for n in range(len(rectangles),1,-1):
		for i in range(0,n-1):
			_,_,_,y11 = canvas.coords(rectangles[i])
			_,_,_,y21 = canvas.coords(rectangles[i+1])
			canvas.itemconfig(rectangles[i], fill='blue')
			canvas.itemconfig(rectangles[i+1], fill='green')
			#upadte comparisons
			comparisons = comparisons + 1
			compVar.set('Number of comparisons: {}'.format(comparisons))
			if(y11 > y21):
				swaps = swaps + 1
				swapVar.set('Number of swaps: {}'.format(swaps))
				swap(i,i+1)
			canvas.itemconfig(rectangles[i+1], fill='blue')
			canvas.itemconfig(rectangles[i], fill='red')
			sleep(0.0003)	
			root.update()
			#root.update_idletasks()
			
				
def shuffle():
	global rectangles, comparisons, swaps
	comparisons = 0
	swaps = 0
	compVar.set('Number of comparisons: {}'.format(comparisons))
	swaps = 0
	swapVar.set('Number of swaps: {}'.format(swaps))
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
  

  
root = Tk()  
root.title("Sorting Algorithm Visualization")  
root.geometry("800x600")

#global variables
rectangles = []
comparisons = 0
swaps = 0
compVar = StringVar()
compVar.set('Number of comparisons: {}'.format(comparisons))
swapVar = StringVar()
swapVar.set('Number of swaps: {}'.format(swaps))

#create canvas
canvas = Canvas(root,width=800, height=530)
canvas.pack()

#Create widgets to show # of comparisons, # of swaps, # of items
compLabel = Label(root, textvariable = compVar)
compLabel.pack(anchor = "s", side = "bottom")
swapLabel = Label(root, textvariable = swapVar)
swapLabel.pack(anchor = "s", side = "bottom")
itemLabel = Label(root, text = 'Number of items: 265')
itemLabel.pack(anchor = "s", side = "bottom")

# create a toplevel menu  
menubar = Menu(root)  
algmenu = Menu(menubar)
menubar.add_cascade(label="Set Algorithm", menu=algmenu)
algmenu.add_command(label="BubbleSort", command=bubble_sort)
algmenu.add_command(label="QuickSort", command= lambda:quick_sort(0,264))  
algmenu.add_command(label="CombSort", command=comb_sort)
menubar.add_command(label="Shuffle",command=shuffle)
menubar.add_command(label="Quit!", command=root.quit)  
  
# display the menu  
root.config(menu=menubar) 
  
root.mainloop()  
