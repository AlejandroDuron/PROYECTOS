using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoPilas
{
     class Node <T>
    {

		private T data;
		public T Data
		{
			get { return data; }
			set { data = value; }
		}

		private Node<T> next;
		public Node<T> Next
		{
			get { return next; }
			set { next = value; }
		}

		public Node(T data)
		{
			this.data = data;
			this.next = null;
		}

	}
}
