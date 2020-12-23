from tkinter import *




def set_alg():
	algWindow = Toplevel(root)
	algWindow.title("Choose Algorithm")
	algWindow.geometry("300x100")
	algOption = OptionMenu(algWindow, algVar, *algList)
	algOption.pack()  
	okAlgButton = Button(algWindow,text="Ok",command=algWindow.destroy)
	okAlgButton.pack()
  
	

def set_size():
	sizeWindow = Toplevel(root)
	sizeWindow.title("Choose Size")
	sizeWindow.geometry("300x100")
	okSizeButton = Button(sizeWindow,text="Ok",command=sizeWindow.destroy)
	okSizeButton.pack()


  
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
menubar.add_command(label="Set Size", command=set_size)  
menubar.add_command(label="Quit!", command=root.quit)  
  
# display the menu  
root.config(menu=menubar)  
  
root.mainloop()  
