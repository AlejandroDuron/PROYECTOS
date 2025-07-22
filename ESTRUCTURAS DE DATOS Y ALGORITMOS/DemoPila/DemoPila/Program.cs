using DemoPilas;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Text;
using System.Threading.Tasks;

namespace DemoPila
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int opcion = 0;
            MyStack<Libro> myStack = new MyStack<Libro>();

            while (true)
            {
                Console.WriteLine("*********** DEMO PILAS*************");
                Console.WriteLine("* 1- Agregar libro                *");
                Console.WriteLine("* 2- Mostrar pila                 *");
                Console.WriteLine("* 3- Retirar libro                *");
                Console.WriteLine("* 4- Mostrar ult. libro           *");
                Console.WriteLine("* 5- Buscar elemento              *");
                Console.WriteLine("* 6- Salir                        *");
                Console.WriteLine("***********************************");
                Console.WriteLine("Selecciona una opcion: ");
                opcion = int.Parse(Console.ReadLine());
                switch (opcion)
                {
                    case 1:
                        string nombre = "";
                        string autor = "";
                        int paginas = 0;

                        Console.WriteLine("Ingrese el nombre del libro que desea insertar:");
                        nombre = Console.ReadLine();

                        Console.WriteLine("Ingrese el autor del libro que desea insertar:");
                        autor = Console.ReadLine();

                        Console.WriteLine("Ingrese el numero de paginas del libro que desea insertar:");
                        paginas = int.Parse(Console.ReadLine());

                        Libro nuevoLibro = new Libro(nombre, autor, paginas);
                        myStack.Push(nuevoLibro);

                        Console.WriteLine("El libro {0} fue agregado exitosamente", nuevoLibro.ToString());
                        break;
                    case 2:
                        myStack.Show();
                        break;
                    case 3:
                        Console.WriteLine("Elemento desenpilado: " + myStack.Pop().Data);
                        break;
                    case 4:
                        Console.WriteLine("Ultimo libro agregado: " + myStack.Peek());
                        break;
                    case 5:
                        Libro aux = null;
                        int indice = 0;

                        Console.WriteLine("Ingresa el nombre del libro que quieres buscar: ");

                        aux.Nombre = Console.ReadLine();
                        indice = myStack.Find(aux);

                        if (indice == -1)
                        {
                            Console.WriteLine("El elemento {0} no se encuentra en la cola", aux);
                        }
                        else
                        {
                            Console.WriteLine("El elemento {0} se encuentra en la posicion {1} de la cola", aux.Nombre, indice);
                        }
                        break;

                    case 6:
                        return;

                    default:
                        Console.WriteLine("Opcion no valida");
                        break;
                }
                Console.ReadKey();
                Console.Clear();
            }
        }
    }
}
