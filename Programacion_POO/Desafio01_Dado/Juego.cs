using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desafio01_Dado
{
    internal class Juego
    {
        // atributos
        private Dado dado;

        // Constructor
        public Juego(Dado dado)
        {
            this.dado = dado;
        }

        public void Jugar()
        {
            int numeroDado = dado.GetCaras();

            Console.WriteLine("¡Bienvenido, valiente aventurero, al desafío del Dado Épico!");
            Console.WriteLine("Hoy, el destino se decide con un simple giro de la fortuna...");
            Console.WriteLine($"Si sacas un {numeroDado} ¡GANARÁS LA GLORIA ETERNA!");
            Console.WriteLine("Cuidado... un solo error y la oscuridad te reclamará.");
            Console.WriteLine("Presioná cualquier tecla y deja que el azar decida tu destino...");
            Console.WriteLine("El dado se eleva en el aire, girando como el destino mismo...");
            Console.ReadKey();
            Console.Clear();

            int resultado = dado.HacerTirada();

            if (resultado == numeroDado)
            {
                Console.WriteLine($"¡Increíble! ¡Has obtenido un {resultado}! El mundo celebra tu triunfo!");
            }
            else
            {
                Console.WriteLine($"Tu tirada fue un {resultado}. El destino no estuvo de tu lado esta vez...");
                Console.WriteLine("Pero no te rindas, valiente, la gloria aún puede ser tuya.");
            }
            Console.WriteLine("\nGracias por jugar al desafío del Dado Épico. Hasta la próxima aventura...");

        }

    }
}
