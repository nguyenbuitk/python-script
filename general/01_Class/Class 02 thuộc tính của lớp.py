class sieunhan:
	sothutu=1
	suc_manh=50
	def __init__(self,para_ten,para_vukhi,para_mausac):
		self.ten=" sieu nhan "+para_ten
		self.vukhi=para_vukhi
		self.para_mausac=para_mausac
		self.stt=sieunhan.sothutu
		sieunhan.sothutu+=1
		#thay đổi số thứ tự khi tạo class khác
	def xinchao(self):
		return "xin chao,ta chinh la"  +self.ten
	@classmethod
	def capnhatsucmanh(cls,smanh)
		# cls thay thế class siêu nhâno
		cls.suc_manh=smanh

sieunhana=sieunhan("kteam","dsafa","sdfa")

print(sieunhana.xinchao())