using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desafio01
{
    public class Druida
    {
        #region Atributos
        // ATRIBUTOS BASICOS
        private string nombre;
        private int edad;
        private string raza;
        private int vidaMax;
        private int vidaActual;
        private int defensa;
        private int nivel; // (entre 1 y 20.  del nivel depende la cantidad de espacio de hechizos)
        private int hechizosMax;
        private int hechizosActual;
        private string formaSalvaje;

        // Atributos: ESTADISTICAS
        private int fuerza;
        private int destreza;
        private int constitucion;
        private int inteligencia;
        private int sabiduria;
        private int carisma;

        #endregion

        #region Propiedades

        #endregion


        // CONSTRUCTOR

        public Druida(string nombre, string raza, int edad, int nivel)
        {
            this.nombre = nombre;
            this.edad = edad;
            this.raza = raza;

            // this.vidaActual = vidaMax;
            this.defensa = (int)(vidaMax * 0.25);

            //nivel
            if (nivel < 1)
                this.nivel = 1;
            else if (nivel > 20)
                this.nivel = 20;
            else
                this.nivel = nivel;

            this.hechizosMax = this.nivel * 2;
            this.hechizosActual = this.hechizosMax;
            this.formaSalvaje = "Aun no se transformó";

            // Inicia con estadisticas estandar

            this.fuerza = 12;
            this.destreza = 13;
            this.constitucion = 10;
            this.inteligencia = 14;
            this.sabiduria = 15;
            this.carisma = 8;

        }

        #region Metodos
        // METODOS
        public string MostrarDruida()
        {
            StringBuilder sb = new StringBuilder();

            sb.AppendLine("----------------- D&D ------------------");
            sb.AppendLine("------------- CLASE DRUIDA -------------");

            sb.AppendLine("\nNombre: " + this.nombre);
            sb.AppendLine("\nRaza: " + this.raza);
            sb.AppendLine("\nEdad: " + this.edad);
            sb.AppendLine("\nForma Salvaje: " + this.formaSalvaje);
            sb.AppendLine("\nVida Maxima: " + this.vidaMax);
            sb.AppendLine("\nVida Actual: " + this.vidaActual);
            sb.AppendLine("\nNivel: " + this.nivel);
            sb.AppendLine("\nEspacio de Hechizos Maxima: " + this.hechizosMax);
            sb.AppendLine("\nEspacio de Hechizos Actual: " + this.hechizosActual);
            sb.AppendLine("\n----------------------------------------");
            return sb.ToString();
        }

        // setter
        public void Transformarse(string animal)
        {
            this.formaSalvaje = animal;
        }

        // Estadísticas
        public void GenerarEstadisticas()
        {
            Random d6 = new Random(); // Representa el dado, genera un numero aleatorio

            // lista con los nombres de las estadisticas para mostrar al usuario 
            string[] nombreEstadistica = { "Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma" };

            for (int i = 0; i < 6; i++) // bucle q recorre las 6 estadisticas
            {

                Console.WriteLine($"\nInvocando los designios del destino para tu {nombreEstadistica[i]}...");
                int[] tiros = new int[4]; // almacena los 4 resultados

                for (int j = 0; j < 4; j++) // bucle para tirar dados
                {
                    Console.WriteLine("\nEscucha el eco de los dioses... Presiona cualquier tecla para lanzar el dado...");
                    Console.ReadKey(true); // usuario debe presionar una tecla para realizar la tirada
                    tiros[j] = d6.Next(1, 7); // representa el dado, genera un numero aleatorio entre 1 y 6
                    Console.WriteLine($"\nEl dado n°{j + 1} rueda con fuerza y revela: {tiros[j]}"); // almacena resultados y los muestra en pantallla
                    Console.WriteLine("\nEl destino aún guarda más revelaciones... Presiona una tecla para continuar");
                    Console.ReadKey();
                    Console.Clear();
                }

                int menor = tiros.Min(); // valor mas bajo
                int suma = tiros.Sum() - menor; // suma las tiradas y resta el dado mas bajo

                // Asignar valor a la estadística correspondiente
                switch (i)
                {
                    case 0: fuerza = suma; break;
                    case 1: destreza = suma; break;
                    case 2: constitucion = suma; break;
                    case 3: inteligencia = suma; break;
                    case 4: sabiduria = suma; break;
                    case 5: carisma = suma; break;
                }

                Console.WriteLine($"El dado menor ({menor}) se desvanece en las sombras del destino...");
                Console.WriteLine($"La {nombreEstadistica[i]} de tu héroe brilla con un poder de {suma}.\n");

                Console.WriteLine("\nEl destino aún guarda más revelaciones... Presiona una tecla para continuar");
                Console.ReadKey();
                Console.Clear();
            }

            Console.WriteLine("Todas las estadísticas han sido forjadas por los hilos del destino.");
        }

        



        // VIDA
        public void EstablecerVida()
        {
            if (nivel == 1)
            {
                vidaMax = 8 + (int)((constitucion - 10) / 2);
                vidaActual = vidaMax;
            }
        }



public void Descansar()
        {
            this.vidaActual = this.vidaMax;
            this.hechizosActual = this.hechizosMax;
        }

        public int Defenderse(int puntosDeDaño)
        {
            if (puntosDeDaño < this.defensa)
            {
                this.vidaActual = this.vidaActual;
            }
            else if ((this.vidaActual - puntosDeDaño) < 0)
            {
                this.vidaActual = 0;
            }
            else
            {
                this.vidaActual -= puntosDeDaño;
            }
            return this.vidaActual;
        }

        public int Curarse(int puntosDeVida)
        {
            if ((this.vidaActual + puntosDeVida) > this.vidaMax)
            {
                this.vidaActual = this.vidaMax;
            }
            else
            {
                this.vidaActual += puntosDeVida;
            }

            return this.vidaActual;
        }


    }


}

#endregion

