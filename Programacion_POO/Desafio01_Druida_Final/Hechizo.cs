using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desafio01_Druida_Final
{
    public enum TipoHechizo
    {
        Ataque,
        Defensa,
        Curacion,
        Movimiento,
        Otro
    }
    internal class Hechizo
    {
        private string nombre;
        private TipoHechizo tipo;
        private int nivel; // si no tiene suficiente nivel, no puede realizar el hechizo
        private int costoMana; // si no tiene suficiente mana, no puede realizar el hechizo

    }
}

/*
 
    internal class Aplicacion
    {
        // EJ:
        // TipoAplicacion t = TipoAplicacion.Juego;

        //Atributos
        private string nombre;
        private int tamaño;
        private TipoAplicacion tipo;

        // constructor
        public Aplicacion(string nombre, int tamaño, TipoAplicacion tipo) 
        {
            this.nombre = nombre;
            this.tamaño = tamaño;
            this.tipo = tipo;
 */
