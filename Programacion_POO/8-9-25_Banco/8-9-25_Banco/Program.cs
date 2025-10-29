namespace _8_9_25_Banco
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CuentaBancaria miCuenta = new CuentaBancaria(1, "Pablo Gomez");

            //miCuenta.numeroCuenta = 1;
            //miCuenta.titular = "Pablo Gomez";
            //miCuenta.saldo = 100000;

            Console.WriteLine(miCuenta.MostrarInfo());
            Console.WriteLine(miCuenta.ConsultarSaldo());

            Console.WriteLine("Monto a depositar");
            double monto = double.Parse(Console.ReadLine());

            if (miCuenta.Depositar(monto))
            {
                Console.WriteLine($"Deposito exitoso su nuevo saldo es ${miCuenta.ConsultarSaldo()}");
            }
            else
            {
                Console.WriteLine("No se pudo hacer el deposito");
            }

            Console.WriteLine("Monto a retirar");
            monto = double.Parse(Console.ReadLine());

            if (miCuenta.Retirar(monto))
            {
                Console.WriteLine($"Retiro exitoso su nuevo saldo es ${miCuenta.ConsultarSaldo()}");
            }
            else
            {
                Console.WriteLine("No se pudo hacer el retiro");
            }
        }
    }
}
