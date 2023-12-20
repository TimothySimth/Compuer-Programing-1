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
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(521, 262)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 54)
		self._button1.TabIndex = 0
		self._button1.Text = "clear"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(617, 262)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 54)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(470, 29)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 54)
		self._button3.TabIndex = 2
		self._button3.Text = "+"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(566, 29)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(90, 54)
		self._button4.TabIndex = 3
		self._button4.Text = "-"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(662, 29)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(90, 54)
		self._button5.TabIndex = 4
		self._button5.Text = "X"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(470, 89)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(90, 54)
		self._button6.TabIndex = 5
		self._button6.Text = "^"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(566, 89)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(90, 54)
		self._button7.TabIndex = 6
		self._button7.Text = "/"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(662, 89)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(90, 54)
		self._button8.TabIndex = 7
		self._button8.Text = "//"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(566, 149)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(90, 54)
		self._button9.TabIndex = 8
		self._button9.Text = "MOD"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(0, 0)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 16
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Transparent
		self._label2.Location = System.Drawing.Point(140, 125)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 10
		self._label2.Click += self.Label2Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(140, 47)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 11
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(140, 102)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 12
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(34, 44)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 13
		self._label3.Text = "Number1"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(34, 98)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 14
		self._label4.Text = "Number2"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(34, 125)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 15
		self._label5.Text = "Answer"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(140, 70)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 17
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(838, 478)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg140"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		self._label6.Text = "+"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 + num2
		self._label2.Text = str(answer)

	def Button4Click(self, sender, e):
		self._label6.Text = "-"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 - num2
		self._label2.Text = str(answer)


	def Button5Click(self, sender, e):
		self._label6.Text = "X"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 * num2
		self._label2.Text = str(answer)


	def Button6Click(self, sender, e):
		self._label6.Text = "^"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 ** num2
		self._label2.Text = str(answer)

	def Button7Click(self, sender, e):
		self._label6.Text = "/"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 / num2
		self._label2.Text = str(answer)

	def Button8Click(self, sender, e):
		self._label6.Text = "//"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 // num2
		self._label2.Text = str(answer)

	def Button9Click(self, sender, e):
		self._label6.Text = "MOD"
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		answer = num1 % num2
		self._label2.Text = str(answer)

	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label2.Text = ""
		self._label6.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()

	def Label2Click(self, sender, e):
		self._label2.Text = "HEHEHEHE"

	def TextBox1TextChanged(self, sender, e):
		self._label2.Text = ""

	def TextBox2TextChanged(self, sender, e):
		self._label2.Text = ""

	def Label3Click(self, sender, e):
		self._label2.Text = "HEHEHEHE"

	def Label4Click(self, sender, e):
		self._label2.Text = "HEHEHEHE"

	def Label5Click(self, sender, e):
		self._label2.Text = "HEHEHEHE"