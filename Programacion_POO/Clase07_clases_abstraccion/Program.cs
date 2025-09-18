namespace Clase07_clases_abstraccion
{
    /*
     Drawio (UML):
    Diagrama de clases

    -- nombre de clase: nombre del objeto que voy a crear (ej. Pokemon). Nombre siempre en singular.
    -- Lista de atributos con el tipo de dato. Van en minuscula
    -- Metodos
    -- Qué devuelve
     */
    internal class Program
    {

        
        static void Main(string[] args)
        {
            //Pokemon pokemon1 = new Pokemon();

            Pokemon pokemon1 = new Pokemon("Pikachu", 50, 20, 40, true);

            string datos;
            datos = pokemon1.MostrarPokemon();
            Console.WriteLine(datos);

            pokemon1.RecargarVida(5);

            Pokemon pokemon2 = new Pokemon("Charmander", 20, 50, 10, false);

            if (pokemon1.Atacar(pokemon2) == true)
            {
                Console.WriteLine("Gano el ataque: {0}", pokemon1.GetNombre());
            }
            else
            {
                Console.WriteLine("{0} se pudo defender del ataque de {1}", pokemon2.GetNombre(), pokemon1.GetNombre());
            }

            Console.WriteLine(pokemon1.MostrarPokemon());
            Console.WriteLine(pokemon2.MostrarPokemon());


            // Cambiar nombre a charmander
            pokemon2.SetNombre("Charmandercito");

            // dar puntos de vida
            pokemon2.SetVida(50);





        }
    }
}
