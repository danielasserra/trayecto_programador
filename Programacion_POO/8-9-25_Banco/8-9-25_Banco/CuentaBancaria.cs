using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _8_9_25_Banco
{
    public class CuentaBancaria
    {
        private int numeroCuenta;
        private string titular;
        private double saldo;
        private int cantidadOperaciones;

        public CuentaBancaria(int numeroCuenta, string titular)
        {
            this.numeroCuenta = numeroCuenta;
            this.titular = titular;
            this.saldo = 0;
            //this.cantidadOperaciones = cantidadOperaciones;
        }

        public string MostrarInfo()
        {
            string info = $"El numero de cuenta es {numeroCuenta} \nTitular: {titular} \nSaldo: {saldo}";

            return info ;
        }

        public double ConsultarSaldo()
        {
            return saldo;
        }

        public bool Depositar(double monto)
        {
            bool exito = true; ;
            if (monto <= 0)
            {
                exito = false;
            }
            else
            {
                saldo += monto;
            }
            return exito;
        }

        public bool Retirar(double monto)
        {
            bool exito = true; ;
            if (monto <= 0 || monto > saldo)
            {
                exito = false;
            }
            else
            {
                saldo -= monto;
            }
            return exito;
        }
    }
}
