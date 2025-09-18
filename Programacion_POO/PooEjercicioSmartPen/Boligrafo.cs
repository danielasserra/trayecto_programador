using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PooEjercicioSmartPen
{
    public class Boligrafo
    {

        #region Atributos
        // ATRIBUTOS
        private int capacidadTintaMaxima = 100;
        private string grosorPunta;
        private string color;
        private int cantidadTinta = 80;
        #endregion

        #region Constructor

        // CONSTRUCTOR
        public Boligrafo(string grosorPunta, string color)
        {
            this.grosorPunta = grosorPunta;
            this.color = color;
        }
        #endregion

        // METODOS

        public string Escribir(string texto)
        {
            int gasto = texto.Length;

            if (grosorPunta.ToLower() == "grueso")
            {
                gasto *= 2;
            }

            if (cantidadTinta >= gasto)
            {
                cantidadTinta -= gasto;
                return texto;
            }
            else
            {
                return "No alcanza la tinta";
            }

        }

        public string Recargar(int cantidad)
        {
            if (cantidad < 0)
            {
                return "La cantidad a recargar debe ser mayor a cero";
            }

            cantidadTinta += cantidad;

            if (cantidadTinta > capacidadTintaMaxima)
            {
                int sobra;
                sobra = cantidadTinta - capacidadTintaMaxima;
                cantidadTinta -= sobra;

                return $"Se recargó la lapicera al máximo y sobran {sobra} unidades de tinta";
            }
            return "Lapicera recargada";

        }

    }
}
