namespace Clase01_formularios
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            BtnSaludar = new Button();
            txtSaludo = new TextBox();
            SuspendLayout();
            // 
            // BtnSaludar
            // 
            BtnSaludar.Location = new Point(354, 265);
            BtnSaludar.Name = "BtnSaludar";
            BtnSaludar.Size = new Size(91, 48);
            BtnSaludar.TabIndex = 0;
            BtnSaludar.Text = "Saludar";
            BtnSaludar.UseVisualStyleBackColor = true;
            BtnSaludar.Click += BtnSaludar_Click;
            // 
            // txtSaludo
            // 
            txtSaludo.BackColor = SystemColors.MenuHighlight;
            txtSaludo.Location = new Point(272, 146);
            txtSaludo.Name = "txtSaludo";
            txtSaludo.Size = new Size(266, 27);
            txtSaludo.TabIndex = 2;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.ActiveCaption;
            ClientSize = new Size(800, 450);
            Controls.Add(txtSaludo);
            Controls.Add(BtnSaludar);
            Name = "Form1";
            Text = "Inicio";
            Activated += Form1_Activated;
            FormClosing += Form1_FormClosing;
            FormClosed += Form1_FormClosed;
            Load += Form1_Load;
            Paint += Form1_Paint;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button BtnSaludar;
        private TextBox txtSaludo;
    }
}
