using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _Arbol_AVL
{
    public partial class Form1 : Form
    {
        private enum ModoDibujo
        {
            Ninguno,
            Recorrido,
            Busqueda
        }

        int dato = 0;
        ArbolAVL arbolAVL = new ArbolAVL(null);
        Graphics g;
        private ModoDibujo modoDibujo = ModoDibujo.Ninguno;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            g = e.Graphics;

            arbolAVL.DibujarArbol(g, this.Font,
                Brushes.White, Brushes.Black, Pens.White, dato, Brushes.Black);

            switch (modoDibujo)
            {
                case ModoDibujo.Recorrido:
                    arbolAVL.Colorear(g, Font, Brushes.Black, Brushes.Yellow, Pens.Blue, arbolAVL.Raiz,
                        rbPostOrden.Checked, rbEnOrden.Checked, rbPreOrden.Checked);
                    break;

                case ModoDibujo.Busqueda:
                    arbolAVL.ColorearBusqueda(g, Font, Brushes.White, Brushes.Red, Pens.White,
                        arbolAVL.Raiz, dato);
                    break;
            }

            modoDibujo = ModoDibujo.Ninguno;
            dato = 0;

        }

        private void btnAgregar_Click(object sender, EventArgs e)
        {
            errores.Clear();
            if (valor.Text == "")
            {
                errores.SetError(valor, "Valor obligatorio");
            }
            else
            {
                try
                {
                    dato = int.Parse(valor.Text);
                    arbolAVL.Insertar(dato);
                    valor.Clear();
                    valor.Focus();
                    lblAltura.Text = arbolAVL.Raiz.ObtenerAltura(arbolAVL.Raiz).ToString();
                    Refresh();
                    lblTipo.Text = NodoAVL.UltimaRotacion; // Mostrar tipo de rotacion
                    Refresh();
                }
                catch (Exception ex)
                {
                    errores.SetError(valor, "Debe ser numérico");
                }
            }
        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            errores.Clear();
            if (valor.Text == "")
            {
                errores.SetError(valor, "Valor obligatorio");
            }
            else
            {
                try
                {
                    dato = int.Parse(valor.Text);
                    arbolAVL.Buscar(dato);
                    modoDibujo = ModoDibujo.Busqueda;
                    Refresh();
                    Refresh();
                    valor.Clear();
                }
                catch (Exception ex)
                {
                    errores.SetError(valor, "Debe ser numérico");
                }
            }

        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            errores.Clear();
            if (valor.Text == "")
            {
                errores.SetError(valor, "Valor obligatorio");
            }
            else
            {
                try
                {
                    dato = int.Parse(valor.Text);
                    valor.Clear();
                    arbolAVL.Eliminar(dato);
                    lblAltura.Text = arbolAVL.Raiz.ObtenerAltura(arbolAVL.Raiz).ToString();
                    Refresh();
                    lblTipo.Text = NodoAVL.UltimaRotacion; // Mostrar tipo de rotacion
                    Refresh();
                }
                catch (Exception ex)
                {
                    errores.SetError(valor, "Debe ser numerico");
                }
            }

        }

        private void btnSalir_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void rbPreOrden_CheckedChanged(object sender, EventArgs e)
        {
            if (rbPreOrden.Checked)
            {
                modoDibujo = ModoDibujo.Recorrido;
                txtRecorrido.Text = arbolAVL.ObtenerRecorrido("PreOrden");
                Refresh();
            }
        }

        private void rbEnOrden_CheckedChanged(object sender, EventArgs e)
        {
            if (rbEnOrden.Checked)
            {
                modoDibujo = ModoDibujo.Recorrido;
                txtRecorrido.Text = arbolAVL.ObtenerRecorrido("InOrden");
                Refresh();
            }
        }

        private void rbPostOrden_CheckedChanged(object sender, EventArgs e)
        {
            if (rbPostOrden.Checked)
            {
                modoDibujo = ModoDibujo.Recorrido;
                txtRecorrido.Text = arbolAVL.ObtenerRecorrido("PostOrden");
                Refresh();
            }
        }

    }
}
