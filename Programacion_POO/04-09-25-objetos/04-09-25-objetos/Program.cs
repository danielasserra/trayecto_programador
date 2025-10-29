namespace _04_09_25_objetos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Instanciar objeto
            // Crear objeto en memoria
            // Usando operador new (crea espacio fisico en memoria para crear objeto de clase Alumno)
            Alumno miAlumno = new Alumno();
            // Alumno() es el constructor de la clase

            //Console.WriteLine(miAlumno); // Si pongo un objeto en el ConsoleWriteLine me dice qué tipo de objeto es (clase Alumno)

            miAlumno.nombre = "Juan";
            miAlumno.apellido = "Ruiz";
            miAlumno.dni = 2222222;

            miAlumno.Estudiar();

            miAlumno.nota = miAlumno.RendirExamen();

            Console.WriteLine($"La nota de {miAlumno.nombre} es {miAlumno.nota}");
            

        }
    }
}
