using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase07_clases_abstraccion
{
    // si la clase es publica se puede ver desde cualquier lado, en este proyecto y tambien en otros.

    public class Pokemon
    {
        //REGIONES PARA ORDENAR
        #region Atributos
        // ATRIBUTOS

        // Constructor por defecto, está implicito
        // Este constructor no existe en esta clase implicitamente, pero existe.
        // Crea los objetos en Null o Vacio.
        // Puedo crear una instancia a partir de ese constructor implicito
        // Constructores se pueden sobrecargar: puedo crear distintos constructores para una clase

        string nombre; // que sea de Lectura y escritura. Necesito dos metodos. Getter (lectura) y Setter(escritura)
        int vida;
        int ataque; // Getter (lectura)
        int defensa;
        bool esShinny;

        #endregion

        #region Constructores

        // CONSTRUCTOR PARAMETRIZADO
        // xq recibe parametros e inicializa c/u de los atributos de la clase
        // Cuando creo un constructor explicito, como este, el constructor implicito deja de existir.

        public Pokemon(string nombre, int vida, int ataque, int defensa, bool esShinny)
        {
            //this hace referencia a la instancia actual
            //es una forma de representar un objeto de la clase, en un momento en particular
            this.nombre = nombre;
            this.vida = vida;
            this.ataque = ataque;
            this.defensa = defensa;
            this.esShinny = esShinny;
        }
        #endregion

        #region Metodos
        // METODOS
        //la mayoria de los metodos son publicos
        // si es privado, es interno de la clase y lo voy a llamar desde otro metodo de la clase
        // no va a ser parte de la interfaz del objeto


        //1er metodo: mostrar datos
        //hay que hacer este metodo porq los atributos son privados y no puedo verlos desde afuera.

        public string MostrarPokemon() //no recibe nada pero retorna string
        {
            //string mensaje = string.Empty;
            //mensaje += "Nombre: " + this.nombre;
            //mensaje += "\nVida: " + this.vida;
            //mensaje += "\nAtaque: " + this.ataque;
            //mensaje += "\nDefensa: " + this.defensa;
            //mensaje += "\nShinny: " + this.esShinny;

            //return mensaje;


            /*string builder 

             vamos a crear un objeto que va a ser el encargado de concatenar todos los demas objetos
             para el procesamiento interno de la clase, este metodo es mas eficiente
             */

            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Nombre: " + this.nombre);
            sb.AppendLine("\nVida: " + this.vida);
            sb.AppendLine("\nAtaque: " + this.ataque);
            sb.AppendLine("\nDefensa: " + this.defensa);
            sb.AppendLine("\nShinny: " + this.esShinny);

            return sb.ToString();
        }

        public void RecargarVida(int vida)
        {
            this.vida += vida;
        }

        /// <summary>
        /// permite que un pokemon ataque a otro
        /// </summary>
        /// <param name="pokemonAtaque"></param>
        /// <returns>bool que me indica si pudo atacar o no</returns>
        public bool Atacar(Pokemon pokemonAtaque) // recibe como instancia un pokemon
        {
            bool pudoAtacar = false;
            if (pokemonAtaque != null)
            {
                int daño;
                daño = this.ataque - pokemonAtaque.defensa;
                if (daño < 0)
                {
                    pokemonAtaque.vida -= daño;
                    pudoAtacar = true;
                }
            }
            return pudoAtacar;
        }
        #endregion

        #region Getter y Setter

        // MEtodos:
        // GETTER (LECTURA)
        // SETTER (ESCRITURA)

        public void SetNombre(string nombre)
        {
            this.nombre = nombre;
        }

        public string GetNombre()
        {
            return this.nombre;
        }

        // puedo obtener el nombre del atributo a traves del metodo, no del atributo.


        public void SetVida(int vida)
        {
            this.vida += vida;
        }
        #endregion

    }
}

// usar tres barras para documentacion