using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace DemoPila
{
    internal class Libro
    {
        private string nombre;

        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        private string autor;

        public string Autor
        {
            get { return autor; }
            set { autor = value; }
        }

        private int paginas;

        public int Paginas
        {
            get { return paginas; }
            set { paginas = value; }
        }


        public override string ToString()
        {
            return $"'{Nombre}' por {Autor} ({Paginas} páginas)";
        }

        public Libro(string nombre, string autor, int paginas)
        {
            this.nombre = nombre;
            this.autor = autor; 
            this.paginas = paginas; 
        }


    }
}
