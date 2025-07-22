using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoColas
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Queue<string> cola = new Queue<string>();

            int opcion = 0;
            MyQueue<string> myQueue = new MyQueue<string>(); //Ahora el "value" sera string y no int

            while (true)
            {
                Console.WriteLine("************ DEMO COLAS **************");
                Console.WriteLine("* 1-Encolar elemento                 *");
                Console.WriteLine("* 2-Mostrar Cola                     *");
                Console.WriteLine("* 3-Desencolar elemento              *");
                Console.WriteLine("* 4-Ver primer elemento              *");
                Console.WriteLine("* 5-Buscar elemento                  *");
                Console.WriteLine("* 6-Salir                            *");
                Console.WriteLine("**************************************");
                Console.WriteLine("Selecciona una opcion:  ");
                opcion = int.Parse(Console.ReadLine());
                switch (opcion)
                {
                    case 1:
                        istringnt elemento = 0;
                        Console.WriteLine("Ingrese el elemento que desea inserar: ");
                        elemento = Console.ReadLine();
                        myQueue.Add(elemento);
                        Console.WriteLine("Elemento {0} agregado exitosamente", elemento);
                        break;

                    case 2:
                        myQueue.Show();
                        break;
                    case 3:
                        Console.WriteLine("Elemento desencolocado: " + myQueue);
                        break;
                    case 4:
                        Console.WriteLine("Primer elemento:  " + myQueue);
                        break;
                    case 5:
                        int aux = 0, indice = 0;
                        Console.WriteLine("ingresa el elemento que quieres buscar: ");
                        aux = int.Parse(Console.ReadLine());
                        indice = myQueue.Find(aux);
                        if (indice == -1)
                        {
                            Console.WriteLine("El elemento {0} no se encuentra en la cola", aux);
                        }
                        else
                        {
                            Console.WriteLine("El elemento {0} se encuentra en la posicion {1} de la cola", aux, indice);
                        }
                        break;
                    case 6:
                        return; //Se hace asi para que se salga del switch y el while






                }
            }
        }
    }
}
