import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(117, 267)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(116, 61)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(117, 335)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(116, 35)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(117, 377)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(116, 39)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(43, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(161, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(43, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "label2"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(161, 40)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(161, 122)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(161, 149)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(161, 176)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(34, 122)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "label6"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(34, 149)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(34, 176)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 12
		self._label8.Text = "label8"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(419, 447)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg240"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		rate = int(self._textBox1.Text)
		if rate < 10000:
			self._label3.Text = "5%"
			comm = 0.05
			thing = int(self._textBox2.Text)
			comm1 = rate * comm
			total = comm1 - thing
			self._label5.Text = str(total)
			self._label4.Text = str(comm1)
		elif rate >= 10000 and rate <= 14999:
			self._label3.Text = "10%"
			comm = 0.1
			thing = int(self._textBox2.Text)
			comm1 = rate * comm
			total = comm1 - thing
			self._label5.Text = str(total)
			self._label4.Text = str(comm1)
		elif rate >= 15000 and rate <= 17999:
			self._label3.Text = "12%"
			comm = 0.12
			thing = int(self._textBox2.Text)
			comm1 = rate * comm
			total = comm1 - thing
			self._label5.Text = str(total)
			self._label4.Text = str(comm1)
		elif rate >= 18000 and rate <= 21999:
			self._label3.Text = "14%"
			comm = 0.14
			thing = int(self._textBox2.Text)
			comm1 = rate * comm
			total = comm1 - thing
			self._label5.Text = str(total)
			self._label4.Text = str(comm1)
		elif rate >= 22000:
			self._label3.Text = "16%"
			comm = 0.16
			thing = int(self._textBox2.Text)
			comm1 = rate * comm
			total = comm1 - thing
			self._label5.Text = str(total)
			self._label4.Text = str(comm1)
		
		
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()