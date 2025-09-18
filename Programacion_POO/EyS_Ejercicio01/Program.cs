namespace EyS_Ejercicio01
{
    internal class Program
    {
        // Realizar un programa que permita el ingreso de dos números.
        // Calcular la suma, resta, multiplicación y división de los mismos.
        // Mostrar los resultados por pantalla.
        // Utilizar una variable para mostrar el resultado (concatenar).

        static void Main(string[] args)
        {
            float primerNumero;
            float segundoNumero;
            float resultado;

            Console.WriteLine("Ingrese un numero");
            primerNumero = float.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero");
            segundoNumero = float.Parse(Console.ReadLine());

            // suma
            resultado = primerNumero + segundoNumero;
            Console.WriteLine($"La suma de {primerNumero} y {segundoNumero} es {resultado}");

            // resta
            resultado = primerNumero - segundoNumero;
            Console.WriteLine($"La resta de {primerNumero} y {segundoNumero} es {resultado}");

            // multiplicacion
            resultado = primerNumero * segundoNumero;
            Console.WriteLine($"La multiplicación de {primerNumero} y {segundoNumero} es {resultado}");

            // division
            if (segundoNumero != 0)
            { 
                resultado = primerNumero / segundoNumero;
                Console.WriteLine($"La división de {primerNumero} y {segundoNumero} es {resultado}");
            }
            else
            {
                Console.WriteLine("No se puede dividir por cero");
            }
        }
    }
}
