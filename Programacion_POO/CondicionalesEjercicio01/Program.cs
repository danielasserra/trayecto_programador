namespace CondicionalesEjercicio01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             Escribe un programa que pregunte al usuario su edad y si tiene licencia de conducir. 
            Si la edad es mayor o igual a 18 y tiene licencia de conducir, muestra un mensaje que diga "Puedes conducir".
            De lo contrario, muestra un mensaje que diga "No puedes conducir".
            */

            Console.WriteLine("Ingrese su edad");
            int edad = int.Parse(Console.ReadLine());
            Console.WriteLine("¿Tiene licencia de conducir? si/no");
            string licenciaConducir = Console.ReadLine().ToLower();

            if (edad >= 18 && licenciaConducir == "si")
            {
                Console.WriteLine("Puede Conducir");
            }
            else
            {
                Console.WriteLine("No puede conducir");

            }
        }
    }
}
