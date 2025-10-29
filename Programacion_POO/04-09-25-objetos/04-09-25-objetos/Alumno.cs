using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _04_09_25_objetos
{
    public class Alumno
    {
        public String nombre;
        public String apellido;
        public int dni;
        public float nota;

        public void Estudiar()
        {
            Console.WriteLine("Estoy estudiando");
        }

        public int RendirExamen()
        {
            Random r = new Random();
            int nota = r .Next(1, 10);

            return nota;
        }
       

       
    }
}
