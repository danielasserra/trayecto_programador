namespace Condicionales_Ejercicio08
{
    internal class condicionales08
    {
        static void Main(string[] args)
        {
            /*
             * A partir del ingreso de la altura en centímetros de un 
             * jugador de baloncesto, el programa deberá determinar la 
             * posición del jugador en la cancha, considerando los 
             * siguientes parámetros:
                        Menos de 160 cm: Base
                        Entre 160 cm y 179 cm: Escolta
                        Entre 180 cm y 199 cm: Alero
                        200 cm o más: Ala-Pívot o Pívot
            */

            int altura;

            Console.WriteLine("Ingrese la altura en cm del jugador:");
            altura = int.Parse(Console.ReadLine());

            if (altura < 160)
            {
                Console.WriteLine("La posición del jugador es Base");
            }
            else if (altura < 180)
            {
                Console.WriteLine("La posición del jugador es Escolta");
            }
            else if (altura < 200)
            {
                Console.WriteLine("La posición del jugador es Alero");
            }
            else
            {
                Console.WriteLine("La posición del jugador es Pivot");

            }
        }
    }
}
