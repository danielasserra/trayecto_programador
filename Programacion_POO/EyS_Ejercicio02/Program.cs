namespace EyS_Ejercicio02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Realizar un programa que pida dos números enteros.
            //Calcular y mostrar el resto de la división entre ambos números.
            //Ej: "El resto de dividir 7 por 2 es: 1" .

            Console.WriteLine("Ingrese un numero");
            float unNumero = float.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero");
            float otroNumero = float.Parse(Console.ReadLine());

            float resultado = unNumero % otroNumero;
            Console.WriteLine($"El resto de dividir {unNumero} por {otroNumero} es {resultado}");

        }
    }
}
