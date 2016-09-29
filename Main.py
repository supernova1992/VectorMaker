import tkinter
import re
from string import *
from tkinter import *
import os

class Application(Frame):
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		
		self.QUIT.grid(row=4,column=1)
		
		self.submit_button = Button(self)
		self.submit_button["text"] = "submit"
		self.submit_button["command"] = self.submit_method
		
		self.submit_button.grid(row=4, column=0)
		
		self.instruct = Label(self,text="Select your experiment:")
		self.instruct.grid(row=2,column=0)
		self.clone_type = Listbox(self)
		self.clone_type.grid(row=3,column=0)
		
		self.l_name = Label(self,text="Final Vector Name:")
		self.l_name.grid(row=0,column=0)
		self.final_name = Entry(self)
		self.final_name.grid(row=1,column=0)
		
		for item in ["Gateway","RNAi","TOPO"]:
			self.clone_type.insert(END, item)
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		print(os.getcwd())
	
	def writeOut(self, final):
		#write out the final vector to fasta file
		f = open(self.final_name.get()+".fas",'w')
		f.write(">"+self.final_name.get()+" | Made with VectorMaker \n"+final)
		f.close()
		
	def restart(self):
		root.destroy()
		root= tk()
		app = Application(master=root)
		app.mainloop()
		root.destroy()
		
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
			except ValueError:
					print("No enzymes were entered")
			
			
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
			except ValueError:
					print("No enzymes were entered")
			return final_vector
	def process(self):
			vector = self.vector_sequence.get("1.0",END)
			flank1 = self.t_5f.get("1.0",END)
			flank2 = self.t_3f.get("1.0",END)
			e1 = self.t_e1.get().upper()
			e2 = self.t_e2.get().upper()
			e3 = self.t_e3.get().upper()
			e4 = self.t_e4.get().upper()
			v_clean = self.clean_sequence(vector)
			clean_5 = self.clean_sequence(flank1)
			clean_3 = self.clean_sequence(flank2)
			
			d_5 = self.digest_flank(clean_5, e1, e2)
			d_3 = self.digest_flank(clean_3, e3, e4)
			final = self.digest_vector(v_clean, e1,e2,e3,e4, d_5,d_3)
			#print(final)
			self.writeOut(final)
			forget= self.winfo_children()
			self.forget_me(forget)
			
			path = os.getcwd()
			
			self.final_text = Label(self, text="Your file has been written to "+path)
			self.final_text.grid()
			
			#self.confirm = Button(self, text="Yes", command=self.restart)
			#self.confirm.grid()
			self.QUIT.grid()
			
	def RNAi(self):
		"Creates a vector for RNA interference of a targeted gene"
		
			
		self.l_5f = Label(self,text="5' Flank Sequence:")
		self.l_5f.grid(row=0,column=0)
		self.l_3f = Label(self,text="3' Flank Sequence:")
		self.l_3f.grid(row=1, column=0)
		self.t_5f = Text(self)
		self.t_5f.grid(row=0,column=1)
		self.t_3f = Text(self)
		self.t_3f.grid(row=1,column=1)
		self.l_e1 = Label(self,text="Enzyme 1 sequence")
		self.l_e1.grid(row=2,column=0)
		self.l_e2 = Label(self,text="Enzyme 2 sequence")
		self.l_e2.grid(row=3,column=0)
		self.l_e3 = Label(self,text="Enzyme 3 sequence")
		self.l_e3.grid(row=4,column=0)
		self.l_e4 = Label(self,text="Enzyme 4 sequence")
		self.l_e4.grid(row=5,column=0)
		self.t_e1 = Entry(self)
		self.t_e1.grid(row=2,column=1)
		self.t_e2 = Entry(self)
		self.t_e2.grid(row=3,column=1)
		self.t_e3 = Entry(self)
		self.t_e3.grid(row=4,column=1)
		self.t_e4 = Entry(self)
		self.t_e4.grid(row=5,column=1)
		vector = self.vector_sequence.get("1.0",END)
		flank1 = self.t_5f.get("1.0",END)
		flank2 = self.t_3f.get("1.0",END)
		e1 = self.t_e1.get()
		e2 = self.t_e2.get()
		e3 = self.t_e3.get()
		e4 = self.t_e4.get()
		self.rnai_button = Button(self,text="Submit",command=self.process)
		self.rnai_button.grid(row=6,column=0)
		self.QUIT.grid(row=6,column=1)
		
		
		
	def clone_logic(self, type):
			"Changes the cloning method"
			if type == "RNAi":
				print("You have selected RNAi")
				#self.lab_seq.grid_forget()
				#self.vector_sequence.grid_forget()
				#self.button_method.grid_forget()
				forget = [self.lab_seq,self.vector_sequence,self.button_method,self.QUIT]
				self.forget_me(forget)
				self.RNAi()
				
				#self.button_method = Button(self)
				#self.button_method["text"] = "submit"
				#self.button_method["command"] = self.RNAi
				#self.button_method.grid(row=3, column=0)
				
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
		forget = [self.clone_type,self.submit_button,self.l_name,self.final_name,self.instruct]
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
