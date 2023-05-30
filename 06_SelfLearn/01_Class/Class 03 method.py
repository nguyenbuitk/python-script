# dùng classmethod , staticmethod, regularmethod

# classmethod
class sieunhan:
	def __init__(self,para_ten,para_vukhi,para_mausac):
		self.ten=" sieu nhan "+para_ten
		self.vukhi=para_vukhi
		self.para_mausac=para_mausac
	@classmethod
	def from_string(cls,s):
		lst=s.split('-')
		new_lst=[st.strip() for st in lst]
		ten,vu_khi,mau_sac=new_lst
		return cls(ten,vu_khi,mau_sac)

infor_str="do-kiem-do"
sieunhana=sieunhan.from_string(infor_str)
print(sieunhana.__dict__)

# staticmethod

class sieunhan:
	def __init__(self,para_ten,para_vukhi,para_mausac):
		self.ten=" sieu nhan "+para_ten
		self.vukhi=para_vukhi
		self.para_mausac=para_mausac

	@staticmethod

	# nếu không dùng static method thì phải có def bien_hinh(self):

	def bien_hinh():
		dsadsf

#regularmethod 
	
	def bien_hinh(self):