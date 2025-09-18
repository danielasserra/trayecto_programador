namespace RepetitivasEjercicio04
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Ingresar 10 números enteros. Determinar el máximo y el mínimo.

            int cantidad;
            Console.WriteLine("Especifique la cantidad de numeros a ingresar");
            cantidad = int.Parse(Console.ReadLine());
            

            int numero;
            int maximo = 0;
            int minimo = 0;

            for (int i = 0; i < cantidad; i++)
            {
                Console.WriteLine("Ingrese un numero");
                numero = int.Parse(Console.ReadLine());

                if (i == 0)
                {
                    maximo = numero;
                    minimo = numero;
                }
                else
                {
                    if (numero > maximo)
                    {
                        maximo = numero;
                    }

                    if (numero < minimo)
                    {
                        minimo = numero;
                    }
                }
                
            }

            Console.WriteLine($"El numero máximo es {maximo} y el mínimo es {minimo}");

        }
    }
}
