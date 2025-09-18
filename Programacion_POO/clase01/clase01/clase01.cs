using static System.Runtime.InteropServices.JavaScript.JSType;

namespace clase01
{
    internal class clase01
    {
        static void Main(string[] args)
        {

            // EXPLICACION :
            
            // DECLARACION DE VARIABLES

            string nombre = "cualquier cosa"; //valor por defecto
            int edad;
            double altura;
            int anioNacimiento;

            // PROCESOS

            Console.WriteLine("Ingrese su nombre"); //Writeline es para mostrar x pantalla
            nombre = Console.ReadLine(); //Readline es para ingresar un dato

            Console.WriteLine("Ingrese su edad");
            edad = int.Parse(Console.ReadLine());

            Console.WriteLine("Ingrese su altura");
            altura = double.Parse(Console.ReadLine());


            Console.WriteLine("Ingrese su año de nacimiento");
            altura = int.Parse(Console.ReadLine());

            anioNacimiento = 2025 - edad;

            // SALIDA DE DATOS
            Console.WriteLine($"hola, {nombre}. Tenes {edad} años. Medis {altura} metros");

            Console.WriteLine($"hola, {nombre}");
            Console.WriteLine($"hola " + nombre);




        }
    }
}
