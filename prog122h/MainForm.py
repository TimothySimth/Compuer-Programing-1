import math
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
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Teal
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MediumVioletRed
		self._button1.Location = System.Drawing.Point(12, 419)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(267, 174)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Teal
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MediumVioletRed
		self._button2.Location = System.Drawing.Point(338, 419)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(267, 174)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Teal
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MediumVioletRed
		self._button3.Location = System.Drawing.Point(646, 419)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(267, 174)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.MediumBlue
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.LimeGreen
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 33
		self._listBox1.Location = System.Drawing.Point(12, 8)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(901, 367)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(925, 605)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\tSquare\tSquare Root\tCube\t4th root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 50+1):
			nsqrd = num**2
			nsqrt = math.sqrt(num)
			cube = num**3
			four = num**.25
			msg = str(num) + "\t" + str(nsqrd) + "\t" + str(round(nsqrt, 4)) + "\t\t" + str(cube) + "\t" + str(four)
			self._listBox1.Items.Add(msg)
			
			

	def Button2Click(self, sender, e):
		self._listBox1.Items.clear()

	def Button3Click(self, sender, e):
		Application.Exit()