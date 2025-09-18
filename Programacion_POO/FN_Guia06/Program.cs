namespace FN_Guia06
{
    internal class Program
    {
        /* 
            Crear una función que determine si un número es primo o no. Retorna true si lo es.
         
            Para comprobar si un número es primo, debes intentar dividirlo por todos los números 
            enteros menores que él. Si ninguna de estas divisiones da un resultado exacto 
            (es decir, el resto no es cero), entonces el número es primo. Es importante recordar
            que el número 1 no es primo, ya que solo tiene un divisor 
        */
        static bool PrimoONo(int numero)
        {
            if (numero <= 1)
                return false; // 0 y 1 no son primos

            for (int i = 2; i < numero; i++)
            {
                if (numero % i == 0)
                {
                    return false;
                }
            }

            return true;
        }
        static void Main(string[] args)
        {
            int numero;

            Console.WriteLine("Ingrese un numero: ");
            numero = int.Parse(Console.ReadLine());

            bool esPrimo = PrimoONo(numero);
            Console.WriteLine("¿Es Primo? " + esPrimo);
        }
    }
}
