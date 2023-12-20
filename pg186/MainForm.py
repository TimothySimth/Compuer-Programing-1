import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
					self._label1 = System.Windows.Forms.Label()
					self._label2 = System.Windows.Forms.Label()
					self._label3 = System.Windows.Forms.Label()
					self._label4 = System.Windows.Forms.Label()
					self._label5 = System.Windows.Forms.Label()
					self._textBox1 = System.Windows.Forms.TextBox()
					self._textBox2 = System.Windows.Forms.TextBox()
					self._textBox3 = System.Windows.Forms.TextBox()
					self._label6 = System.Windows.Forms.Label()
					self._label7 = System.Windows.Forms.Label()
					self._label8 = System.Windows.Forms.Label()
					self._label9 = System.Windows.Forms.Label()
					self._label10 = System.Windows.Forms.Label()
					self._label11 = System.Windows.Forms.Label()
					self._label12 = System.Windows.Forms.Label()
					self._label13 = System.Windows.Forms.Label()
					self._label14 = System.Windows.Forms.Label()
					self._button1 = System.Windows.Forms.Button()
					self._button2 = System.Windows.Forms.Button()
					self._button3 = System.Windows.Forms.Button()
					self.SuspendLayout()
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.PaleVioletRed
					self._label1.Location = System.Drawing.Point(12, 19)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(354, 36)
					self._label1.TabIndex = 0
					self._label1.Text = "Tickets Sold"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label2
					# 
					self._label2.BackColor = System.Drawing.Color.DarkOrchid
					self._label2.Location = System.Drawing.Point(12, 72)
					self._label2.Name = "label2"
					self._label2.Size = System.Drawing.Size(354, 36)
					self._label2.TabIndex = 1
					self._label2.Text = "Enter number of tickets sold for each class of seats"
					self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label3
					# 
					self._label3.BackColor = System.Drawing.Color.HotPink
					self._label3.Location = System.Drawing.Point(12, 126)
					self._label3.Name = "label3"
					self._label3.Size = System.Drawing.Size(208, 36)
					self._label3.TabIndex = 2
					self._label3.Text = "Class A"
					self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label4
					# 
					self._label4.BackColor = System.Drawing.Color.DarkOrchid
					self._label4.Location = System.Drawing.Point(12, 182)
					self._label4.Name = "label4"
					self._label4.Size = System.Drawing.Size(208, 36)
					self._label4.TabIndex = 3
					self._label4.Text = "Class B"
					self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label5
					# 
					self._label5.BackColor = System.Drawing.Color.Thistle
					self._label5.Location = System.Drawing.Point(12, 234)
					self._label5.Name = "label5"
					self._label5.Size = System.Drawing.Size(208, 36)
					self._label5.TabIndex = 4
					self._label5.Text = "Class C"
					self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# textBox1
					# 
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(228, 126)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(138, 31)
					self._textBox1.TabIndex = 5
					# 
					# textBox2
					# 
					self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox2.Location = System.Drawing.Point(228, 187)
					self._textBox2.Name = "textBox2"
					self._textBox2.Size = System.Drawing.Size(138, 31)
					self._textBox2.TabIndex = 6
					# 
					# textBox3
					# 
					self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox3.Location = System.Drawing.Point(228, 234)
					self._textBox3.Name = "textBox3"
					self._textBox3.Size = System.Drawing.Size(138, 31)
					self._textBox3.TabIndex = 7
					# 
					# label6
					# 
					self._label6.BackColor = System.Drawing.Color.PaleVioletRed
					self._label6.Location = System.Drawing.Point(372, 19)
					self._label6.Name = "label6"
					self._label6.Size = System.Drawing.Size(418, 36)
					self._label6.TabIndex = 8
					self._label6.Text = "Revenue Made"
					self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label7
					# 
					self._label7.BackColor = System.Drawing.Color.Lavender
					self._label7.Location = System.Drawing.Point(615, 67)
					self._label7.Name = "label7"
					self._label7.Size = System.Drawing.Size(166, 72)
					self._label7.TabIndex = 9
					self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label8
					# 
					self._label8.BackColor = System.Drawing.Color.Lavender
					self._label8.Location = System.Drawing.Point(615, 164)
					self._label8.Name = "label8"
					self._label8.Size = System.Drawing.Size(166, 72)
					self._label8.TabIndex = 10
					self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label9
					# 
					self._label9.BackColor = System.Drawing.Color.Lavender
					self._label9.Location = System.Drawing.Point(615, 260)
					self._label9.Name = "label9"
					self._label9.Size = System.Drawing.Size(166, 72)
					self._label9.TabIndex = 11
					self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label10
					# 
					self._label10.BackColor = System.Drawing.Color.Lavender
					self._label10.Location = System.Drawing.Point(477, 344)
					self._label10.Name = "label10"
					self._label10.Size = System.Drawing.Size(304, 106)
					self._label10.TabIndex = 12
					self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label11
					# 
					self._label11.BackColor = System.Drawing.Color.Thistle
					self._label11.Location = System.Drawing.Point(503, 67)
					self._label11.Name = "label11"
					self._label11.Size = System.Drawing.Size(100, 72)
					self._label11.TabIndex = 13
					self._label11.Text = "Class A"
					self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label12
					# 
					self._label12.BackColor = System.Drawing.SystemColors.ActiveBorder
					self._label12.Location = System.Drawing.Point(503, 164)
					self._label12.Name = "label12"
					self._label12.Size = System.Drawing.Size(100, 72)
					self._label12.TabIndex = 14
					self._label12.Text = "Class B"
					self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label13
					# 
					self._label13.BackColor = System.Drawing.Color.LightBlue
					self._label13.Location = System.Drawing.Point(503, 260)
					self._label13.Name = "label13"
					self._label13.Size = System.Drawing.Size(100, 72)
					self._label13.TabIndex = 15
					self._label13.Text = "Class C"
					self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label14
					# 
					self._label14.BackColor = System.Drawing.Color.Turquoise
					self._label14.Location = System.Drawing.Point(372, 344)
					self._label14.Name = "label14"
					self._label14.Size = System.Drawing.Size(100, 106)
					self._label14.TabIndex = 16
					self._label14.Text = "Total Revenue"
					self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.Transparent
					self._button1.Location = System.Drawing.Point(0, 377)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(270, 88)
					self._button1.TabIndex = 17
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.HotPink
					self._button2.Location = System.Drawing.Point(12, 275)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(132, 88)
					self._button2.TabIndex = 18
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.SaddleBrown
					self._button3.Location = System.Drawing.Point(150, 275)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(132, 88)
					self._button3.TabIndex = 19
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.Orchid
					self.ClientSize = System.Drawing.Size(802, 477)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Controls.Add(self._label14)
					self.Controls.Add(self._label13)
					self.Controls.Add(self._label12)
					self.Controls.Add(self._label11)
					self.Controls.Add(self._label10)
					self.Controls.Add(self._label9)
					self.Controls.Add(self._label8)
					self.Controls.Add(self._label7)
					self.Controls.Add(self._label6)
					self.Controls.Add(self._textBox3)
					self.Controls.Add(self._textBox2)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._label5)
					self.Controls.Add(self._label4)
					self.Controls.Add(self._label3)
					self.Controls.Add(self._label2)
					self.Controls.Add(self._label1)
					self.Name = "MainForm"
					self.Text = "pg186"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        A = 15
        B = 12
        C = 9
        ClassA = A * int(self._textBox1.Text)
        ClassB = B * int(self._textBox1.Text)
        ClassC = C * int(self._textBox1.Text)
        Revenue = ClassA + ClassB + ClassC
        self._label7.Text = str(ClassA)
        self._label8.Text = str(ClassB)
        self._label9.Text = str(ClassC)
        self._label10.Text = str(Revenue)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""
        self._label10.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()   