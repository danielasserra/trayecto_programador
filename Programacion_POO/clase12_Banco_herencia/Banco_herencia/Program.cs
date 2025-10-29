using Biblioteca;

namespace Banco_herencia
{
    public class Program
    {
        static void Main(string[] args)
        {
            CuentaBancaria ahorro1 = new CajaDeAhorro("444", "pepe", 12000, 5);
            CuentaCorriente corriente1 = new CuentaCorriente("444", "lala", 3000, 15000);
            CuentaBancaria ahorro2 = new CajaDeAhorro("444", "pepe", 12000, 5);//
            CuentaCorriente corriente2 = new CuentaCorriente("444", "lala", 3000, 15000);
            CuentaBancaria ahorro3 = new CajaDeAhorro("444", "pepe", 12000, 5);//

            List<CuentaBancaria> listaCuentas = new List<CuentaBancaria>();
            listaCuentas.Add(ahorro1);
            listaCuentas.Add(corriente1);
            listaCuentas.Add(ahorro2);
            listaCuentas.Add(ahorro3);

            foreach (CuentaBancaria cuenta in listaCuentas)
            {
                if(cuenta is CajaDeAhorro)
                {
                    Console.WriteLine("True");
                    CajaDeAhorro caja = (CajaDeAhorro)cuenta;
                    caja.CalcularInteres();
                }
                else
                {  Console.WriteLine("False"); }
            }

            foreach (CuentaBancaria cuenta in listaCuentas)
            {
                cuenta.Depositar(5000);
            }

            foreach (CuentaBancaria cuenta in listaCuentas)
            {
                Console.WriteLine(cuenta.ToString());
            }

            //CuentaBancaria c = new CuentaBancaria("444", "titular", 4589);

            //CuentaBancaria ahorro = new CajaDeAhorro("444", "pepe", 12000, 5);// El objeto es caja de ahorro
            //                                                                  // La variable que lo guarda es cuenta bancaria
            //                                                                  // Esto permite crear lista de cuentas bancarias
            //                                                                  // pero dentro definir cajas de ahorro o cuentas corrientes


            //CuentaCorriente corriente = new CuentaCorriente("444", "lala", 3000, 15000);


            //corriente.Retirar(5000);
            //corriente.Retirar(10000);
            //corriente.Depositar(10000);
            //corriente.MostrarDatos();

            //ahorro.Depositar(3000);
            //ahorro.Retirar(90000);
            //((CajaDeAhorro)ahorro).CalcularInteres(); // Casteo caja de ahorro para poder calcular el interes.


            //Console.WriteLine(ahorro.ToString());

            //public override string ToString() {
            //return ($"Cuenta {this.nroCuenta}, Titular {this.titular}, Saldo {this.saldo}");



        }
    }



}
