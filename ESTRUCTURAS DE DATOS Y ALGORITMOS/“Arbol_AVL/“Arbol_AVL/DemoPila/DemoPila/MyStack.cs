using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoPilas
{
     class MyStack<T>
    {
        private Node<T> first;
        private Node<T> last;

        public MyStack() { 
            this.first = this.last= null;
            
        }

        public bool IsEmpty()
        {
            return first == null;
        }

        //Devuelve el nodo que se encuentra en un determinado indice
        public Node<T> FindAt(int index)
        {
            int currentIndex = 0;
            Node<T> current = first;
            while (current != null)
            {
                if (currentIndex == index) return current;
                currentIndex++;
                current = current.Next;
            }
            return null; 

        }

        //Agrega un nuevo nodo al final de la lista - no
       


        public void Push(T value)
        {
            Node<T> aux = new Node<T>(value);
            if (IsEmpty())
            {
                first = last = aux;
                return;
            }
            //Si la lista no esta vacia
            aux.Next=first;
            first = aux;
            
        }

        
        // devuelve el indice de la primera ocurrencia de value en la lista
        public int Find(T value)
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

        // Elimina el ultimo elmento agregado de la pila
        public Node<T> Pop()
        {
            if (IsEmpty()) return null;

            Node<T> aux = first;
            first=first.Next;
            aux.Next = null;

            return aux;
            
        }

        public Node<T> Peek()
        {
            return first;
        }


        public void Show()
        {
            if (IsEmpty())
            {
                Console.WriteLine("La lista esta vacia");
                return;
            }
            Node<T> current = first;
            while (true)
            {
                Console.WriteLine(current.Data);
                current = current.Next;
                if(current==null) break;//Cuando ya no hayan mas nodos
            }
        }
    }
}
