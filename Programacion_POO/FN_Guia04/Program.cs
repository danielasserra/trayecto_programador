namespace FN_Guia04
{
    internal class Program
    {
        // Hacer una función que muestre una tabla de multiplicar de un
        // número indicado por el usuario.

        static void tablaMultiplicar(int numero)
        {
            int i = 0;
            int resultado;
            do
            {
                resultado = numero * i;
                Console.WriteLine($"{numero} x {i} = {resultado}");
                i += 1;
            } while (i < 11);
        }
        static void Main(string[] args)
        {
            int numero;
            Console.WriteLine("Ingrese un número entero");
            numero = int.Parse(Console.ReadLine());

            tablaMultiplicar(numero);
        }
    }
}
