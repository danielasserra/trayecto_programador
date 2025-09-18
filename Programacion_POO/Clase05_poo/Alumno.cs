using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase05_poo
{
    public class Alumno
    {
        // ATRIBUTOS DE LA CLASE
        public string nombre;
        public string apellido;
        public int dni;
        public float nota;

        public void Estudiar()
        {
            Console.WriteLine("Estoy estudiando");
        }

        public int RendirExamen()
        {
            Random r = new Random();
            int nota;
            nota = r.Next(1, 10);

            return nota;
        }
    }
}
