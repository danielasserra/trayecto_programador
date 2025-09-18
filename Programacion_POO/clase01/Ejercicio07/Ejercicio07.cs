namespace Ejercicio07
{
    internal class Ejercicio07
    {
        static void Main(string[] args)
        {
            // Realizar un programa que pida dos números enteros.
            // Calcular y mostrar el resto de la división entre ambos números.
            // Ej: "El resto de dividir 7 por 2 es: 1" .

            int numeroA = 7;
            int numeroB = 3;
            int resto;

            resto = numeroA % numeroB;

            Console.WriteLine($"El resto de dividir {numeroA} por {numeroB} es {resto}");
        }
    }
}
