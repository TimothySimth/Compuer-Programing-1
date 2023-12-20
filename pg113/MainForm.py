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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(333, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(216, 49)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(333, 63)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(216, 49)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.MenuText
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Turquoise
		self._label1.Location = System.Drawing.Point(128, 10)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(199, 53)
		self._label1.TabIndex = 2
		self._label1.Text = "First name"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.MenuText
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Turquoise
		self._label2.Location = System.Drawing.Point(128, 63)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(199, 53)
		self._label2.TabIndex = 3
		self._label2.Text = "Last name"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.InactiveCaptionText
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Thistle
		self._button1.Location = System.Drawing.Point(12, 321)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(184, 92)
		self._button1.TabIndex = 4
		self._button1.Text = "Show Name"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.InactiveCaptionText
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Thistle
		self._button2.Location = System.Drawing.Point(255, 321)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(184, 92)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.InactiveCaptionText
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Thistle
		self._button3.Location = System.Drawing.Point(489, 321)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(184, 92)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Yellow
		self._label3.Location = System.Drawing.Point(-4, 116)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(710, 202)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSalmon
		self.ClientSize = System.Drawing.Size(718, 425)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "pg113"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		fn = self._textBox1.Text
		ln = self._textBox2.Text
		self._label3.Text = fn + " " + ln

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def MainFormLoad(self, sender, e):
		pass