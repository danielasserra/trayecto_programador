using System;
using System.Text;

namespace clase08
{
    internal class Celular
    {
        #region Atributos
        private string modelo;
        private string numero;

        private static string marca;
        public static int contador;

        //Necesito conocer cuanta bateria tiene el celular
        private int bateria;

        private bool encendido;

        private int almacenamientoUsado;
        private int almacenamientoTotal;

        private const int minBat = 20;

        private List<aplicacion> aplicaciones;
        #endregion

        #region Propiedades
        /*
         * Las propiedades encapsulan getters y setters
         Las propiedades van a estar configuradas en un mismo esquema.
        No todos los atributos van a tener propiedades, podria no tenerlas (quedar privado siempre)
        O podria tener una exposicion a traves de una propiedad: lectura, escritura o ambas
        Depende del acceso que querramos darle al atributo
         */

        //crear variable publica. nombre distinto al del atributo (upper camel case)
        public int Bateria
        {
            get
            {
                return this.bateria;
            }
            set
            {
                if (value <= 0)
                {
                    this.bateria = 0;
                    this.encendido = false;
                }
                else
                {
                    if (value > 100)
                    {
                        this.bateria = 100;
                    }
                    else
                    {
                        this.bateria = value;
                    }
                }


            }
        }
        public bool Encendido
        {
            get
            {
                return this.encendido;
            }

            set
            {
                if (value == true && this.bateria == 0)
                {
                    this.encendido = false;
                }
                else
                {
                    this.encendido = true;
                }
            }
        }

        public int AlmacenamientoTotal
        {
            get;
            set;
        }
        public int AlmacenamientoUsado
        {
            get
            {
                return almacenamientoUsado;
            }
            set
            {
                if (value < 0)
                {
                    this.almacenamientoUsado = 0;
                }
                if (value > AlmacenamientoTotal)
                {
                    this.almacenamientoUsado = AlmacenamientoTotal;
                }
                else
                {
                    this.almacenamientoUsado = value;
                }
            }

        }

        public int EspacioLibre
        {
            get
            {
                return AlmacenamientoTotal - this.almacenamientoUsado;
            }
        }

        #endregion


        #region Constructores

        // Constructor Parametrizado
        public Celular() //defecto
        {
            contador++; //cant d cel q se crean. Atributo de Clase.
            aplicaciones = new List<aplicacion>(); // crea lista de aplicaciones
        }

        public Celular(string modelo, string numero, int almacenamientoTotal = 128) : this()

        //Llamada explicita al constructor por defecto ":this()"
        // ejecuta el constructor x defecto, crea la lista
        // y despues se ejecuta el cosntructor parametrizado
        {
            this.modelo = modelo;
            this.numero = numero;
            this.almacenamientoTotal = almacenamientoTotal;
            this.Bateria = 100;
            this.Encendido = false;
            this.almacenamientoUsado = 0;



        }

        // Constructor estático
        static Celular()
        {
            marca = "Iphone";
            contador = 0;
        }
        #endregion

        #region Métodos

        public string MostrarCelular()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Marca: {marca}");
            sb.AppendLine($"Modelo: {this.modelo}");
            sb.AppendLine($"Numero: {this.numero}");
            sb.AppendLine($"Bateria: {this.Bateria}");
            sb.AppendLine($"Espacio Libre: {this.EspacioLibre}");
            sb.AppendLine($"Encendido: {this.Encendido}");
            sb.AppendLine($"Almacenamiento Total: {this.AlmacenamientoTotal}");
            sb.AppendLine($"Almacenamiento Usado: {this.AlmacenamientoUsado}");
            sb.AppendLine(MostrarApps());

            return sb.ToString();
        }

        private string MostrarApps()
        {
            // Crear un stringbuilder
            // concatena las apps
            // devuelve un sb

            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Lista de apps instaladas:");
            
            // iteracion para mostrar las apps
            for (int i = 0; i < this.aplicaciones.Count; i++)
            {
                sb.AppendLine(this.aplicaciones[i].MostrarApp());
            }

            /*
            // FOR EACH
            // Simplifica la variable de control (i), contar elementos, etc.
            // Sirve para recorrer una coleccion

            //por cada aplicacion que esta instalada en aplicaciones, mostrame esa app
            foreach (Aplicacion app in this.aplicaciones)
            {
                sb.AppendLine(app.MostrarApp());
            }
            */
            return sb.ToString();
        }

        


        public static bool CompararEstatico(Celular c1, Celular c2)
        {
            // Compara los números de teléfono
            return c1.numero == c2.numero;
        }



        public bool CompararInstancias(Celular otroCelular)
        {
            return Celular.CompararEstatico(this, otroCelular);
        }

        public void MostrarCelular2()
        {
            Console.WriteLine($"Modelo: {modelo}, Número: {numero}, Marca: {marca}");
        }

        public void Encender()
        {
            if (this.Bateria > 0)
            {
                this.Encendido = true;
            }
        }

        public void Apagar()
        {
            this.Encendido = false;
        }

        public void CargarBateria(int porcentaje)
        {
            this.Bateria += porcentaje;
        }

        public bool InstalarApp(int tamaño)
        {
            bool resultado = false;

            if (this.Encendido && this.Bateria > minBat && this.EspacioLibre >= tamaño)
            {
                resultado = true;
                this.almacenamientoUsado += tamaño;
            }

            return resultado;
        }

        public bool InstalarApp(Aplicacion app)
        {
            bool resultado = false;

            if (this.encendido && this.bateria > minBat && this.EspacioLibre >= app.Tamaño)
            {
                resultado = true;
                this.almacenamientoUsado += app.Tamaño;
                this.aplicaciones.Add(app);
            }

            return resultado;
        }
        #endregion


    }
}
