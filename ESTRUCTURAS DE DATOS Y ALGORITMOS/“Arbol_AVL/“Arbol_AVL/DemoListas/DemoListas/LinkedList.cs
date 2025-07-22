using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoListas
{
    internal class LinkedList
    {
        private Node first;
        private Node last;

        public LinkedList()
        {
            this.first = this.last = null;

        }

        public bool IsEmpty()
        {
            return first == null;
        }

        public int Find(int index)
        {
            if (IsEmpty())
            {
                return -1;
            }


        }
    }
}
