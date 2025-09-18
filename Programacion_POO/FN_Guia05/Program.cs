namespace FN_Guia05
{
    internal class Program
    {
        // Crear una función que determine si un número es par o no. Retorna true si lo es.
        static bool parONo(int numero)
        {
            if (numero % 2 == 0)
            {
                return true;
            }
            else
            {
                return false;
            }

        }
        static void Main(string[] args)
        {
            int numero;
            Console.WriteLine("Ingrese un número entero");
            numero = int.Parse(Console.ReadLine());
            bool esPar = parONo(numero);
            Console.WriteLine("¿Es par? " + esPar);
        }
    }
}
