using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase05_poo
{
    public class AlumnoClase6
    {
        // ATRIBUTOS DE LA CLASE
        private string nombre;
        private string apellido;
        private int dni;
        private int nota = 0;

        //--------------//
        // CONSTRUCTOR //
        //--------------//
        public AlumnoClase6(string nombre, string apellido, int dni)
        {
            this.nombre = nombre; 
            this.apellido = apellido;
            this.dni = dni;
            this.nota = nota;
        }

        public string MostrarInfoAlumno()
        {
            string info = $"Los datos del alumno son: \n{nombre}, \n{apellido}, \n{dni}, \n{nota}";
            return info;
        }
        public void Estudiar()
        {
            Console.WriteLine("Estoy estudiando");
        }

        public int RendirExamen()
        {
            Random r = new Random();
            this.nota = r.Next(1, 10);

            return this.nota;
        }
    }
}
