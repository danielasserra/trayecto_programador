namespace Clase01_formularios
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            MessageBox.Show("new");
            InitializeComponent();
        }

        private void BtnSaludar_Click(object sender, EventArgs e)
        {
            String texto;
            String nombre;
            nombre = txtSaludo.Text; //me permite tener el texto del textbox
            texto = "Hola " + nombre + ", ¿como estas?";

            //mostrar texto dentro del label
            //lblSaludo.Text = "hola " + texto + "¿como estas?";

            MessageBox.Show(texto);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            MessageBox.Show("en el paint");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //MessageBox.Show("en el load");
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            //MessageBox.Show("en el activated");
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            DialogResult d = MessageBox.Show("estoy cerrando", "mi app", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (d == DialogResult.NO)
            {
                e.Cancel = true; // e es un parametro que recibo en FormClosingEventArgs
                                 // va a cancelar el cierre del form
            }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            MessageBox.Show("en el closed");
        }
    }
}
