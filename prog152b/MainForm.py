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
					self._textBox1 = System.Windows.Forms.TextBox()
					self._label1 = System.Windows.Forms.Label()
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.Location = System.Drawing.Point(3, 270)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(242, 285)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.Location = System.Drawing.Point(251, 270)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(206, 285)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.Location = System.Drawing.Point(463, 270)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(255, 285)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# listBox1
					# 
					self._listBox1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
					self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.ForeColor = System.Drawing.Color.DarkRed
					self._listBox1.FormattingEnabled = True
					self._listBox1.ItemHeight = 33
					self._listBox1.Location = System.Drawing.Point(13, 13)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(705, 202)
					self._listBox1.TabIndex = 3
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.SystemColors.HotTrack
					self._textBox1.ForeColor = System.Drawing.Color.Black
					self._textBox1.Location = System.Drawing.Point(13, 244)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(705, 20)
					self._textBox1.TabIndex = 4
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
					self._label1.Location = System.Drawing.Point(13, 218)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(93, 23)
					self._label1.TabIndex = 5
					self._label1.Text = "Enter Num:"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.Lime
					self.ClientSize = System.Drawing.Size(730, 567)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._listBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "Prog152b"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        Heading = "Num \t\t Sum"
        self._listBox1.Items.Add(Heading)
        Num1 = self._textBox1.Text
        Num1 = int(Num1)
        l = 0
        for num in range(2, Num1+2, 2):
            if l <= Num1:
                
                l = num + l
                
                Final = str(num) + " \t\t" + str(l)
                self._listBox1.Items.Add(Final)


    def Button2Click(self, sender, e):
        self._listBox1.Clear()
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit() 