namespace Biblioteca
{
    public class CuentaBancaria
    {
        protected string nroCuenta;
        protected string titular;
        protected double saldo;

        public CuentaBancaria(string nroCuenta, string titular, double saldo)
        {
            this.nroCuenta = nroCuenta;
            this.titular = titular;
            this.saldo = saldo;
        }

        #region METODOS

        public void Depositar(double monto)
        {
            if (monto <= 0)
            {
                Console.WriteLine("El monto debe ser positivo");
            }
            else
            {
                this.saldo += monto;
                Console.WriteLine($"Deposito de ${monto}, ud. dispone de ${this.saldo}");
            }
        }

        public virtual void Retirar(double monto)
        {
            if (monto <= 0)
            {
                Console.WriteLine("El monto debe ser positivo");
            }
            else if(monto > this.saldo)
            {
            }
            else
            {
                this.saldo -= monto;
                Console.WriteLine($"Deposito de ${monto}, ud. dispone de ${this.saldo}");
            }
        }

        public virtual void MostrarDatos()
        {
            Console.WriteLine($"Cuenta {this.nroCuenta}, Titular {this.titular}, Saldo {this.saldo}");
        }
    
    }
}
#endregion 