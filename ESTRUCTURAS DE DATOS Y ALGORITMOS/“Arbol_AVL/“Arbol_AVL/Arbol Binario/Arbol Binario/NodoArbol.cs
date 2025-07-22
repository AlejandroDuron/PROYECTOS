using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;

namespace Arbol_Binario
{
    public enum TipoRecorridoArbol
    {
        postOr,
        inOr,
        preOr
    }

    public struct FormatoNodo
    {
        public Font fuente;
        public Brush relleno;
        public Brush rellenofuente;
        public Pen lapiz;
        public Brush encuentro;
    }
    public class NodoArbol
    {
        public int Info { get; set; }
        public NodoArbol Izquierdo { get; set; }
        public NodoArbol Derecho { get; set; }
        public int Altura { get; set; }
        public int Nivel { get; set; }
        public int CoordenadaX { get; set; }
        public int CoordenadaY { get; set; }

        // Variables constantes:
        private const int Radio = 30;
        private const int DistanciaH = 80;
        private const int DistanciaV = 10;

        public NodoArbol(int nueva_info, NodoArbol izquierdo, NodoArbol derecho)
        {
            this.Info = nueva_info;
            this.Izquierdo = izquierdo;
            this.Derecho = derecho;
            this.Altura = 0;
        }

        public NodoArbol Buscar(int x, NodoArbol nodo)
        {
            // Si el nodo es null, significa que no encontramos el valor
            if (nodo == null)
            {
                return null;
            }

            // Si el valor es igual al nodo actual, hemos encontrado el nodo
            if (x == nodo.Info)
            {
                return nodo;
            }
            // Si el valor es menor que el nodo actual, buscamos en el subárbol izquierdo
            else if (x < nodo.Info)
            {
                return Buscar(x, nodo.Izquierdo);
            }
            // Si el valor es mayor que el nodo actual, buscamos en el subárbol derecho
            else
            {
                return Buscar(x, nodo.Derecho);
            }
        }
        public NodoArbol Insertar(int x, NodoArbol t, int nivel)
        {
            if (t == null)
            {
                t = new NodoArbol(x, null, null);
                t.Nivel = nivel;
            }
            else if (x < t.Info)
            {
                // Insertar en subárbol izquierdo
                nivel++;
                t.Izquierdo = Insertar(x, t.Izquierdo, nivel);
            }
            else if (x > t.Info)
            {
                // Insertar en subárbol derecho
                nivel++;
                t.Derecho = Insertar(x, t.Derecho, nivel);
            }
            else
            {
                // El valor ya existe en el árbol
                MessageBox.Show("Dato ya existe en el Árbol", "Error de Ingreso");

                // Actualizar altura al volver de la recursión
                t.Altura = 1 + Math.Max(getAltura(t.Izquierdo), getAltura(t.Derecho));
                return t;
            }
            return t;
        }

        public NodoArbol Eliminar(int x, NodoArbol t)
        {
            if (t == null)
            {
                MessageBox.Show("Nodo NO existente en el Árbol", "Error de eliminación");
                return null;
            }

            if (x < t.Info)
            {
                // Buscar en el subárbol izquierdo y actualizar la referencia
                t.Izquierdo = Eliminar(x, t.Izquierdo);
            }
            else if (x > t.Info)
            {
                // Buscar en el subárbol derecho y actualizar la referencia
                t.Derecho = Eliminar(x, t.Derecho);
            }
            else
            {
                // Nodo encontrado: caso de eliminación
                // Caso 1: nodo sin hijo derecho, se reemplaza por hijo izquierdo
                if (t.Derecho == null)
                {
                    return t.Izquierdo;
                }
                // Caso 2: nodo sin hijo izquierdo, se reemplaza por hijo derecho
                else if (t.Izquierdo == null)
                {
                    return t.Derecho;
                }
                else
                {
                    // Caso 3: nodo con dos hijos
                    // Elegimos el sucesor o predecesor según la altura de los subárboles
                    if (getAltura(t.Izquierdo) > getAltura(t.Derecho))
                    {
                        // Buscar el nodo máximo en el subárbol izquierdo (predecesor)
                        NodoArbol padreAux = null;
                        NodoArbol aux = t.Izquierdo;
                        while (aux.Derecho != null)
                        {
                            padreAux = aux;
                            aux = aux.Derecho;
                        }

                        // Reemplazar valor del nodo a eliminar con predecesor
                        t.Info = aux.Info;

                        // Eliminar el nodo predecesor y actualizar su padre
                        if (padreAux != null)
                            padreAux.Derecho = aux.Izquierdo;
                        else
                            t.Izquierdo = aux.Izquierdo;
                    }
                    else
                    {
                        // Buscar el nodo mínimo en el subárbol derecho (sucesor)
                        NodoArbol padreAux = null;
                        NodoArbol aux = t.Derecho;
                        while (aux.Izquierdo != null)
                        {
                            padreAux = aux;
                            aux = aux.Izquierdo;
                        }

                        // Reemplazar valor del nodo a eliminar con sucesor
                        t.Info = aux.Info;

                        // Eliminar el nodo sucesor y actualizar su padre
                        if (padreAux != null)
                            padreAux.Izquierdo = aux.Derecho;
                        else
                            t.Derecho = aux.Derecho;
                    }
                }
            }

            // Actualizar altura después de la posible modificación del subárbol
            t.Altura = 1 + Math.Max(getAltura(t.Izquierdo), getAltura(t.Derecho)) ;

            // Retornar el nodo (posiblemente modificado) para reasignar en el padre
            return t;
        }

        public void PosicionNodo(ref int x, int y)
        {
            const int distanciaHorizontal = 40;  // Espacio horizontal entre nodos
            const int distanciaVertical = 50;    // Espacio vertical entre niveles

            // Primero se posicionan los nodos del subárbol izquierdo
            if (Izquierdo != null)
            {
                Izquierdo.PosicionNodo(ref x, y + distanciaVertical);  // Se aumenta la altura para el subárbol izquierdo
            }

            // Asignar coordenadas al nodo actual
            this.CoordenadaX = x;
            this.CoordenadaY = y;

            // Avanzamos la coordenada X para el siguiente nodo
            x += distanciaHorizontal;

            // Finalmente, se posicionan los nodos del subárbol derecho
            if (Derecho != null)
            {
                Derecho.PosicionNodo(ref x, y + distanciaVertical);  // Se aumenta la altura para el subárbol derecho
            }
        }

        public void DibujarRamas(Graphics grafo, FormatoNodo formatoNodo)
        {
            if (Izquierdo != null)
            {
                // Línea desde borde inferior del nodo padre al borde superior del hijo izquierdo
                grafo.DrawLine(formatoNodo.lapiz,
                    CoordenadaX, CoordenadaY,
                    Izquierdo.CoordenadaX, Izquierdo.CoordenadaY);
                Izquierdo.DibujarRamas(grafo, formatoNodo);
            }
            if (Derecho != null)
            {
                // Línea desde borde inferior del nodo padre al borde superior del hijo derecho
                grafo.DrawLine(formatoNodo.lapiz,
                    CoordenadaX, CoordenadaY,
                    Derecho.CoordenadaX, Derecho.CoordenadaY);
                Derecho.DibujarRamas(grafo, formatoNodo);
            }
        }

        public void DibujarNodo(Graphics grafo, FormatoNodo formatoNodo)
        {
            // Rectángulo que enmarca el nodo circular (elipse)
            // Sintaxis: Rectangle(int x, int y, int width, int height)
            Rectangle rect = new Rectangle
                ((int)(CoordenadaX - Radio / 2),
                (int)(CoordenadaY - Radio / 2),
                Radio, Radio);

            // Rellenar con color de fondo (relleno)
            grafo.FillEllipse(formatoNodo.relleno, rect);

            // Dibujar borde del nodo
            grafo.DrawEllipse(formatoNodo.lapiz, rect);

            // Preparar formato para texto centrado
            StringFormat formato = new StringFormat
            {
                Alignment = StringAlignment.Center,
                LineAlignment = StringAlignment.Center
            };

            // Dibujar texto con el contenido del nodo centrado
            grafo.DrawString(Info.ToString(), formatoNodo.fuente,
                formatoNodo.rellenofuente, CoordenadaX, CoordenadaY, formato);

            // Dibujar nodos hijos (recursivo)
            if (Izquierdo != null)
                Izquierdo.DibujarNodo(grafo, formatoNodo);

            if (Derecho != null)
                Derecho.DibujarNodo(grafo, formatoNodo);
        }

        public void Colorear(Graphics grafo, FormatoNodo formatoNodo)
        {
            Rectangle rect = new Rectangle(
                (int)(CoordenadaX - Radio / 2),
                (int)(CoordenadaY - Radio / 2),
                Radio, Radio);

            // Rellenar con color para resaltar (por ejemplo al seleccionar)
            grafo.FillEllipse(formatoNodo.relleno, rect);

            // Dibujar borde
            grafo.DrawEllipse(formatoNodo.lapiz, rect);

            // Formato texto centrado
            StringFormat formato = new StringFormat
            {
                Alignment = StringAlignment.Center,
                LineAlignment = StringAlignment.Center
            };

            // Dibujar texto centrado
            grafo.DrawString(Info.ToString(), formatoNodo.fuente,
                formatoNodo.rellenofuente, CoordenadaX, CoordenadaY, formato);
        }



        private static int getAltura(NodoArbol t)
            {
                return t == null ? -1 : t.Altura;
            }

    }
}
