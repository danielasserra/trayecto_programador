namespace CondicionalesEjercicio02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Escribe un programa que pregunte al usuario si tiene un título universitario
            // o si tiene experiencia laboral. Si tiene un título universitario o experiencia 
            // laboral, muestra un mensaje que diga "Eres elegible para el trabajo".
            // De lo contrario, muestra un mensaje que diga "No eres elegible para el trabajo".

            Console.WriteLine("¿Posee titulo universitario? si/no");
            string tituloUniversitario = Console.ReadLine().ToLower();
            Console.WriteLine("¿Tiene experiencia laboral? si/no");
            string experienciaLaboral = Console.ReadLine().ToLower();

            if (tituloUniversitario == "si" ||  experienciaLaboral == "si")
            {
                Console.WriteLine("Eres elegible para el trabajo");
            }
            else
            {
                Console.WriteLine("No eres elegible para el trabajo");
            }

        }
    }
}
