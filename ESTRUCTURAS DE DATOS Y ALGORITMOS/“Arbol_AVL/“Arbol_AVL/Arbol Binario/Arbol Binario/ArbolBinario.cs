using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//Para utilizar a la clase MessageBox 
using System.Windows.Forms;
//usa clases del namespace para dibujar figuras 
using System.Drawing;
//accede a clases para manejo de hilos 
using System.Threading;

namespace Arbol_Binario
{
    public class ArbolBinario
    {
        public NodoArbol Raiz { get; set; }

        public ArbolBinario(NodoArbol nueva_raiz)
        {
            Raiz = nueva_raiz;
        }

        public void Insertar(int x)
        {
            if (Raiz == null)
            {
                Raiz = new NodoArbol(x, null, null);
                Raiz.Nivel = 0;
            }
            else
                Raiz = Raiz.Insertar(x, Raiz, Raiz.Nivel);
        }

        public void Eliminar(int x)
        {
            if (Raiz == null)
            {
                MessageBox.Show("El árbol está vacío. No se puede eliminar.", "Error");
                return;
            }
            Raiz = Raiz.Eliminar(x, Raiz);
        }

        public void BuscarEnArbol(int x, Graphics panelGraphics, Size areaDibujo, FormatoNodo formatoNodo)
        {
            NodoArbol nodo;
            if (Raiz != null)
            {
                nodo = Raiz.Buscar(x, Raiz);
                if (nodo != null) // encontro al nodo
                {
                    nodo.Colorear(panelGraphics, formatoNodo);
                    MessageBox.Show("Nodo " + nodo.Info.ToString() + " fue encontrado",
                        "Busqueda de nodo en Árbol", MessageBoxButtons.OK,
                        MessageBoxIcon.Exclamation);
                }
                else
                {
                    MessageBox.Show("No se encontró el nodo " + x.ToString() +
                        " en el Arbol Binario", "Busqueda de nodo en Árbol",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
        }

        public void DibujarArbol(Graphics panelGraphics, Size areaDibujo, FormatoNodo formatoNodo)
        {
            int x, y; //posicion del nodo raiz del arbol a grafica
            x = areaDibujo.Width / 4;
            y = 40;

            if (Raiz == null)
                return; //finaliza funcion, aun no hay arbol que dibujar

            Raiz.PosicionNodo(ref x, y); //Obtiene la posicion de cada nodo
            Raiz.DibujarRamas(panelGraphics, formatoNodo); //Dibuja los Enlaces entre nodos
            Raiz.DibujarNodo(panelGraphics, formatoNodo); //Dibuja todos los Nodos
        }

        public void VisualizarRecorrido(Graphics panelGraphics, FormatoNodo formatoNodo, NodoArbol Raiz, TipoRecorridoArbol tipoRecorrido, Label lblRecorrido)
        {
            FormatoNodo formatonodo2 = formatoNodo;
            formatonodo2.relleno = Brushes.Red;

            // Usamos un metodo especial para acumular los valores de los nodos
            StringBuilder recorrido = new StringBuilder();

            switch (tipoRecorrido)
            {
                case TipoRecorridoArbol.preOr:
                    if (Raiz != null)
                    {
                        // Preorden: primero el nodo raíz
                        recorrido.Append(Raiz.Info.ToString() + " "); // Acumular el valor
                        lblRecorrido.Text += Raiz.Info.ToString() + " "; // Mostrar el valor en el Label
                        Raiz.Colorear(panelGraphics, formatonodo2); // Subrayar el nodo
                        lblRecorrido.Refresh(); // Actualizar el Label en tiempo real
                        Thread.Sleep(800); 
                        VisualizarRecorrido(panelGraphics, formatoNodo, Raiz.Izquierdo, tipoRecorrido, lblRecorrido); // Recorrer subárbol izquierdo
                        VisualizarRecorrido(panelGraphics, formatoNodo, Raiz.Derecho, tipoRecorrido, lblRecorrido); // Recorrer subárbol derecho
                    }
                    break;

                case TipoRecorridoArbol.inOr:
                    if (Raiz != null)
                    {
                        VisualizarRecorrido(panelGraphics, formatoNodo, Raiz.Izquierdo, tipoRecorrido, lblRecorrido); // Recorrer subárbol izquierdo
                        recorrido.Append(Raiz.Info.ToString() + " "); // Acumular el valor
                        lblRecorrido.Text += Raiz.Info.ToString() + " "; // Mostrar el valor en el Label
                        Raiz.Colorear(panelGraphics, formatoNodo); // Subrayar el nodo
                        lblRecorrido.Refresh(); // Actualizar el Label en tiempo real
                        Thread.Sleep(800); 
                        VisualizarRecorrido(panelGraphics, formatoNodo, Raiz.Derecho, tipoRecorrido, lblRecorrido); // Recorrer subárbol derecho
                    }
                    break;

                case TipoRecorridoArbol.postOr:
                    if (Raiz != null)
                    {
                        VisualizarRecorrido(panelGraphics, formatoNodo, Raiz.Izquierdo, tipoRecorrido, lblRecorrido); // Recorrer subárbol izquierdo
                        VisualizarRecorrido(panelGraphics, formatoNodo, Raiz.Derecho, tipoRecorrido, lblRecorrido); // Recorrer subárbol derecho
                        recorrido.Append(Raiz.Info.ToString() + " "); // Acumular el valor
                        lblRecorrido.Text += Raiz.Info.ToString() + " "; // Mostrar el valor en el Label
                        Raiz.Colorear(panelGraphics, formatonodo2); // Subrayar el nodo
                        lblRecorrido.Refresh(); // Actualizar el Label en tiempo real
                        Thread.Sleep(800); 
                    }
                    break;
            }

            // Aseguramos que todos los valores del recorrido se agreguen correctamente
            if (recorrido.Length > 0)
            {
                // No agregamos nuevamente el primer valor si ya ha sido agregado
                if (!lblRecorrido.Text.Contains(recorrido.ToString()))
                {
                    lblRecorrido.Text += recorrido.ToString();
                }
            }
        }


        // Metodo para obtener la altura del árbol

        public int ObtenerAltura(NodoArbol nodo)
        {
            if (nodo == null)
            {
                return -1;  // La altura de un árbol vacio es -1
            }
            else
            {
                int alturaIzquierda = ObtenerAltura(nodo.Izquierdo);
                int alturaDerecha = ObtenerAltura(nodo.Derecho);
                return 1 + Math.Max(alturaIzquierda, alturaDerecha);
            }
        }

        // Metodo para obtener la suma de los nodos del árbol
        public int ObtenerSuma(NodoArbol nodo)
        {
            if (nodo == null)
            {
                return 0;
            }
            else
            {
                return nodo.Info + ObtenerSuma(nodo.Izquierdo) + ObtenerSuma(nodo.Derecho);
            }
        }

        // Metodo para conocer la cantidad de nodos del árbol

        public int ContarNodos(NodoArbol nodo)
        {
            if (nodo == null)
            {
                return 0;
            }
            else
            {
                return 1 + ContarNodos(nodo.Izquierdo) + ContarNodos(nodo.Derecho);
            }
        }

        // Los siguientes metodos son utilizados para exportar e importar arboles 
        public void GuardarArbolEnArchivo(NodoArbol nodo, string rutaArchivo)
        {
            // Recopilamos los valores del árbol en una lista
            List<int> valores = new List<int>();
            GuardarValoresEnLista(nodo, valores);  // Llenamos la lista

            // Ordenamos los valores para asegurarnos de que estén en orden ascendente
            valores.Sort();  // Recorrido inorden

            // Guardamos los valores ordenados en el archivo
            using (System.IO.StreamWriter archivo = new System.IO.StreamWriter(rutaArchivo, false)) // Sobrescribir archivo
            {
                foreach (int valor in valores)
                {
                    archivo.WriteLine(valor);  // Guardar cada valor en el archivo
                }
            }
        }

        // Metodo recursivo para obtener los valores del árbol
        private void GuardarValoresEnLista(NodoArbol nodo, List<int> valores)
        {
            if (nodo == null)
                return;

            // Recorrido inorden: Subárbol izquierdo, nodo actual, subárbol derecho
            GuardarValoresEnLista(nodo.Izquierdo, valores);
            valores.Add(nodo.Info);  // Agregar valor a la lista
            GuardarValoresEnLista(nodo.Derecho, valores);
        }

        // Metodo para rebalancear el arbol de una lista de valores ordenados
        public NodoArbol InsertarBalanceado(List<int> valores, int inicio, int fin)
        {
            if (inicio > fin)
                return null;

            int medio = (inicio + fin) / 2;
            int valorMedio = valores[medio];
            NodoArbol nodo = new NodoArbol(valorMedio, null, null);

            nodo.Izquierdo = InsertarBalanceado(valores, inicio, medio - 1);
            nodo.Derecho = InsertarBalanceado(valores, medio + 1, fin);

            return nodo;
        }



        public void CargarArbolBalanceadoDesdeArchivo(string rutaArchivo, Panel panel)
        {
            string[] lineas = System.IO.File.ReadAllLines(rutaArchivo);
            List<int> valores = new List<int>();

            // Convertir cada línea a un valor entero
            foreach (string linea in lineas)
            {
                int valor;
                if (int.TryParse(linea, out valor))
                {
                    valores.Add(valor);
                }
            }

            // Ordenamos los valores para garantizar que estén en orden ascendente
            valores.Sort();  // Aseguramos que los valores estén en orden ascendente

            // insertamos los valores en el arbol balanceado
            Raiz = InsertarBalanceado(valores, 0, valores.Count - 1);

            // Recalculamos las posiciones de los nodos después de cargar el árbol
            int x = panel.Width / 4;  // Coordenada X inicial de la raíz
            int y = 40;   // Coordenada Y inicial de la raíz
            Raiz.PosicionNodo(ref x, y);  // Recalcular las posiciones de todos los nodos

            // Se actualiza el panel para dibujar el árbol cargado
            panel.Refresh();  // Panel se refresca
            MessageBox.Show("Árbol cargado correctamente y balanceado.", "Cargado", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }


    }
}
