require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.HighlightText
		@label1.Location = System::Drawing::Point.new(144, 24)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(477, 23)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::SystemColors.HighlightText
		@label2.Location = System::Drawing::Point.new(144, 47)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(477, 23)
		@label2.TabIndex = 1
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::SystemColors.HighlightText
		@label3.Location = System::Drawing::Point.new(144, 70)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(477, 23)
		@label3.TabIndex = 2
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::SystemColors.HighlightText
		@label4.Location = System::Drawing::Point.new(144, 92)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(477, 23)
		@label4.TabIndex = 3
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.ForeColor = System::Drawing::SystemColors.HighlightText
		@label5.Location = System::Drawing::Point.new(144, 115)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(477, 23)
		@label5.TabIndex = 4
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlText
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.HighlightText
		@button1.Location = System::Drawing::Point.new(144, 169)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(234, 127)
		@button1.TabIndex = 5
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.InfoText
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.HighlightText
		@button2.Location = System::Drawing::Point.new(384, 169)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(237, 127)
		@button2.TabIndex = 6
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(890, 436)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Phone nubers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "868-865-8658"
		@label2.Text = "564-654-8779"
		@label3.Text = "842-847-7493"
		@label4.Text = "383-474-5435"
		@label5.Text = "957-585-3859"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
	end
end

