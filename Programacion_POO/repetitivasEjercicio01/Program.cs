namespace repetitivasEjercicio01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Pedir las 5 notas de un alumno y calcular el promedio.

            Console.WriteLine("¿Cuantas notas desea ingresar para cada alumno?");
            int cantidad = int.Parse(Console.ReadLine());

            float suma = 0;
            int cantidadNotas = cantidad;

            do
            {
                
                Console.WriteLine("Ingrese nota");
                float nota = float.Parse(Console.ReadLine());
                suma += nota;
                cantidad -= 1;

            } while (cantidad > 0);

            float promedio = suma / cantidadNotas;

            Console.WriteLine($"El promedio del alumno es {promedio}");
        }
    }
}
