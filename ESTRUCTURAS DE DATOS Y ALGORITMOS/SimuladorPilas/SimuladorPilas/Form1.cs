using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SimuladorPilas
{
    public partial class Form1 : Form
    {
        int x = 0, y = 70;

        Stack<Label> myStack = new Stack<Label>();
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnPop_Click(object sender, EventArgs e)
        {
            if (myStack.Count == 0)
            {
                MessageBox.Show("la pila esta vacía"); // mbox -> tab
                return;
            }
           // Label deleted = myStack.Pop(); //almaceno la variable eliminada
           // panel1.Controls.Remove(deleted);
           // x -= deleted.Width;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Label nuevo = myStack.Peek();
            nuevo.BackColor = Color.Aqua;
            if (nuevo.Location.X < x)
            {
                nuevo.Location = new Point(nuevo.Location.X + 10, nuevo.Location.Y);
                return;
            }

            if (nuevo.Location.Y < y)
            {
                nuevo.Location = new Point(nuevo.Location.X, nuevo.Location.Y + 10);
                return;
            }

            x += nuevo.Width;
            timer1.Stop();
            nuevo.BackColor = Color.White;

        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            
            
                Label deleted = myStack.Pop();
                MessageBox.Show("la pila esta vacía"); // mbox -> tab
                return;
            
            
            if (deleted.Location.X > x)
            {
                deleted.Location = new Point(deleted.Location.X - 10, deleted.Location.Y);
                return;
            }
            if (deleted.Location.Y > y)
            {
                deleted.Location = new Point(deleted.Location.X, deleted.Location.Y - 10);
                return;
            }


            x -= deleted.Width;
            panel1.Controls.Remove(deleted);
            timer2.Stop();

        }

        private void btnPush_Click(object sender, EventArgs e)
        {
            int valor = (int) numValor.Value;
            Label label = new Label();
            label.Width = 50;
            label.Height = 50;  
            label.BackColor = Color.White;
            label.Text = valor.ToString();
            label.BorderStyle = BorderStyle.FixedSingle; //borde sencillo
            //label.Location = new Point(x, y);
            label.Location = new Point(0, 0);
            label.TextAlign = ContentAlignment.MiddleLeft;
            // x += label.Width;
            myStack.Push(label);
            panel1.Controls.Add(label);

            timer1.Start(); 
            timer2.Start(); 
            
        }
    }
}
