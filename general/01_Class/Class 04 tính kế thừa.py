class sieunhan:
	sucmanh=50
	def __init__(self,paraten,paravukhi): 
		self.ten=paraten
		self.vukhi=paravukhi

class sieunhangao(sieunhan):
	sucmanh=40
	#kế thừa thuộc tính
	def __init__(self,paraten,paravukhi,paramau):
		super().__init__(paraten,paravukhi)
		self.mau=paramau
		print("suc manh cua ta la: ",self.vukhi)

sieunhando=sieunhangao("nguyen","kiem","500") #constructor
print(sieunhando.__dict__)
print(sieunhando.ten)