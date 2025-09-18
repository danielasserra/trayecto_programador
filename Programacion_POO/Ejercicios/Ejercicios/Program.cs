namespace Ejercicios
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //* 1. Realizar un programa que muestre por terminal el mensaje: 
            //* “Esto no anda: funciona”.

            Console.WriteLine("Esto no anda: Funciona");
            //* 2. Realizar un programa que pida el ingreso del nombre de una persona 
            //* input y lo muestre con el formato: “Su nombre es: ___“

            string nombre;
            Console.WriteLine("Ingrese su nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine($"Su nombre es: " + nombre);

            //* 3. Realizar un programa que pida el ingreso del nombre y la edad de una 
            //* persona por input. Mostrar la información con el siguiente formato: 
            //* “Su nombre es: ____ y tiene: ___ años”

            string nombre3;
            int edad;
            Console.WriteLine("Ingrese su nombre:");
            nombre3 = Console.ReadLine();
            Console.WriteLine("Ingrese su edad:");
            edad = int.Parse(Console.ReadLine());
            Console.WriteLine($"Su nombre es: {nombre} y tiene: {edad} años");

            //* 4. Ingresar dia, mes y año y mostrar la fecha con el siguiente formato: 
            //* La fecha ingresada es: xx/xx/xxxx”

            int dia;
            int mes;
            int año;

            Console.WriteLine("Ingrese el día: ");
            dia = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese el mes:");
            mes = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese el año:");
            año = int.Parse(Console.ReadLine());
            Console.WriteLine($"La fecha ingresada es: {dia}/{mes}/{año}");


        }
    }
}
