using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Biblioteca
{
    public class CajaDeAhorro: CuentaBancaria
    {
        private double tasaInteres;

        public CajaDeAhorro(string nroCuenta, string titular, double saldo, double tasaInteres):base(nroCuenta, titular, saldo)
        {
            this.tasaInteres = tasaInteres;
        }

        public void CalcularInteres()
        {
            double interes = saldo * (tasaInteres / 100);
            this.saldo += interes;
            Console.WriteLine($"Interes del {tasaInteres}% aplicado al {interes}. Nuevo saldo ${this.saldo}");
        }

        public override void MostrarDatos()
        {
            base.MostrarDatos();
            Console.WriteLine($"Tasa interes {this.tasaInteres}");
        }

    }
}
