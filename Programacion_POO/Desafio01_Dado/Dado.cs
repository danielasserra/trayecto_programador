using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desafio01_Dado
{
    internal class Dado
    {
        // atributos
        private int caras;
        private string color;
        private int ultimoResultado;

        // constructor
        public Dado(int caras, string color)
        {
            this.caras = caras;
            this.color = color;
            this.ultimoResultado = 0;
        }

        // GETTERS
        public int GetCaras()
        {
            return this.caras;
        }

        public string GetColor()
        {
            return this.color;
        }

        public int GetUltimoResultado()
        {
            return this.ultimoResultado;
        }

        // SETTERS

        public void SetColor(string color)
        {
            this.color = color;
        }

        public void SetCaras(int caras)
        {
            this.caras = caras;
        }

        public void SetUltimoResultado(int ultimoResultado)
        {
            if(ultimoResultado < 1 || this.ultimoResultado > this.caras)
            {
                Console.WriteLine($"El destino se niega a ser manipulado: el último resultado no puede ser menor a 1 ni mayor a {this.caras}.");
            }
            else
            {
                this.ultimoResultado = ultimoResultado;
            }
        }

        public string MostrarDado()
        {
            StringBuilder sb = new StringBuilder();

            sb.AppendLine("Observas el dado frente a ti, una reliquia de tiempos antiguos...");
            sb.AppendLine($"Este dado posee {caras} caras, cada una custodiando el destino de los valientes.");
            sb.AppendLine($"Su color es {color}, brillante como la promesa de la victoria.");
            sb.AppendLine($"La última tirada fue {ultimoResultado}, un eco del azar que desafía a los mortales.");

            return sb.ToString();
        }

        public int HacerTirada()
        {
            Random r = new Random();
            this.ultimoResultado = r.Next(1, this.caras + 1);
            return this.ultimoResultado;
        }
    }
}
