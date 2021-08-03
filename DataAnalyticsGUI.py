import DataAnalysis as da
import tkinter as tk
import webbrowser
import os
reports=False

#Action function for the upload dataset button, the same retrieve the filename and route in the computer
def UploadAction(event=None):
    filename = tk.filedialog.askopenfilename()
    print(filename)
    #This conditional verified that the user entered a file and then generate the report and open it a browser window with webbrowser
    if filename !='':
        global reports
        reports=bool(True)
        da.fn=filename
        da.report()
        webbrowser.open_new_tab('Report.html')

#Action function for the open correlation matrix button, the same opens the already generated corr matrix in the browser with webbrowser
def OpenCorrMatrix(event=None):
    if reports:
        webbrowser.open_new_tab('CorrelationMatrix.html')
    else:
        #this also triggers a warning box in the case the user didnt entered any dataset
        tk.messagebox.showwarning("Warning", "Please first upload a CSV Dataset to generate the Correlation Matrix" ) 

#Action function for the dotGraph button, the same opens a new tkinter window so the user can select the variables to generate the graph
def dotGraph():
    #Action function for the generate dot graphic button the same generates the dot graph in and open it in the browser
    def generate():
        da.dotGraphic(variablex.get(),variabley.get())
        webbrowser.open_new_tab(f'dotGraphic[{variablex.get()}]vs[{variabley.get()}].html')
    if reports:
        #If the suer already uploaded a dataset, this creates the new window and ask the user for the variables for the graph
        dotg = tk.Tk()
        dotg.iconbitmap("favicon.ico")
        dotg.title('Data Analytics for Everyone')
        frame2 = tk.Frame(master=dotg, width=int(100), height=100, bg="#1f2124")
        title=tk.Label(frame2,text="Select the x and y variable to generate the doth graph",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
        variablex = tk.StringVar(frame2)
        variablex.set("Select x variable") # default value
        variabley = tk.StringVar(frame2)
        variabley.set("Select y variable") # default value
        varx = tk.OptionMenu(frame2, variablex, *da.varL['x']).pack()
        vary = tk.OptionMenu(frame2, variabley, *da.varL['y']).pack()
        for varx in da.varL['x']:
            print(f'xvar:{varx},')
        for vary in da.varL['y']:
            print(f'yvar:{vary},')
        buttonok = tk.Button(frame2, text=str("Generate new Dot Graph"), command=generate).pack(anchor='e')
        frame2.pack(fill=tk.X)
        dotg.mainloop()
    #this also triggers a warning box in the case the user didnt entered any dataset
    else:
        tk.messagebox.showwarning("Warning", "Please first upload a CSV Dataset to generate the Correlation Matrix" )
#Action function for the openPath button, the same opens a the file explorer on teh folder where the reports are stored  
def openPath():
    path = os.getcwd()
    path = os.path.realpath(path)
    os.startfile(path)


#Creation of the main window, were we include the instructions for the user and the buttons to interact
mtk = tk.Tk()
mtk.iconbitmap("favicon.ico")
mtk.title('Data Analytics for Everyone')

frame = tk.Frame(master=mtk, width=100, height=100, bg="#1f2124")

title=tk.Label(frame,text="Welcome to Data Analytics for Everyone!",fg="white",bg="#18191c", font=("Verdana",24),width=50, height=2).pack()
#First step the user uploads the CSV dataset, this triggers the UploadAction fuction to generate and open the report
title=tk.Label(frame,text="1. First download/create a CSV dataset of your data and click in the following button to create a data report",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
upload = tk.Button(frame, text='Open CSV DataSet',width=25, command=UploadAction).pack()

title=tk.Label(frame,text="2. With the Data report that is going to open in your browser you can edit and adjust your Dataset to fit the report requirements.",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')

title=tk.Label(frame,text="3. Once your data set fit all the requirements you can review important information from the report such as Minimum, Maximun, Distinct... ",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
#Fourth step the user can open in a browser the correlation matrix this triggers the function OpenCorrMatrix
title=tk.Label(frame,text="4. After you have the report generated you can generate a Correlation matrix clicking in the following button.",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
upload = tk.Button(frame, text='Generate Correlation Matrix',width=25, command=OpenCorrMatrix).pack()

title=tk.Label(frame,text="5. With the Correlation Matrix you can review the Correlation of your variables and generate dot graphic with the following step.",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
# Step number six this one triggers dotGraph to open a new window and ask for the dot grapgh variables, and the onpen it in the browser
title=tk.Label(frame,text="6. In this step generate dot graphs of the variables, first the select required variables and click on generate to open the graph ",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
ok = tk.Button(frame, text='Generate Dot Graph',width=25,height=2, command=dotGraph).pack()

title=tk.Label(frame,text="7. Now wit this data you can improve your business, find new possible markets, recognize issues in your business model...",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
#Step number eight With this one the user can open the folder in the file explorer where can find the html reports to save an open after
title=tk.Label(frame,text="8. You can retrieve the .html file and open them in your browser in the same folder of the program, you can open it with this button",fg="white",bg="#1f2124", font=("Verdana",12), height=2).pack(anchor='w')
cpath = tk.Button(frame, text='Open report and graph folder',width=25, command=openPath).pack()

#Thanks for using! message with th eframe pack and tkinter mainloop that keep open the window
title=tk.Label(frame,text="Thanks for using!",fg="white",bg="#18191c", font=("Verdana",24),width=30, height=2).pack()
frame.pack(fill=tk.X)
mtk.mainloop()