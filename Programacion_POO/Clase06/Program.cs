using Clase05_poo;
using Clase06_clases;

namespace Clase06

{
    internal class Program
    {
        static void Main(string[] args)
        {
            ///* -------------- //
            // CUENTA BANCARIA
            // ---------------- */

            //// Llamamos a la clase
            //// Creamos un espacio para almacenar la cuenta bancaria (por eso usamos new)
            //// CuentaBancaria miCuenta = new CuentaBancaria(1, "Pablo Gomez");

            //// Completamos los datos
            ////miCuenta.numeroCuenta = 1;
            ////miCuenta.titular = "Pablo Gomez";
            ////miCuenta.saldo = 1000;

            //CuentaBancaria miCuenta;

            //// creamos variable monto para agregar dinero a la ccuenta
            //double monto;
            //int seleccion;

            //int numeroCuenta;
            //string nombre;

            //Console.WriteLine("Ingrese el numero de cuenta");
            //numeroCuenta = int.Parse(Console.ReadLine());

            //Console.WriteLine("Ingrese el nombre");
            //nombre = Console.ReadLine();

            //miCuenta = new CuentaBancaria(numeroCuenta, nombre);

            //// Llamamos el metodo
            //Console.WriteLine(miCuenta.MostrarInfo());

            //Console.WriteLine(miCuenta.ConsultarSaldo());


            //Console.WriteLine("Ingrese el monto");
            //monto = double.Parse(Console.ReadLine());

            //if (miCuenta.Depositar(monto))
            //{
            //    Console.WriteLine($"Deposito exitoso. Su nuevo saldo es {miCuenta.ConsultarSaldo()}");
            //}
            //else
            //{
            //    Console.WriteLine("No se pudo realizar el deposito. Saldo: " + miCuenta.ConsultarSaldo());
            //}


            //if (miCuenta.Retirar(monto))
            //{
            //    Console.WriteLine($"Retiro exitoso. Su nuevo saldo es {miCuenta.ConsultarSaldo()}");
            //}
            //else
            //{
            //    Console.WriteLine("No se pudo realizar el retiro. Saldo: " + miCuenta.ConsultarSaldo());
            //}


            /* -----
             ALUMNO
             ----- */

            AlumnoClase6 miAlumno;

            string nombreAlumno;
            string apellidoAlumno;
            int dni;

            Console.WriteLine("Ingrese el nombre del alumno");
            nombreAlumno = Console.ReadLine();
            Console.WriteLine("Ingrese el apellido del alumno");
            apellidoAlumno = Console.ReadLine();
            Console.WriteLine("Ingrese el DNI del alumno");
            dni = int.Parse(Console.ReadLine());

            miAlumno = new AlumnoClase6(nombreAlumno, apellidoAlumno, dni);

            miAlumno.Estudiar();

            int nota = miAlumno.RendirExamen();

            Console.WriteLine(miAlumno.MostrarInfoAlumno());


            Console.WriteLine(miAlumno);

        }
    }
}

