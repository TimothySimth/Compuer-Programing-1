require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox
class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(225, 24)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(241, 23)
		@label1.TabIndex = 0
		@label1.Text = "radius"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(472, 24)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(250, 20)
		@textBox1.TabIndex = 2
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(225, 168)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 4
		@button1.Text = "Caculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(432, 168)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 5
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(647, 168)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(75, 23)
		@button3.TabIndex = 6
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label3.Location = System::Drawing::Point.new(225, 49)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(497, 58)
		@label3.TabIndex = 7
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label4.Location = System::Drawing::Point.new(225, 107)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(497, 58)
		@label4.TabIndex = 8
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(954, 621)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		radius = float(@textBox1.Text)
		pi = 3.14159
		Area = pi * radius ** 2
		Area = round(Area,3)
		Circumference = 2 * pi * radius
		Circumference = round(Area,3)
		@label3.Text = "Area: " + str(Area)
		@label4.Text = "Circumference: " + str(Circumference)
		
		
		
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

