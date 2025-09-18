using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace ClasesEjercicioPaqueteTuristico
{
    internal class PaqueteTuristico
    {

        private int codigo;
        private string destino;
        private double precioBase;
        private int cupoMaximo;
        private int reservados;

        public PaqueteTuristico(int codigo, string destino, double precioBase, int cupoMaximo)
        {
            this.codigo = codigo;
            this.destino = destino;
            this.precioBase = precioBase;
            this.cupoMaximo = cupoMaximo;
            this.reservados = 0;
        }

        // METODOS

        public bool ReservarLugar(int cantidad)
        {
            /*Aumenta la cantidad de reservados si hay lugares disponibles.
            Devuelve true si se pudo reservar, false en caso contrario.*/
            if (cantidad > 0 && (reservados + cantidad) <= cupoMaximo)
            {
                reservados += cantidad;
                Console.WriteLine("Reserva realizada");
                return true;
            }
            Console.WriteLine("Reserva no realizada");
            return false;
        }

        public bool CancelarReserva(int cantidad)
        {
            // Resta esa cantidad de lugares reservados, siempre que no sea mayor a lo ya reservado.
            if (cantidad > 0 && reservados >= cantidad)
            {
                reservados -= cantidad;
                Console.WriteLine("Reserva cancelada");
                return true;
            }
            Console.WriteLine("Reserva no cancelada");
            return false;
        }







    }
}
