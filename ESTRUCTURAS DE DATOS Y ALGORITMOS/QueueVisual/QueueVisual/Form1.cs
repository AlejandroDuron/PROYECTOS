using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace QueueVisual
{
    public partial class Form1 : Form
    {
        Queue<Empleado> trabajadores = new Queue<Empleado>();

        public Form1()
        {
            InitializeComponent();
        }

        public void Clear()
        {
            txtcarnet.Clear();
            txtnombre.Clear();
            txtsalario.Clear();
        }
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Empleado empleado = new Empleado();
            empleado.Carnet = txtcarnet.Text;
            empleado.Nombre = txtnombre.Text;
            empleado.Salario = Decimal.Parse(txtsalario.Text);
            empleado.Fecha = fecha.Value;

            trabajadores.Enqueue(empleado);
            dgvCola.DataSource = null;
            dgvCola.DataSource = trabajadores.ToArray();
            Clear();
            txtcarnet.Focus();  
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (trabajadores.Count != 0)
            {
                Empleado empleado = new Empleado();
                empleado = trabajadores.Dequeue();

                txtcarnet.Text = empleado.Carnet;
                txtnombre.Text = empleado.Nombre;
                txtsalario.Text = empleado.Salario.ToString();
                fecha.Value = empleado.Fecha;

                dgvCola.DataSource = trabajadores.ToList();
                MessageBox.Show("Se eleimino el registro de la cola", "AVISO");
                Clear();
            }
            else
            {
                MessageBox.Show("No hay empleados en la cola", "AVISO");
                Clear();
            }
            txtcarnet.Focus();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
