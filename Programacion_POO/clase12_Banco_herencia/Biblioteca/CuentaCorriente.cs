using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Biblioteca
{
    public class CuentaCorriente: CuentaBancaria
    {
        #region Atributos
        private double limiteDescubierto;


        #endregion

        public CuentaCorriente (string nroCuenta, string titular, double saldo, double limite):base(nroCuenta, titular, saldo)
        {
            this.limiteDescubierto = limite;
        }

        public override void Retirar(double monto)
        {
            if (monto <= 0)
            {
                Console.WriteLine("El monto debe ser positivo");
            }
            else if (monto > this.saldo + this.limiteDescubierto)
            {
            }
            else
            {
                this.saldo -= monto;
                Console.WriteLine($"Deposito de ${monto}, ud. dispone de ${this.saldo}");
            }
        }

        public override void MostrarDatos()
        {
            base.MostrarDatos();
            Console.WriteLine($"Limite Descubierto {this.limiteDescubierto}");
        }
    }
}
