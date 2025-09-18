namespace FN_Guia10
{
    internal class Program
    {
        //  Ingresar un número. Determinar si el número es primo o no.

        static void EsPrimo(int numero)
        {
            if (numero <= 1)
            {
                Console.WriteLine($"El numero {numero} no es primo");
                return;
            }

            for (int i = 2; i < numero; i++)
            {
                if (numero % i == 0)
                {
                    Console.WriteLine($"El numero {numero} no es primo");
                    return;
                }
            }
            Console.WriteLine($"El numero {numero} es primo");
        }

        static void Main(string[] args)
        {
            int numero;
            Console.WriteLine("Ingrese un numero");
            numero = int.Parse(Console.ReadLine());
            EsPrimo(numero);
        }
    }
}
