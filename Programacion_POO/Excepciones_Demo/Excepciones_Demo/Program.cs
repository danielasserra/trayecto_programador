namespace Excepciones_Demo
{
    internal class Program
    {
        
        static void Main(string[] args)
        {
            // CONSIGNA

            // Una tienda necesita un programa en C# que calcule el precio final de un producto luego de aplicar un descuento.

            // El programa debe:

            // Pedir al usuario el precio del producto (en número decimal).

            // Pedir el porcentaje de descuento (por ejemplo, 15 para 15%).

            // Calcular y mostrar el precio final.

            // El programa debe manejar las siguientes excepciones:

            // Si el usuario ingresa algo que no sea un número válido, mostrar:
            // "Error: el valor ingresado no es numérico."

            // Si el descuento ingresado es negativo o mayor que 100, lanzar manualmente una excepción (ArgumentOutOfRangeException) con el mensaje:
            // "El descuento debe estar entre 0 y 100."

            // Usar un bloque finally para mostrar el mensaje:
            // "Operación finalizada."

            //-------------------------------------------------------------------------------------------//

            
            
            try
            {
                Console.WriteLine("Ingrese el precio del producto: ");

                double precioProducto = double.Parse(Console.ReadLine());

                Console.WriteLine("Ingrese el porcentaje de descuento: ");

                int porcentajeDescuento = int.Parse(Console.ReadLine());

                if (porcentajeDescuento < 0 || porcentajeDescuento > 100)
                {
                    throw new ArgumentOutOfRangeException(null,"El descuento debe estar entre 0 y 100.");
                }

                double precio = precioProducto - (precioProducto * (porcentajeDescuento / 100));

                Console.WriteLine($"El precio final es {precio}");

            }
            catch (FormatException)
            {
                Console.WriteLine("Error: el valor ingresado no es numerico");
            }
            catch (ArgumentOutOfRangeException)
            {
                Console.WriteLine("El descuento debe estar entre 0 y 100");
            }
            catch (Exception)
            {
                Console.WriteLine("Error");
            }

            finally
            {
                Console.WriteLine("Operación finalizada");
            }
            



            


        }
    }
}

//static void VerificarEdad(int edad)
//{
//    if (edad <= 0)
//    {
//        throw new Exception("La edad no puede ser cero o negativa");
//    }

//}


//int edad = -5;

//try
//{
//    VerificarEdad(edad);
//}
//catch (Exception ex)
//{
//    Console.WriteLine(ex.Message);
//}

///////////////////////////////////////
//int a = 5;
//int b = 0;
////int c = a/b;
//// error: excepcion no controlada
//// se resuelve con if (b == 0) msj de error

//try
//{
//    int c = a / b;
//}

//// EXCEPCION GENERICA
//catch (Exception e)
//{
//    //Console.WriteLine(e.ToString());
//    // muestra msj de error original
//    // hay q hacerlo amistoso para el usuario
//    Console.WriteLine("no se puede dividir por cero");
//}

//// FORMAT EXCEPTION (si el usuario ingresa letras en vez de numeros)
//// Divide by zero (si el usuario ingresa cero)

//int[] numeros = { 1, 2, 3};

//try
//{
//    Console.WriteLine(numeros[5]); // indice fuera de rango
//}
//catch (IndexOutOfRangeException ex)
//{
//    // Mensaje de la excepcion:
//    //Console.WriteLine(ex.Message);
//    // sirve de referencia, no se lo muestro al usuario
//    Console.WriteLine("Imposible acceder al elemento");
//}
//finally
//{
//    Console.WriteLine("Me meti por aca"};
