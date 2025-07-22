using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _Arbol_AVL
{
    internal class ArbolAVL
    {
        public NodoAVL Raiz { get; set; }
        public ArbolAVL(NodoAVL RaizNueva)
        {
            Raiz = RaizNueva;
        }
        public void Insertar(int dato)
        {
            if (Raiz == null)
                Raiz = new NodoAVL(dato);
            else
                Raiz = Raiz.Insertar(dato, Raiz);
        }
        public void Eliminar(int dato)
        {
            if (Raiz == null)
                Raiz = new NodoAVL(dato);
            else
                Raiz.Eliminar(dato, Raiz);
        }

        public void Colorear(Graphics grafo, Font fuente, Brush Relleno, Brush RellenoFuente, Pen
        Lapiz, NodoAVL Raiz, bool post, bool inor, bool preor)
        {
            Brush entorno = Brushes.Red;
            if (inor == true)
            {
                if (Raiz != null)
                {
                    Colorear(grafo, fuente, Brushes.Blue, RellenoFuente, Lapiz, Raiz.Izquierdo,
                    post, inor, preor);
                    Raiz.Colorear(grafo, fuente, entorno, RellenoFuente, Lapiz);
                    Thread.Sleep(500);
                    Raiz.Colorear(grafo, fuente, Relleno, RellenoFuente, Lapiz);
                    Colorear(grafo, fuente, Relleno, RellenoFuente, Lapiz, Raiz.Derecho, post, inor,
                    preor);
                }
            }
            else if (preor == true)
            {
                if (Raiz != null)
                {
                    Raiz.Colorear(grafo, fuente, Brushes.Yellow, Brushes.Blue, Pens.Black);
                    Thread.Sleep(500);
                    Raiz.Colorear(grafo, fuente, Brushes.White, Brushes.Black, Pens.Black);
                    Colorear(grafo, fuente, Brushes.Blue, RellenoFuente, Lapiz, Raiz.Izquierdo,
                   post, inor, preor);
                    Colorear(grafo, fuente, Relleno, RellenoFuente, Lapiz, Raiz.Derecho, post, inor,
                   preor);
                }
            }
            else if (post == true)
            {
                if (Raiz != null)
                {
                    Colorear(grafo, fuente, Relleno, RellenoFuente, Lapiz, Raiz.Izquierdo, post,
                   inor, preor);
                    Colorear(grafo, fuente, Relleno, RellenoFuente, Lapiz, Raiz.Derecho, post, inor,
                   preor);
                    Raiz.Colorear(grafo, fuente, entorno, RellenoFuente, Lapiz);
                    Thread.Sleep(500);
                    Raiz.Colorear(grafo, fuente, Relleno, RellenoFuente, Lapiz);
                }
            }
        }

        public void ColorearBusqueda(Graphics grafo, Font fuente, Brush Relleno, Brush
        RellenoFuente, Pen Lapiz, NodoAVL Raiz, int busqueda)
        {
            Brush entorno = Brushes.Red;
            if (Raiz != null)
            {
                Raiz.Colorear(grafo, fuente, entorno, RellenoFuente, Lapiz);
                if (busqueda < Raiz.Valor)
                {
                    Thread.Sleep(500);
                    Raiz.Colorear(grafo, fuente, entorno, Brushes.Blue, Lapiz);
                    ColorearBusqueda(grafo, fuente, Relleno, RellenoFuente, Lapiz, Raiz.Izquierdo,
                   busqueda);
                }
                else if (busqueda > Raiz.Valor)
                {
                    Thread.Sleep(500);
                    Raiz.Colorear(grafo, fuente, entorno, RellenoFuente, Lapiz);
                    ColorearBusqueda(grafo, fuente, Relleno, RellenoFuente, Lapiz, Raiz.Derecho,
                   busqueda);
                }
                else
                {
                    Raiz.Colorear(grafo, fuente, entorno, RellenoFuente, Lapiz);
                    Thread.Sleep(500);
                }
            }
        }

        public void DibujarArbol(Graphics grafo, Font fuente, Brush Relleno, Brush RellenoFuente,
        Pen Lapiz, int dato, Brush encuentro)
        {
            int x = 100;
            int y = 75;
            if (Raiz == null) return;
            Raiz.PosicionNodo(ref x, y);
            Raiz.DibujarRamas(grafo, Lapiz);
            Raiz.DibujarNodo(grafo, fuente, Relleno, RellenoFuente, Lapiz, dato, encuentro);
        }
        public void Buscar(int x)
        {
            if (Raiz == null)
                MessageBox.Show("Árbol AVL Vacío", "Error", MessageBoxButtons.OK);
            else
                Raiz.Buscar(x, Raiz);
        }

        // Capturar recorrido
        public string ObtenerRecorrido(string tipo)
        {
            List<int> recorrido = new List<int>();
            if (Raiz == null) return "";

            switch (tipo)
            {
                case "InOrden":
                    Raiz.RecorridoInOrden(Raiz, recorrido);
                    break;
                case "PreOrden":
                    Raiz.RecorridoPreOrden(Raiz, recorrido);
                    break;
                case "PostOrden":
                    Raiz.RecorridoPostOrden(Raiz, recorrido);
                    break;
            }

            return string.Join(", ", recorrido);
        }

    }
}

