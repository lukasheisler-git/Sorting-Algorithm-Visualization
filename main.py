from tkinter import *
import numpy as np

def bubble_sort():
	global rectangles
	print("Test")
	canvas.itemconfig(rectangles[10], fill='blue')
	canvas.itemconfig(rectangles[11], fill='blue')
	canvas.itemconfig(rectangles[12], fill='blue')
	for n in range(len(rectangles),1,-1):
		for i in range(0,n-1):
			x10,y10,x11,y11 = canvas.coords(rectangles[i])
			x20,y20,x21,y21 = canvas.coords(rectangles[i+1])
			if(y11 > y21):
				canvas.coords(rectangles[i],x20,y20,x21,y21)
				canvas.coords(rectangles[i+1],x10,y10,x11,y11)
def update_rectangles():
	pass
		
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
	okAlgButton = Button(algWindow,text="Ok",command=bubble_sort)
	okAlgButton.pack()
  
#global variables
rectangles = []
  
root = Tk()  
root.title("Sorting Algorithm Visualization")  
root.geometry("800x600")
  
  
#define possible algorithms
algList = ["BubbleSort", "QuickSort", "MergeSort"]
algVar = StringVar(root)
algVar.set(algList[0])
sizeVar = IntVar(root)
sizeVar.set(100)



  
# create a toplevel menu  
menubar = Menu(root)  
menubar.add_command(label="Set Algorithm", command=set_alg)  
menubar.add_command(label="Shuffle",command=shuffle)
menubar.add_command(label="Quit!", command=root.quit)  
  
# display the menu  
root.config(menu=menubar) 

#create canvas
canvas = Canvas(root,width=800, height=530)
canvas.pack()
update_rectangles()
  
root.mainloop()  
