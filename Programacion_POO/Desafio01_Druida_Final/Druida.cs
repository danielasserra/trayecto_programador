using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desafio01_Druida_Final
{
    public class Druida
    {
        #region Atributos

        private string nombre;
        private int nivel;
        private int hpMax;
        private int hpActual;
        private int constitucion;
        private int manaMax;
        private int manaActual;
        private bool consciente;
        private string formaSalvaje;
        // ataque?


        #endregion

        #region Propiedades

        public string Nombre // se puede ver y modificar
        {
            get
            {
                return this.nombre;
            }
            set
            {
                this.nombre = value;
            }
        }
        public int Nivel
        {
            get
            {
                return this.nivel;
            }
            private set // solo se modifica con metodo SubirNivel()
            {
                if (this.nivel < 0)
                {
                    this.nivel = 0;
                }
                else if (this.nivel > 20)
                {
                    this.nivel = 20;
                }
            }
        }
        public int HpMax  // solo se puede ver porque se modifica mediante metodo
        {
            get
            {
                return this.hpMax;
            }
        }
        public int HpActual  // solo se puede ver porque se modifica mediante metodo
        {
            get
            {
                return this.hpActual;
            }
        }


        public int ManaMax  // solo se puede ver porque se modifica mediante metodo
        {
            get
            {
                return this.manaMax;
            }
            private set
            {
                this.manaMax = this.nivel * 2;
                this.ManaActual = manaMax;
            }
        }

        public int ManaActual
        {
            get
            {
                return this.manaActual;
            }
            private set
            {
                this.ManaActual = value;
            }
        }
        public bool Consciente  // solo se puede ver porque se modifica mediante metodo
        {
            get
            {
                return this.consciente;
            }
        }
        public string FormaSalvaje  // solo se puede ver porque se modifica mediante metodo
        {
            get
            {
                return this.formaSalvaje;
            }
        }

        public int Constitucion
        {
            get
            {
                return this.constitucion;
            }
        }

        #endregion

        #region Constructores

        public Druida(string nombre, int nivel)
        {
            this.nombre = nombre;
            this.nivel = nivel;
            this.hpMax = nivel * 10; // nivel x 10 = vida
            this.hpActual = this.hpMax; // inicia vida actual = vida maxima
            this.constitucion = (int)(hpMax * 0.25); // defensa: 25% de la vida
            this.manaMax = nivel * 2; // nivel x 2 = energia magica
            this.manaActual = this.manaMax; // inicia energia magica actual = energia magica maxima
            this.consciente = true;
            this.formaSalvaje = "Aun no se transformó";
        }

        #endregion

        #region Metodos

        public string MostrarDruida()
        {
            StringBuilder sb = new StringBuilder();

            sb.AppendLine("----------------- D&D ------------------");
            sb.AppendLine("------------- CLASE DRUIDA -------------");

            sb.AppendLine("\nNombre: " + this.nombre);
            sb.AppendLine("\nVida Maxima: " + this.hpMax);
            sb.AppendLine("\nVida Actual: " + this.hpActual);
            sb.AppendLine("\nCapacidad defensiva: " + this.constitucion);
            sb.AppendLine("\nForma Salvaje: " + this.formaSalvaje);
            sb.AppendLine("\nNivel: " + this.nivel);
            sb.AppendLine("\nEnergía mágica Maxima: " + this.manaMax);
            sb.AppendLine("\nEnergía mágica Actual: " + this.manaActual);
            sb.AppendLine("\nEstá consciente: " + this.consciente);
            sb.AppendLine("\n----------------------------------------");
            return sb.ToString();
        }

        public void Transformarse(string animal) 
            // Faltan condiciones: cantidad de mana, si ya está transformado
        {
            this.formaSalvaje = animal;
        }

        



        public void Descansar()
        {
            this.hpActual = this.hpMax;
            this.manaActual = this.manaMax;
            this.consciente = true;
        }

        public int Defenderse(int puntosDeDaño)
        {
            if (puntosDeDaño < this.constitucion)
            {
                this.hpActual = this.hpActual;
            }
            else if ((this.hpActual - puntosDeDaño) < 0)
            {
                this.hpActual = 0;
            }
            else
            {
                this.hpActual -= puntosDeDaño;
            }
            return this.hpActual;
        }

        public int Curarse(int puntosDeVida) // FALTA USAR MANA!!
        {
            if ((this.hpActual + puntosDeVida) > this.hpMax)
            {
                this.hpActual = this.hpMax;
            }
            else
            {
                this.hpActual += puntosDeVida;
            }

            return this.hpActual;
        }

        #endregion

    }
}

// FALTA!!!

// SubirNivel() - aumenta nivel +1, hpMax (nivel x 10) y manaMax (nivel x2)
// Atacar() - dañoAtaque - Mana
// Ver metodos que falta completar
// 