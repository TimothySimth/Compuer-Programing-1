import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label1.Location = System.Drawing.Point(184, 38)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(166, 47)
		self._label1.TabIndex = 0
		self._label1.Text = "Salary"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(372, 47)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(169, 47)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(372, 91)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(169, 47)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Cyan
		self._label2.Location = System.Drawing.Point(184, 91)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(166, 47)
		self._label2.TabIndex = 2
		self._label2.Text = "Number of pay periods"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Cyan
		self._label3.Location = System.Drawing.Point(184, 144)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(166, 47)
		self._label3.TabIndex = 4
		self._label3.Text = "Salary per pay period"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(126, 316)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(162, 84)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Coral
		self._button2.Location = System.Drawing.Point(345, 316)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(162, 84)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkBlue
		self._button3.Location = System.Drawing.Point(572, 316)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(162, 84)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(372, 145)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(169, 46)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonShadow
		self.ClientSize = System.Drawing.Size(844, 477)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg153"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		h = int(self._textBox1.Text)
		j = int(self._textBox2.Text)
		k = h / j
		self._label4.Text = str(k)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()