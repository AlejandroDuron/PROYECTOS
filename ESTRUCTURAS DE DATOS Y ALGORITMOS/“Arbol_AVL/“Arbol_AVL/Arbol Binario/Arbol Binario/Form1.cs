using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Arbol_Binario
{
    public partial class Form1 : Form
    {

        // Declaración de variables a utilizar
        int dato = 0;
        ArbolBinario miArbol; // Instancia de la clase ArbolBinario
        FormatoNodo formatoNodo; // Variable struct para definir elementos graficos: color, relleno, etc
        Graphics g; // Definicion del objeto grafico

        public Form1()
        {
            InitializeComponent();

            miArbol = new ArbolBinario(null); // Creación del objeto Árbol

            // Define colores a usar para dibujar el Arbol Binario en area de dibujo
            formatoNodo.fuente = this.Font;
            formatoNodo.relleno = Brushes.Blue;
            formatoNodo.rellenofuente = Brushes.White;
            formatoNodo.lapiz = Pens.Black;
            formatoNodo.encuentro = Brushes.White;

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);  // Limpiar el fondo del panel
            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;  // Mejora el renderizado de texto
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;  // Suavizado de líneas

            g = e.Graphics;  // Obtener el objeto gráfico para dibujar
            miArbol.DibujarArbol(g, panel1.Size, formatoNodo);  // Llamada al metodo para dibujar el árbol

        }

        private void btnInsertar_Click(object sender, EventArgs e)
        {
            if (txtDato.Text == "")
            {
                MessageBox.Show("Debe Ingresar un Valor");
            }
            else
            {
                dato = int.Parse(txtDato.Text);
                if (dato <= 0 || dato >= 100)
                {
                    MessageBox.Show("Solo Recibe Valores desde 1 hasta 99", "Error de Ingreso");
                }
                else
                {
                    miArbol.Insertar(dato);
                    txtDato.Clear();
                    txtDato.Focus();
                    panel1.Refresh(); // Actualiza contenido presentado en control panel1
                }
            }

        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            if (txtEliminar.Text == "")
            {
                MessageBox.Show("Debe ingresar el valor a eliminar");
            }
            else
            {
                dato = Convert.ToInt32(txtEliminar.Text);
                if (dato <= 0 || dato >= 100)
                {
                    MessageBox.Show("Sólo se admiten valores entre 1 y 99", "Error de Ingreso");
                }
                else
                {
                    miArbol.Eliminar(dato);
                    txtEliminar.Clear();
                    txtEliminar.Focus();
                    panel1.Refresh();
                }
            }

        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            if (txtBuscar.Text == "")
            {
                MessageBox.Show("Debe ingresar el valor a buscar");
            }
            else
            {
                dato = Convert.ToInt32(txtBuscar.Text);
                if (dato <= 0 || dato >= 100)
                {
                    MessageBox.Show("Sólo se admiten valores entre 1 y 99", "Error de Ingreso");
                }
                else
                {
                    FormatoNodo formatoNodoEncontrado;
                    formatoNodoEncontrado = formatoNodo;
                    formatoNodoEncontrado.relleno = Brushes.Red;
                    miArbol.BuscarEnArbol(dato, panel1.CreateGraphics(), panel1.Size, formatoNodoEncontrado);
                    txtBuscar.Clear();
                    txtBuscar.Focus();
                    panel1.Refresh();
                }
            }

        }

        // Creamos metodo para realizar recorrido en Pre-orden
        private void button1_Click(object sender, EventArgs e)
        {
            // Verificar si el árbol está vacío
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede realizar la operación.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return; // Salir del método si el árbol está vacío
            }

            // Limpiar el texto del Label antes de mostrar un nuevo recorrido
            lblRecorrido.Text = "Recorrido: ";

            // Llamamos al metodo de recorrido en preorden y lo mostramos en el Label
            miArbol.VisualizarRecorrido(panel1.CreateGraphics(), formatoNodo, miArbol.Raiz, TipoRecorridoArbol.preOr, lblRecorrido);
        }


        private void btnPost_Click(object sender, EventArgs e)
        {
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede realizar la operación.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            else
            {
                // Limpiar el texto del Label antes de mostrar un nuevo recorrido
                lblRecorrido.Text = "Recorrido: ";

                // Llamar al método de recorrido en postorden y mostrar en el Label
                miArbol.VisualizarRecorrido(panel1.CreateGraphics(), formatoNodo, miArbol.Raiz, TipoRecorridoArbol.postOr, lblRecorrido);
            }

        }


        private void btnEn_Click(object sender, EventArgs e)
        {
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede realizar la operación.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            else
            {
                // Limpiar el texto del Label antes de mostrar un nuevo recorrido
                lblRecorrido.Text = "Recorrido: ";

                // Llamar al método de recorrido en inorden y mostrar en el Label
                miArbol.VisualizarRecorrido(panel1.CreateGraphics(), formatoNodo, miArbol.Raiz, TipoRecorridoArbol.inOr, lblRecorrido);
            }

        }

        private void lblRecorrido_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnAltura_Click(object sender, EventArgs e)
        {
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede realizar la operación.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                int altura = miArbol.ObtenerAltura(miArbol.Raiz);
                lblAltura.Text = altura.ToString(); // Actualiza el label con la altura
            }
        }

        private void btnSuma_Click(object sender, EventArgs e)
        {
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede realizar la operación.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                int suma = miArbol.ObtenerSuma(miArbol.Raiz);
                lblSuma.Text = suma.ToString(); // Actualiza el label con la suma
            }
        }

        private void btnCantidad_Click(object sender, EventArgs e)
        {
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede realizar la operación.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                int cantidadNodos = miArbol.ContarNodos(miArbol.Raiz);
                lblCantidad.Text = cantidadNodos.ToString(); // Actualiza el label con la cantidad de nodos
            }
        }

        private void btnCargar_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialogoAbrir = new OpenFileDialog();
            dialogoAbrir.Filter = "Archivos de texto (*.txt)|*.txt";

            if (dialogoAbrir.ShowDialog() == DialogResult.OK)
            {
                miArbol = new ArbolBinario(null);  // Reiniciar el árbol
                miArbol.CargarArbolBalanceadoDesdeArchivo(dialogoAbrir.FileName, panel1);  // Cargar el árbol balanceado y pasar el panel

   
                MessageBox.Show("Árbol cargado correctamente y balanceado.", "Cargado", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            if (miArbol.Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede guardar.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                // Usamos un dialogo de guardar para elegir la ubicación del archivo
                SaveFileDialog dialogoGuardar = new SaveFileDialog();
                dialogoGuardar.Filter = "Archivos de texto (*.txt)|*.txt";

                if (dialogoGuardar.ShowDialog() == DialogResult.OK)
                {
                    // Guardamos el árbol en el archivo, barajando los valores antes de escribirlos
                    miArbol.GuardarArbolEnArchivo(miArbol.Raiz, dialogoGuardar.FileName);
                    MessageBox.Show("Árbol guardado correctamente.", "Guardado", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
        }
    }
}
