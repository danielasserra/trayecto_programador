namespace Desafio01
{
    internal class Druida_Program
    {
        static void Main(string[] args)
        {
            // Declaracion de Variables

            // variable para iniciar juego
            string empezar;

            // Variables: Atributos básicos pj
            string nombrePj;
            string razaPj;
            int edadPj;
            int nivelPj;


            // Inicio del programa

            Console.WriteLine("--------------------------------------------------");
            Console.WriteLine(" ¡Bienvenido al Creador de Personajes de D&D! ");
            Console.WriteLine("--------------------------------------------------\n");

            Console.WriteLine("¿Estás listo para comenzar tu viaje? (si/no)\n");
            empezar = Console.ReadLine();

            if (empezar.ToLower() != "si")
            {
                Console.WriteLine("\nEl destino no puede apresurarse...");
                Console.WriteLine("Regresa cuando tu espíritu esté listo para la aventura.");
                return;
            }
            Console.WriteLine("\n¡Adelante, Héroe!");
            Console.WriteLine("El destino te aguarda");
            Console.WriteLine("Cuando estés listo para comenzar tu aventura, presiona cualquier tecla.");

            Console.ReadKey(); // espera que presiones una tecla
            Console.Clear();

            // completar atributos basicos del pj
            Console.WriteLine("Para embarcarte en esta travesía, primero debemos conocer a tu héroe.");
            Console.WriteLine("\nDime, viajero, ¿cuál es el nombre que llevará tu leyenda?"); 
            nombrePj = Console.ReadLine();
            Console.WriteLine("\nY ¿qué raza marcará tu destino?");
            razaPj = Console.ReadLine();
            Console.WriteLine("\nDime tu edad, viajero, pues cada año vivido deja huella en tu destino");
            edadPj = int.Parse(Console.ReadLine());
            Console.WriteLine("\nFinalmente, ¿en qué nivel de maestría se encuentra tu espíritu aventurero? ");
            nivelPj = int.Parse(Console.ReadLine());

            // creacion del pj
            Druida druida1 = new Druida(nombrePj, razaPj, edadPj, nivelPj);

            Console.WriteLine("\n¡Excelente! Has dado el primer paso hacia la gloria.");
            Console.WriteLine("Extiende tu mano y toca el destino… presiona cualquier tecla para avanzar en tu aventura.");
            Console.ReadKey(); // espera que presiones una tecla
            Console.Clear();

            // rolear estadisticas
            Console.WriteLine("Ahora, las fuerzas del universo se preparan para revelar tus verdaderas habilidades.");
            Console.WriteLine("\nForjarás tu destino con 4 dados de seis caras.");
            Console.WriteLine("\nEl más débil caerá en el olvido...");
            Console.WriteLine("\nY los tres restantes darán forma a tu poder.");
            Console.WriteLine("\nHa llegado la hora de invocar la suerte y descubrir la esencia de tu héroe...");
            Console.WriteLine("\nSi estás listo para enfrentar la verdad que aguarda en los dados, presiona una tecla para continuar");
            Console.ReadKey();
            Console.Clear();

            druida1.GenerarEstadisticas();
            druida1.EstablecerVida();

            //Console.WriteLine(druida1.MostrarDruida());

        //druida1.Transformarse("Mamut");

        //Console.WriteLine(druida1.MostrarDruida());


        }
    }
}
