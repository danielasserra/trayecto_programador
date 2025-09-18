namespace Condicionales_Ejercicios01_07
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //// 1. A partir del ingreso de una edad, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años”.

            int edad;

            Console.WriteLine("Ingrese su edad");
            edad = int.Parse(Console.ReadLine());

            //if (edad == 18)
            //{
            //    Console.WriteLine("Usted tiene 18 años");
            //}

            //// 2. A partir del ingreso de una edad, determinar si la persona es mayor de edad.
            //// Si es mayor o igual que 18 se mostrará el mensaje “UD ES MAYOR DE EDAD”.

            //if (edad >= 18)
            //{
            //    Console.WriteLine("Ud. es mayor de edad");
            //}

            //// A partir del ingreso de una edad, determinar si la persona es mayor de edad o no.
            //// Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario
            //// “UD ES MENOR DE EDAD”.
            //if (edad >= 18)
            //{
            //    Console.WriteLine("Usted es mayor de edad");
            //}
            //else
            //{
            //    Console.WriteLine("Usted es menor de edad");
            //}


            //// A partir del ingreso de la altura de un basquetbolista determinar si es pivot
            //// o no. Para serlo el mismo deberá medir más de 1.80 metros.
            //double altura;

            //Console.WriteLine("Ingrese la altura del jugador: ");
            //altura = double.Parse(Console.ReadLine());

            //if (altura > 180)
            //{
            //    Console.WriteLine("Es pivot");
            //}
            //else
            //{
            //    Console.WriteLine("no es pivot");
            //}

            // Pedirle al usuario su edad, determinar si el usuario es adolescente
            // (edad entre 13 y 17 inclusive)
            if (edad >= 13 &&  edad <= 17)
            {
                Console.WriteLine("el usuario es adolescente");
            }

            // Pedirle al usuario su edad, determinar si el usuario NO es adolescente.
            if (!(edad >= 13 && edad <=17 )) 
            {
                Console.WriteLine("el usuario no es adolescente");
            }

            // Pedirle al usuario su edad, determinar si es mayor (18 años o más),
            // niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive)
            // o adolescente (edad entre 13 y 17 años).
            if (edad >= 18)
            {
                Console.WriteLine("El usuario es mayor");

            }
            else if (edad < 10)
            {
                Console.WriteLine("El usuario es niño/a");
            }
            else if (edad >= 10 && edad <= 13)
            {
                Console.WriteLine("El usuario es preadolescente");
            }
            else
            {
                Console.WriteLine("el usuario es adolescente");
            }
             
        }
    }
}
