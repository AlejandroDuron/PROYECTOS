using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _Arbol_AVL
{
    class NodoAVL
    {
        public int Valor {  get; set; }
        public int Altura { get; set; }
        public NodoAVL Izquierdo { get; set; }
        public NodoAVL Derecho { get; set; }

        // Propiedad para almacenar la ultima rotacion realizada
        public static string UltimaRotacion { get; set; } = "";

        public NodoAVL(int valor)
        {
            Valor = valor;
            Altura = 1;
        }

        //Búsqueda recursiva
        public NodoAVL Buscar(int valor, NodoAVL nodo)
        {
            if (nodo == null || nodo.Valor == valor) return nodo;
            return valor < nodo.Valor ? Buscar(valor, nodo.Izquierdo) : Buscar(valor, nodo.Derecho); 
        }

        // Método recursivo de eliminación con balanceo
        public NodoAVL Eliminar(int valor, NodoAVL nodo)
        {
            if (nodo == null) return null;

            if (valor < nodo.Valor)
                nodo.Izquierdo = Eliminar(valor, nodo.Izquierdo);
            else if (valor > nodo.Valor)
                nodo.Derecho = Eliminar(valor, nodo.Derecho);
            else
            {
                // Nodo con un solo hijo o sin hijos
                if (nodo.Izquierdo == null)
                    return nodo.Derecho;
                if (nodo.Derecho == null)
                    return nodo.Izquierdo;

                // Nodo con dos hijos: se reemplaza por el hijo más profundo
                if (ObtenerAltura(nodo.Izquierdo) > ObtenerAltura(nodo.Derecho))
                {
                    // Reemplazar por el mayor de los menores
                    NodoAVL sucesor = ObtenerMayor(nodo.Izquierdo);
                    nodo.Valor = sucesor.Valor;
                    nodo.Izquierdo = Eliminar(sucesor.Valor, nodo.Izquierdo);
                }
                else
                {
                    // Reemplazar por el menor de los mayores
                    NodoAVL sucesor = ObtenerMenor(nodo.Derecho);
                    nodo.Valor = sucesor.Valor;
                    nodo.Derecho = Eliminar(sucesor.Valor, nodo.Derecho);
                }
            }

            return Balancear(nodo);
        }


        public int ObtenerAltura(NodoAVL nodo)
        {
            return nodo != null ? nodo.Altura : 0;
        }

        public void ActualizarAltura(NodoAVL nodo)
        {
            nodo.Altura = 1 + Math.Max(ObtenerAltura(nodo.Izquierdo), ObtenerAltura(nodo.Derecho));
                
        }

        public int ObtenerFactorEquilibrio(NodoAVL nodo)
        {
            return ObtenerAltura(nodo.Derecho) - ObtenerAltura(nodo.Izquierdo);
        }

        public NodoAVL Balancear(NodoAVL nodo)
        {
            ActualizarAltura(nodo);
            int factorEquilibrio = ObtenerFactorEquilibrio(nodo);

            if (factorEquilibrio < -1)
            {
                if (ObtenerFactorEquilibrio(nodo.Izquierdo) > 0)
                    return RotacionID(nodo);
                return RotacionII(nodo);
            }


            if (factorEquilibrio > 1)
            {
                if (ObtenerFactorEquilibrio(nodo.Derecho) > 0)
                    return RotacionDI(nodo);
                return RotacionDD(nodo);
            }

            return nodo;
        }

        private NodoAVL RotacionDD(NodoAVL n)
        {
            NodoAVL.UltimaRotacion = "Derecha-Derecha (DD)";
            NodoAVL n1 = n.Derecho;
            n.Derecho = n1.Izquierdo;
            n1.Izquierdo = n;
            ActualizarAltura(n);
            ActualizarAltura(n1);
            return n1;
        }

        private NodoAVL ObtenerMayor(NodoAVL nodo)
        {
            while (nodo.Derecho != null)
                nodo = nodo.Derecho;
            return nodo;
        }

        private NodoAVL ObtenerMenor(NodoAVL nodo)
        {
            while (nodo.Izquierdo != null)
                nodo = nodo.Izquierdo;
            return nodo;
        }

        private NodoAVL RotacionID(NodoAVL n)
        {
            NodoAVL.UltimaRotacion = "Izquierda-Derecha (ID)";
            n.Izquierdo = RotacionDD(n.Izquierdo);
            return RotacionII(n);
        }

        private NodoAVL RotacionDI(NodoAVL n)
        {
            NodoAVL.UltimaRotacion = "Derecha-Izquierda (DI)";
            n.Derecho = RotacionII(n.Derecho);
            return RotacionDD(n);
        }

        private NodoAVL RotacionII(NodoAVL n)
        {
            NodoAVL.UltimaRotacion = "Izquierda-Izquierda (II)";
            NodoAVL n1 = n.Izquierdo;
            n.Izquierdo = n1.Derecho;
            n1.Derecho = n;
            ActualizarAltura(n);
            ActualizarAltura(n1);
            return n1;
        }


        // Método recursivo de insercion con balanceo

        public NodoAVL Insertar(int valor, NodoAVL nodo)
        {
            if (nodo == null)
                return new NodoAVL(valor);
            if (valor < nodo.Valor)
                nodo.Izquierdo = Insertar(valor, nodo.Izquierdo);
            else if (valor > nodo.Valor)
                nodo.Derecho = Insertar(valor, nodo.Derecho);
            else
                return nodo; // No se permiten duplicados

            return Balancear(nodo); // Se balancea el árbol si es necesario
        }

        /************  FUNCIONES PARA DIBUJAR EL ÁRBOL ************/

        private const int RADIO = 30;
        private const int DISTANCIAH = 40;
        private const int DISTANCIAV = 10;

        private int CoordenadaX;
        private int CoordenadaY;

        // Encuentra la posición en donde debe crearse el nodo.
        public void PosicionNodo(ref int xmin, int ymin)
        {
            int aux1, aux2;

            CoordenadaY = (int)(ymin + RADIO / 2);

            // Obtiene la posición del Sub-Árbol izquierdo.
            if (Izquierdo != null)
            {
                Izquierdo.PosicionNodo(ref xmin, ymin + RADIO + DISTANCIAV);
            }
            if ((Izquierdo != null) && (Derecho != null))
            {
                xmin += DISTANCIAH;
            }

            // Si existe el nodo derecho e izquierdo deja un espacio entre ellos.
            if (Derecho != null)
            {
                Derecho.PosicionNodo(ref xmin, ymin + RADIO + DISTANCIAV);
            }

            // Posición de nodos derecho e izquierdo.
            if (Izquierdo != null)
            {
                if (Derecho != null)
                {
                    // Centro entre los nodos.
                    CoordenadaX = (int)((Izquierdo.CoordenadaX + Derecho.CoordenadaX) / 2);
                }
                else
                {
                    // No hay nodo derecho. Centrar al nodo izquierdo.
                    aux1 = Izquierdo.CoordenadaX;
                    Izquierdo.CoordenadaX = CoordenadaX - 40;
                    CoordenadaX = aux1;
                }
            }
            else if (Derecho != null)
            {
                aux2 = Derecho.CoordenadaX;
                // No hay nodo izquierdo. Centrar al nodo derecho.
                Derecho.CoordenadaX = CoordenadaX + 40;
                CoordenadaX = aux2;
            }
            else
            {
                // Nodo hoja
                CoordenadaX = (int)(xmin + RADIO / 2);
                xmin += RADIO;
            }
        }

        // Dibuja las ramas de los nodos izquierdo y derecho
        public void DibujarRamas(Graphics grafo, Pen Lapiz)
        {
            if (Izquierdo != null)
            {
                grafo.DrawLine(Lapiz, CoordenadaX, CoordenadaY, Izquierdo.CoordenadaX, Izquierdo.CoordenadaY);
                Izquierdo.DibujarRamas(grafo, Lapiz);
            }
            if (Derecho != null)
            {
                grafo.DrawLine(Lapiz, CoordenadaX, CoordenadaY, Derecho.CoordenadaX, Derecho.CoordenadaY);
                Derecho.DibujarRamas(grafo, Lapiz);
            }
        }

        // Dibuja el nodo en la posición especificada.
        public void DibujarNodo(Graphics grafo, Font fuente, Brush Relleno, Brush RellenoFuente, Pen Lapiz, int dato, Brush encuentro)
        {
            // Dibuja el contorno del nodo.
            Rectangle rect = new Rectangle(
                (int)(CoordenadaX - RADIO / 2),
                (int)(CoordenadaY - RADIO / 2),
                RADIO, RADIO);

            if (Valor == dato)
            {
                grafo.FillEllipse(encuentro, rect);
            }
            else
            {
                grafo.FillEllipse(Relleno, rect);
            }

            grafo.DrawEllipse(Lapiz, rect);

            // Dibuja el valor del nodo.
            StringFormat formato = new StringFormat();

            formato.Alignment = StringAlignment.Center;
            formato.LineAlignment = StringAlignment.Center;
            grafo.DrawString(ObtenerFactorEquilibrio(this).ToString(), fuente, Brushes.Black,
                CoordenadaX, CoordenadaY - 20, formato);
            grafo.DrawString(Valor.ToString(), fuente, Brushes.Black, CoordenadaX, CoordenadaY, formato);

            // Dibuja los nodos hijos derecho e izquierdo.
            if (Izquierdo != null)
            {
                Izquierdo.DibujarNodo(grafo, fuente, Brushes.YellowGreen, RellenoFuente, Lapiz, dato, encuentro);
            }

            if (Derecho != null)
            {
                Derecho.DibujarNodo(grafo, fuente, Brushes.Yellow, RellenoFuente, Lapiz, dato, encuentro);
            }
        }

        public void Colorear(Graphics grafo, Font fuente, Brush relleno, Brush rellenoFuente, Pen lapiz)
        {
            Rectangle rect = new Rectangle((int)(CoordenadaX - RADIO / 2), (int)(CoordenadaY - RADIO / 2), RADIO, RADIO);

            //
            StringFormat formato = new StringFormat();

            formato.Alignment = StringAlignment.Center;
            formato.LineAlignment = StringAlignment.Center;

            grafo.DrawEllipse(lapiz, rect);
            grafo.FillEllipse(Brushes.PaleVioletRed, rect);
            grafo.DrawString(Valor.ToString(), fuente, Brushes.Black, CoordenadaX, CoordenadaY, formato);
        }

        // recorridos

        public void RecorridoInOrden(NodoAVL nodo, List<int> recorrido)
        {
            if (nodo != null)
            {
                RecorridoInOrden(nodo.Izquierdo, recorrido);
                recorrido.Add(nodo.Valor);
                RecorridoInOrden(nodo.Derecho, recorrido);
            }
        }

        public void RecorridoPreOrden(NodoAVL nodo, List<int> recorrido)
        {
            if (nodo != null)
            {
                recorrido.Add(nodo.Valor);
                RecorridoPreOrden(nodo.Izquierdo, recorrido);
                RecorridoPreOrden(nodo.Derecho, recorrido);
            }
        }

        public void RecorridoPostOrden(NodoAVL nodo, List<int> recorrido)
        {
            if (nodo != null)
            {
                RecorridoPostOrden(nodo.Izquierdo, recorrido);
                RecorridoPostOrden(nodo.Derecho, recorrido);
                recorrido.Add(nodo.Valor);
            }
        }
    }
}

