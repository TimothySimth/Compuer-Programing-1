require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@show = System::Windows::Forms::Button.new()
		@Clear = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		@label7 = System::Windows::Forms::Label.new()
		@label8 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# show
		# 
		@show.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@show.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@show.Location = System::Drawing::Point.new(314, 317)
		@show.Name = "show"
		@show.Size = System::Drawing::Size.new(86, 23)
		@show.TabIndex = 0
		@show.Text = "Show"
		@show.UseVisualStyleBackColor = false
		@show.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# Clear
		# 
		@Clear.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@Clear.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@Clear.Location = System::Drawing::Point.new(398, 317)
		@Clear.Name = "Clear"
		@Clear.Size = System::Drawing::Size.new(100, 23)
		@Clear.TabIndex = 1
		@Clear.Text = "Clear"
		@Clear.UseVisualStyleBackColor = false
		@Clear.Click { |sender, e| self.ClearClick(sender, e) }
		# 
		# label1
		# 
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(314, 292)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(184, 22)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label2.Location = System::Drawing::Point.new(314, 269)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(184, 23)
		@label2.TabIndex = 3
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label3.Location = System::Drawing::Point.new(314, 249)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(184, 20)
		@label3.TabIndex = 4
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label4.Location = System::Drawing::Point.new(314, 226)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(184, 23)
		@label4.TabIndex = 5
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label4.Click { |sender, e| self.Label4Click(sender, e) }
		# 
		# label5
		# 
		@label5.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label5.Location = System::Drawing::Point.new(314, 203)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(184, 23)
		@label5.TabIndex = 6
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		@label6.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label6.Location = System::Drawing::Point.new(314, 180)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(184, 23)
		@label6.TabIndex = 7
		@label6.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		@label7.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label7.Location = System::Drawing::Point.new(314, 157)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(184, 23)
		@label7.TabIndex = 8
		@label7.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		@label8.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label8.Location = System::Drawing::Point.new(314, 134)
		@label8.Name = "label8"
		@label8.Size = System::Drawing::Size.new(184, 23)
		@label8.TabIndex = 9
		@label8.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(893, 449)
		self.Controls.Add(@label8)
		self.Controls.Add(@label7)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@Clear)
		self.Controls.Add(@show)
		self.Name = "MainForm"
		self.Text = "Your Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Math"
		@label2.Text = "Freshman Seminar"
		@label3.Text = "Computer Programing"
		@label4.Text = "Study Hall"
		@label5.Text = "Science"
		@label6.Text = "Spanish"
		@label7.Text = "English"
		@label8.Text = "AP human geo"
	end

	def ClearClick(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
		@label6.Text = ""
		@label7.Text = ""
		@label8.Text = ""
	end
end

