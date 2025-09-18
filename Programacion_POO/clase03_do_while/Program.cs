namespace clase03_do_while
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int opcion;

            do
            {
                Console.WriteLine("Menu: ");
                Console.WriteLine("1. opcion a ");
                Console.WriteLine("2. opcion b ");
                Console.WriteLine("3. salir ");
                Console.WriteLine("Seleccione: ");
                opcion = int.Parse(Console.ReadLine());
            } while (opcion != 3);





            /*
             * LISTAS
             */


            /* List<string> productos = new List<string>(); 
             List<string> productos = new List<string> {"azucar", "harina", "arroz"}*/

            List<string> productos = new List<string> { "azucar", "harina", "arroz" };

            productos.Add("chocolate");

            Console.WriteLine("nombre del producto: ");
            string producto = Console.ReadLine(productos);

            // producto = producto.To.Upper(); convierte a mayusculas

            /*
             * FOREACH *
                BUCLE
            RECORRER COLECCION
             */




            foreach (string item in productos) // recorrer una coleccion
            {
                Console.WriteLine(item);
            }


            /* ELIMINAR ELEMENTOS DE LA LISTA */
            productos.Remove("azucar");
            productos.RemoveAt(2);


            /* CONTAR ELEMENTOS */
            productos.Count();

            Console.ReadKey();
            Console.Clear();

        }
    }
}
