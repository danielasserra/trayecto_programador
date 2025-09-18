using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase06_clases
{
    // nombre de las clases: mayuscula: con el nombre del objeto q estoy creando
    // cambiar internal a public para verlo en main
    public class CuentaBancaria // upper cammel case
    {
        // agregar atributos en lower cammel case. siempre sustantivos
        private int numeroCuenta;
        private string titular;
        private double saldo;

        //--------------//
        // CONSTRUCTOR //
        //--------------//
        /*
        los atributos siempre van private
            Constructor: metodo para darle valor a los atributos
        constructores 
                siempre son publicos
                no devuelven datos
                simil a metodos
                mismo nombre q la clase, ej. CuentaBancaria
        */
        public CuentaBancaria(int nroCuenta, string titular)
        {
            //THIS HACE REFERENCIA A LA INSTANCIA DEL OBJETO EN Q ESTAMOS TRABAJANDO
            this.numeroCuenta = nroCuenta;
            this.titular = titular;
            this.saldo = 0;
        }

        public string MostrarInfo() // metodo verbo/accion. upper cammel case
        {
            string info = $"El numero de la cuenta es {numeroCuenta}. \n Titular: {titular}. \n Saldo: {saldo}";
            return info;
        }

        public double ConsultarSaldo()
        {
            return saldo;
        }

        public bool Depositar(double monto)
        {
            bool exito = true;

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
            bool exito = true;

            if (monto <= 0 || saldo < monto)
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
