using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoArbolBinario1
{
    internal class Node
    {
		private int data;

		public int Value
		{
			get { return data; }
			set { data = value; }
		}

		private Node left;

		public Node Left
		{
			get { return left; }
			set { left = value; }
		}

		private Node right;

		public Node Right
		{
			get { return right; }
			set { right = value; }
		}

		public Node(int value)
		{
			this.data = value;
			this.left = this.right = null;
		}




	}
}
