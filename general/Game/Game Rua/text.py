class nhaptien:
	def __init__(self,master):
		self.master=master
		Label(master, text="Deposit money").grid(row=0)
		Label(master, text="Bet money").grid(row=1)
		self.e1= Entry(master)
		self.e2 = Entry(master)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
		Button(master, text='Show Bet Money', command=self.show).grid(row=3, column=1, sticky=W, pady=4)
		Button(master, text='Play', command=self.command3_1).grid(row=3, column=2, sticky=W, pady=4)
	def show(self):
		self.tiencuoc=self.e1.get()
		print(self.tiencuoc)
	def command3_1(self):
		self.master.withdraw()
		playgame1()