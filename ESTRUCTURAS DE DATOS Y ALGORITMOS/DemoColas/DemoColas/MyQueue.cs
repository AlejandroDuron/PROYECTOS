using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoColas
{
     class MyQueue<T>
    {
        private Node<T> first;
        private Node<T> last;

        public MyQueue() { 
            this.first = this.last= null;
            
        }

        public bool IsEmpty()
        {
            return first == null;
        }

    

        //Agrega un nuevo nodo al final de la lista
        public void Add(T value)
        {
            Node<T> aux=new Node<T>(value);
            if (IsEmpty()) 
            {
                first = last = aux;
                    return;
            }
            //Si la lista no esta vacia
            last.Next = aux;
            last = aux;
        }

  

        
        // devuelve el indice de la primera ocurrencia de value en la lista
        public int Find(int value)
        {
            if (IsEmpty())
            {
                return -1;
            }
            Node<T> current = first;
            int index = 0;
            while (true)
            {
                if (current.Data.Equals(value)) return index;
                current = current.Next;
                index++;
                if (current == null) break;//Cuando ya no hayan mas nodos
            }
            return -1;
        }

        public int Length()
        {
            if (IsEmpty()) return 0;
            int counter = 0;
            Node<T> current = first;
            while (true)
            {
                counter++;
                current = current.Next;
                if (current == null) break;
            }
            return counter;
        }

        public void DeleteFirst()
        {
            if (IsEmpty()) return;
            Node<T> aux = first;
            first=first.Next;
            aux.Next = null;
            
        }



        public void Show()
        {
            if (IsEmpty())
            {
                Console.WriteLine("La lista esta vacia");
                return;
            }
            Node<T> current = first;
            Console.WriteLine("elementos de la cola: ");
            while (true)
            {
                Console.Write(current.Data + ">>");
                current = current.Next;
                if(current==null) break;//Cuando ya no hayan mas nodos
            }
        }
    }
}
