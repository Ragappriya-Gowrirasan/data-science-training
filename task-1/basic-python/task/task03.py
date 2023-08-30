from tkinter import*
#import webbrowser
#browser1 = webbrowser.get()
#browser1 = webbrowser.open('enter url')
window =Tk() # browser open screen

# browser title
window.title('my_browser')

#size
window.geometry('500x500')

#colour 
window.config(background='light blue')

# display show the text
lab = Label(window, text='enter url')
lab.pack()

#link enter box
url = Entry(window)
url.pack()

#button 
button1 = Button(window,text='open url')
button1.pack()
window.mainloop()