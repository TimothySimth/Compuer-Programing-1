import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(117, 25)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(117, 52)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(117, 79)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(117, 106)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumSeaGreen
		self._label2.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label2.Location = System.Drawing.Point(11, 22)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Test score 1"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LemonChiffon
		self._label3.ForeColor = System.Drawing.SystemColors.ControlDark
		self._label3.Location = System.Drawing.Point(12, 49)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Test score 2"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Indigo
		self._label4.ForeColor = System.Drawing.Color.Crimson
		self._label4.Location = System.Drawing.Point(11, 76)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Test score 3"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LavenderBlush
		self._button1.Location = System.Drawing.Point(38, 194)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 7
		self._button1.Text = "Caluclate avrege"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(39, 223)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Lavender
		self._button3.Location = System.Drawing.Point(39, 252)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LawnGreen
		self._label5.ForeColor = System.Drawing.SystemColors.ControlText
		self._label5.Location = System.Drawing.Point(13, 103)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 10
		self._label5.Text = "Avrege Test score"
		# 
		# label6
		# 
		self._label6.ForeColor = System.Drawing.Color.Red
		self._label6.Location = System.Drawing.Point(24, 139)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(193, 40)
		self._label6.TabIndex = 11
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Khaki
		self.ClientSize = System.Drawing.Size(239, 289)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "pg198"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		num3 = float(self._textBox3.Text)
		num4 = num1 + num2 + num3 
		num5 = num4 / 3
		self._label1.Text = str(num5)
		if num5 >= 95:
			self._label6.Text = "Good Job!!"

	def Label3Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label1.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()