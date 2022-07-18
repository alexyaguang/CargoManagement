import pymongo
import tkinter as tk
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())
mydb = client["mydatabase"]
mycol = mydb["warehouse"]
master = tk.Tk()
master.geometry("1000x400")




def clear_frame():
   for widgets in master.winfo_children():
      widgets.destroy()

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def clearAndShow():
	clear_frame()
	tk.Label(master, text="Everything Cleared").grid(row=0)
	count=0
	for x in mycol.find():
		tk.Label(master, text=x).grid(row=count)
		count+=1
	backButton()
def inboundWindow():
	def inBoundButton():#need function for this button
		tk.Button(master, 
	          text='inBound', command=intoWarehouse).grid(row=5, 
	                                                       column=1, 
	                                                       sticky=tk.W, 
	                                                       pady=4)
	def intoWarehouse():
		temp=[e0.get(),e1.get(),e2.get(),e3.get(),e4.get()]
		count = 0
		for i in temp:
			if i == "":
				count=1
		if count ==0:
			e0.delete(0, 'end')
			e1.delete(0, 'end')
			e2.delete(0, 'end')
			e3.delete(0, 'end')
			e4.delete(0, 'end')
			mydict = { "Created Date": temp[0], "Container ID": temp[1],"SKU ID":temp[2],"Counts":temp[3],"Location":temp[4] }
			mycol.insert_one(mydict)
			tk.Label(master, bg="yellow",text = 'insert successed').grid(row=6)
			for x in mycol.find():
	  			print(x)
		else:
			tk.Label(master, bg="red",text = 'invalid info').grid(row=6)
	clear_frame()
	tk.Label(master, text="Pallet ID(Created Date)").grid(row=0)
	tk.Label(master, text="Container ID").grid(row=1)
	tk.Label(master, text="SKU ID(s)").grid(row=2)
	tk.Label(master, text="Count(s)").grid(row=3)
	tk.Label(master,text = "Location").grid(row=4)
	e0 = tk.Entry(master)
	e1 = tk.Entry(master)
	e2 = tk.Entry(master)
	e3 = tk.Entry(master)
	e4 = tk.Entry(master)
	e0.grid(row=0, column=1)
	e1.grid(row=1, column=1)
	e2.grid(row=2, column=1)
	e3.grid(row=3, column=1)
	e4.grid(row=4, column=1)
	inBoundButton()
	backButton()
def outboundWindow():
	def delCargo():
		temp = e5.get()
		mycol.delete_one({'Created Date':temp})
		print("deleted")
	def searchWarehouse():
		temp=[e0.get(),e1.get(),e2.get(),e3.get(),e4.get()]
		res=[]
		for i in temp:
			if i!="":
				res.append(1)
			else:
				res.append(0)
		targets=[]
		matchs={ 0:"Created Date",1: "Container ID",2:"SKU ID",3:"Counts",4:"Location"}
		for x in mycol.find():
			count=0
			for i in range(len(res)):
				if res[i]==1:
					if temp[i] == x[matchs[i]]:
						count+=1
						continue
					else:
						break
				else:
					continue
			if count == sum(res):
				targets.append(x)
		c=0
		for i in targets:
			c+=1
			tk.Label(master, text=i).grid(row=7+c)
			print(i)
	clear_frame()
	tk.Label(master, text="Keyword Search").grid(row=0)
	tk.Label(master, text="Created Date").grid(row=1)
	tk.Label(master, text="Container ID").grid(row=2)
	tk.Label(master, text="SKU ID(s)").grid(row=3)
	tk.Label(master, text="Count(s)").grid(row=4)
	tk.Label(master,text = "Location").grid(row=5)
	tk.Label(master,text = "Target").grid(row=7)
	e0 = tk.Entry(master)
	e1 = tk.Entry(master)
	e2 = tk.Entry(master)
	e3 = tk.Entry(master)
	e4 = tk.Entry(master)
	e5 = tk.Entry(master)
	e0.grid(row=1, column=1)
	e1.grid(row=2, column=1)
	e2.grid(row=3, column=1)
	e3.grid(row=4, column=1)
	e4.grid(row=5, column=1)
	e5.grid(row=7, column=1)
	tk.Button(master, 
          text='Delete', command=delCargo).grid(row=7, 
                                                       column=3, 
                                                       sticky=tk.W, 
                                                       pady=4)
	tk.Button(master, 
	          text='Find', command=searchWarehouse).grid(row=6, 
	                                                       column=0, 
	                                                       sticky=tk.W, 
	                                                       pady=4)

	backButton()
def backToMain():
	clear_frame()
	tk.Button(master, 
	          text='Show', command=clearAndShow).grid(row=0, 
	                                                       column=0, 
	                                                       sticky=tk.W, 
	                                                       pady=4)
	tk.Button(master, 
	          text='InBound', command=inboundWindow).grid(row=2, 
	                                                       column=0, 
	                                                       sticky=tk.W, 
	                                                       pady=4)
	tk.Button(master, 
	          text='OutBound', command=outboundWindow).grid(row=3, 
	                                                       column=0, 
	                                                       sticky=tk.W, 
	                                                       pady=4)

	backButton()
	tk.Button(master, 
	          text='Quit', 
	          command=master.quit).grid(row=6, 
	                                    column=0, 
	                                    sticky=tk.W, 
	                                    pady=4)

def findButton():
	tk.Button(master, 
	          text='Find', command=backToMain).grid(row=5, 
	                                                       column=0, 
	                                                       sticky=tk.W, 
	                                                       pady=4)

def backButton():
	tk.Button(master, 
	          text='Back', command=backToMain).grid(row=0, 
	                                                       column=7, 
	                                                       sticky=tk.W, 
	                                                       pady=4)

backToMain()


"""


tk.Label(master, text="Created Date").grid(row=0)
tk.Label(master, text="Container ID").grid(row=1)
tk.Label(master, text="SKU ID(s)").grid(row=2)
tk.Label(master, text="Count(s)").grid(row=3)
tk.Label(master,text = "Loction").grid(row=4)



e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)"""
master.mainloop()