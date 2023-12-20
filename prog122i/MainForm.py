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
					self._button1.BackColor = System.Drawing.Color.DarkViolet
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.ForeColor = System.Drawing.Color.White
					self._button1.Location = System.Drawing.Point(26, 433)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(200, 152)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.DarkOrchid
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.ForeColor = System.Drawing.Color.White
					self._button2.Location = System.Drawing.Point(396, 433)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(200, 152)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.DarkOrchid
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.ForeColor = System.Drawing.Color.White
					self._button3.Location = System.Drawing.Point(744, 433)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(200, 152)
					self._button3.TabIndex = 2
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					# 
					# listBox1
					# 
					self._listBox1.BackColor = System.Drawing.Color.MediumSlateBlue
					self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.FormattingEnabled = True
					self._listBox1.ItemHeight = 25
					self._listBox1.Location = System.Drawing.Point(26, 13)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(918, 404)
					self._listBox1.TabIndex = 3
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.LemonChiffon
					self.ClientSize = System.Drawing.Size(956, 597)
					self.Controls.Add(self._listBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "prog122c"
					self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Number\tCube Root\tCube"
        self._listBox1.Items.Add(heading)
        
        for num in range(-25, 25+1):
        	Cube = num * 3
        	if num>=0:
        		Cuberoot = Cube**0.33333333333
        		
        	else:
        		this = abs(num)
        		that = this**0.33333333333
        		Cuberoot = -that
        	
        
        
        	Cubroot = round(Cuberoot, 5)
        	Filn = str(num) + "\t" + str(Cuberoot) + "\t" + str(Cube)
       		self._listBox1.Items.Add(Filn)  
        	    

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()      