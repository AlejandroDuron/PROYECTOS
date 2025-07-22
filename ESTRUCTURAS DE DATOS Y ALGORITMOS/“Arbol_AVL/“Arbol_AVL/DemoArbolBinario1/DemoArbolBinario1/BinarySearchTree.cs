using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoArbolBinario1
{
    internal class BinarySearchTree
    {
		private Node root;
		public Node Root
		{
			get { return root; }
			set { root = value; }
		}

		public BinarySearchTree()
		{
			this.root = null;
		}

		public void Insert(int value, Node root)
		{
			if (root == null) //Si el arbol esta vacio
			{
				this.root = new Node(value);
                Console.WriteLine("elemento {0} agregado exitosamente", value);
                return;
			}

			else if (root.Value == value)
			{
				Console.WriteLine("Ya se encuentra este nodo en el arbol");
				return;
			}

			else if (value < root.Value) //Si el elemento es menor que la raiz
			{
				if (root.Left == null) //Si no hay elementos a la izquierda
				{
					root.Left = new Node(value);
                    Console.WriteLine("elemento {0} agregado exitosamente", value);
                }
				else
				{
					Insert(value, root.Left);
				}
			}

			else if (value > root.Value) //Si el elemento es mayor que la raiz
			{
				if (root.Right == null) //Si no hay elementos a la derecha
				{
					root.Right = new Node(value);
					Console.WriteLine("elemento {0} agregado exitosamente", value);
				}
				else
				{
					Insert(value, root.Right);
				}
			}
        }

		public bool Search(int value, Node root)
		{
			if (root == null) //Si el arbol  actual esta vacío
			{
				return false;
			}
			if (value < root.Value) //valor menor a la raiz
			{
				// A la izquierda
				return Search(value, root.Left); // al final llamara si es falso o verdadero ya sea este vacio o haya un valor igual 
			}
            else if (value > root.Value)
            {
                // Derecha
				return Search(value, root.Right);
            }
			else //if (value == root.Value) , ¿es igual?
			{
				return true;
			}
        }


		public void PreOrdenTransversal(Node root)
		{
			if ( root != null )
			{
				Console.WriteLine(root.Value + " >> ");
				PreOrdenTransversal(root.Left);
				PreOrdenTransversal(root.Right);
			}
		}

		public void InordenTransversal(Node root) //Solo cambia el orden de la impresion
		{
			if (root != null)
			{
				InordenTransversal(root.Left);
				Console.WriteLine(root.Value + " >> ");
				InordenTransversal(root.Right);
			}
		}

        public void PostOrdenTransversal(Node root)
        {
            if (root != null)
            {
                InordenTransversal(root.Left);
                InordenTransversal(root.Right);
                Console.WriteLine(root.Value + " >> ");
                
            }
        }
    }
}
