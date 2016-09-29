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
		
		self.QUIT.grid(row=3,column=1)
		
		self.submit_button = Button(self)
		self.submit_button["text"] = "submit"
		self.submit_button["command"] = self.submit_method
		
		self.submit_button.grid(row=3, column=0)
		
		self.clone_type = Listbox(self)
		self.clone_type.grid(row=0,column=0)
		
		for item in ["Gateway","RNAi","TOPO"]:
			self.clone_type.insert(END, item)
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
	def forget_me(self, stuff):
		for item in stuff:
			item.grid_forget()
	
	
	def clean_sequence(self, sequence):
			"Cleans non-sequence characters from the sequence"
			#old method of cleaning input characters
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
	def RNAi(self):
		"Creates a vector for RNA interference of a targeted gene"
		
		
		
		
		
		
	def clone_logic(self, type):
			"Changes the cloning method"
			if type == "RNAi":
				print("You have selected RNAi")
				#self.lab_seq.grid_forget()
				#self.vector_sequence.grid_forget()
				#self.button_method.grid_forget()
				forget = [self.lab_seq,self.vector_sequence,self.button_method]
				self.forget_me(forget)
				
				
				self.button_method = Button(self)
				self.button_method["text"] = "submit"
				self.button_method["command"] = self.RNAi
				self.button_method.grid(row=3, column=0)
				
			elif type == "Gateway":
				print("You have selected Gateway Cloning")
				self.Gateway()
			elif type == "TOPO":
				print("You have selected TOPO Cloning")
				self.TOPO()
				
				
	def submit_vector(self):
		test = self.vector_sequence.get("1.0",END)
		print(self.clean_sequence(test))
		type = self.clone_type.get(self.clone_type.curselection())
		self.clone_logic(type)
		
		
	def submit_method(self):
		method = self.clone_type.get(self.clone_type.curselection())
		print(method)
		
		#self.clone_type.grid_forget()
		#self.submit_button.grid_forget()
		forget = [self.clone_type,self.submit_button]
		self.forget_me(forget)
		
		self.lab_seq = Label(self,text="Vector Sequence:")
		self.lab_seq.grid(row=1, column=0)
		
		self.vector_sequence = Text(self)
		self.vector_sequence.grid(row=2,column=0)
		
		self.button_method = Button(self)
		self.button_method["text"] = "submit"
		self.button_method["command"] = self.submit_vector
		self.button_method.grid(row=3, column=0)
		
		
		
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
