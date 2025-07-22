using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoArbolBinario1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int valor = 0;
            int opcion = 0;
            BinarySearchTree abb = new BinarySearchTree();
   
            while (true)
            {
                Console.WriteLine("*********** DEMO COLAS*************");
                Console.WriteLine("* 1- Insertar elemento            *");
                Console.WriteLine("* 2- Buscar elemento              *");
                Console.WriteLine("* 3- Eliminar elemento            *");
                Console.WriteLine("* 4- Recorrer en anchura          *");
                Console.WriteLine("* 5- Recorrer en pre-orden        *");
                Console.WriteLine("* 6- Salir                        *");
                Console.WriteLine("***********************************");
                Console.WriteLine("Selecciona una opcion: ");
                opcion = int.Parse(Console.ReadLine());
                switch (opcion)
                {
                    case 1:

                        Console.WriteLine("Ingrese el elemento que desea insertar:");
                        valor = int.Parse(Console.ReadLine());
                        abb.Insert(valor, abb.Root);
                        break;
                    case 2:
                        Console.WriteLine("Ingrese el elemento que desea buscar:");
                        valor = int.Parse(Console.ReadLine());
                        if (abb.Search(valor, abb.Root))
                        {
                            Console.WriteLine("El elemento {0} se encuentra en el arbol", valor);
                        }
                        else
                        {
                            Console.WriteLine("El elemento {0} no se encuentra en el arbol", valor);
                        }
                        break;

                    case 5: 
                        if(abb.Root == null)
                        {
                            Console.WriteLine("El arbol esta vacio");
                        }
                        else
                        {
                            Console.WriteLine("Recorrido en preorden: ");
                            abb.PreOrdenTransversal(abb.Root);
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
