namespace repetitivasEjercicio02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Generar un número aleatorio del 1 al 10 y permitir intentos infinitos hasta acertar.

            Random aleatorio = new Random();
            int numero = aleatorio.Next(1,11);

            int numeroIngresado;
            do
            {
                Console.Write("Ingresa el numero ganador: ");
                numeroIngresado = int.Parse(Console.ReadLine());
                if (numeroIngresado != numero)
                {
                    Console.WriteLine("¡Intentalo nuevamente!\n");
                }
                    
            } while (numeroIngresado != numero);


            Console.WriteLine("¡Acertaste!");
        }
    }
}
