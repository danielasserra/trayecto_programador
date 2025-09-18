namespace repetitivasEjercicio03
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Mostrar un menú de opciones (1, 2, 3, salir) que se repita hasta que el usuario elija salir.

            string opcion;

            do
            {
                Console.WriteLine("----------------");
                Console.WriteLine("Menu de Opciones");
                Console.WriteLine("----------------");
                Console.WriteLine("1. Opción 1");
                Console.WriteLine("2. Opcion 2");
                Console.WriteLine("3. Opcion 3\n");
                Console.WriteLine("salir");

                Console.WriteLine("\nSeleccione una opcion");
                opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        Console.WriteLine("Ud. seleccionó la opción 1.\n");
                        break;

                    case "2":
                        Console.WriteLine("Ud. seleccionó la opción 2.\n");
                        break;

                    case "3":
                        Console.WriteLine("Ud. seleccionó la opción 3.\n");
                        break;

                    case "salir":
                        Console.WriteLine("Saliendo del programa...");
                        break;

                    default:
                        Console.WriteLine("Por favor, seleccione una opción válida");
                        break;
                }


            } while (opcion != "salir");
        }
    }
}
