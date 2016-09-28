import tkinter
import re
from string import *
from tkinter import *

class Application(Frame):
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		
		self.QUIT.pack({"side": "left"})
		
		self.submit_button = Button(self)
		self.submit_button["text"] = "submit"
		self.submit_button["command"] = self.submit
		
		self.submit_button.pack({"side": "left"})
		
		self.lab_seq = Label(self,text="Sequence:")
		self.lab_seq.pack({"side":"left"})
		
		self.sequence = Entry(self)
		self.sequence.pack({"side": "left"})
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	
	def clean_sequence(self, sequence):
			"Cleans non-sequence characters from the sequence"
			#delete_table = maketrans(
			#			"ACGTacgt", " " * len("ACGTacgt")
			#)
			#table = maketrans( "", '')
			#clean = sequence.translate(str.maketrans(table,delete_table))
			#print clean
			clean = re.sub('[^atgc]','',sequence.lower())
			return clean.upper()

	def digest_flank(self, sequence, enzyme1, enzyme2):
			"Simulates a restriction digest with the specified enzymes"
			try:
					step1 = enzyme1 + sequence.split(enzyme1)[1]
					step2 = step1.split(enzyme2)[0] + enzyme2
					return step2
			except IndexError:
					print("One or more of the enzymes could not be found in the flank")
			#print step2

			return

	def digest_vector(self, sequence, enzyme1, enzyme2, enzyme3, enzyme4, flank1, flank2):
			"Simulates a restriction digest with the specified enzymes"
			try:
					step1 = sequence.split(enzyme1)[0]
					step2 = sequence.split(enzyme2)[1]
					#print step2
					half_vector = step1 + flank1 + step2
					step3 = half_vector.split(enzyme3)[0]
					step4 = half_vector.split(enzyme4)[1]
					final_vector = step3 + flank2 + step4
					print(final_vector)
			except IndexError:
					print("One or more of the enzymes could not be found in the vector")

			return
	def submit(self):
		test = self.sequence.get()
		print(self.clean_sequence(test))
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
