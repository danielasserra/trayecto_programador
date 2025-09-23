namespace Desafio01_Dado
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // declaracion de variables
            int caras;
            string color;
            string respuesta;

            // solicitar datos al usuario
            Console.WriteLine("Forjarás el destino de tu dado...");
            Console.WriteLine("Dime, viajero: ¿cuántas caras tendrá el artefacto del azar?");
            caras = int.Parse(Console.ReadLine());
            Console.WriteLine("¿Y de qué color será la joya que esconde el poder del destino?");
            color = Console.ReadLine();
            Console.WriteLine("El dado ha sido invocado.");
            Console.WriteLine("Presiona cualquier tecla y contempla cómo cobra vida...");
            Console.ReadKey();
            Console.Clear();

            // inicializar dado

            Dado miDado = new Dado(caras, color);

            // llamar metodos

            Console.WriteLine("Ha llegado el momento... ¿estás listo para invocar la primera tirada? (si / no)");
            respuesta = Console.ReadLine();

            while (respuesta == "si".ToLower())
            {
                Console.WriteLine("El aire se estremece... ¡lanza tu dado presionando una tecla, valiente!");
                Console.ReadKey();
                Console.WriteLine($"El destino ha hablado: ¡ha caído un {miDado.HacerTirada()}!");
                Console.WriteLine("¿Quieres tentar otra vez a la fortuna? (si / no)");
                respuesta = Console.ReadLine();
                Console.WriteLine("Presiona cualquier tecla para continuar tu travesía...");
                Console.ReadKey();
                Console.Clear();
            }

            Console.WriteLine("Viajero... contempla ahora la reliquia que has forjado con tus propias manos.");
            Console.WriteLine("Presiona una tecla y revela su grandeza..."); 
            Console.ReadKey();
            Console.Clear();

            Console.WriteLine(miDado.MostrarDado());

            Console.WriteLine("El poder del dado queda sellado... hasta que alguien vuelva a invocarlo.");
            Console.ReadKey();
            Console.Clear();

            // inicializacion del juego
            Juego miJuego = new Juego(miDado);

            Console.WriteLine("Pero antes de que partas, una última sombra se cierne sobre tu destino...");
            Console.WriteLine("Ha llegado el momento supremo.");
            Console.WriteLine("La prueba final te aguarda: ¡el Juicio del Dado!");
            Console.WriteLine("\nToca una tecla, y deja que el azar decida tu legado...");

            Console.ReadKey();
            Console.Clear();
            miJuego.Jugar();


        }
    }
}
