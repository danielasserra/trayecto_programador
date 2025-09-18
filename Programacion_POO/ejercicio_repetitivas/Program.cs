namespace ejercicio_repetitivas
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Crear un sistema para una tienda que contenga un menu que permita elegir
            //entre estas opciones:
            //ver una lista de productos
            //agregar nuevos productos - estandarizar ingreso a minusculas
            //eliminar productos - validar eliminacion
            //mostrar la cantidad de productos

            List<string> Productos = new List<string> 
            { 
                "Porotos Aduki", 
                "Porotos Mung", 
                "Lentejas", 
                "Lentejones", 
                "Lentejas rojas" 
            };

            int opcion;

            do
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Lista de Productos");
                Console.WriteLine("2. Agregar Productos");
                Console.WriteLine("3. Eliminar Productos");
                Console.WriteLine("4. Cantidad de Productos");
                Console.WriteLine("5. Salir");
                opcion = int.Parse(Console.ReadLine());

                
                switch(opcion)
                {
                    case 1:
                        foreach (string item in Productos) 
                        { 
                            Console.WriteLine(item); 
                        }
                        break;

                    case 2:
                        Console.WriteLine("Ingrese el nombre del producto:");
                        string nuevo_producto = Console.ReadLine();
                        Productos.Add(nuevo_producto);
                        Console.WriteLine("Producto agregado con éxito");
                        break;

                    case 3:
                        string eliminar_producto;
                        Console.WriteLine("Ingrese el nombre del producto a eliminar:");
                        eliminar_producto = Console.ReadLine();
                        Productos.Remove(eliminar_producto);
                        Console.WriteLine("Producto eliminado con éxito");
                        break;

                    case 4:
                        int cantidad_productos = Productos.Count();
                        Console.WriteLine($"La cantidad de productos es: " + cantidad_productos);
                        break;

                    case 5:
                        Console.WriteLine("\nSaliendo...");
                        break;

                    default:
                        Console.WriteLine("\nOpción inválida");
                        break;



                }

            } while (opcion != 5);


        
        }
    }
}
