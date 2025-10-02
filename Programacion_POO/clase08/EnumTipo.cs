namespace Clase08_09_10
{
    public enum TipoAplicacion
    {
        Juego,
        RedSocial,
        Herramienta,
        Otro
    }

    public class Aplicacion
    {
        // Atributos (campos privados)
        private string nombre;
        private int tamaño;
        private TipoAplicacion tipo;

        // Constructor
        public Aplicacion(string nombre, int tamaño, TipoAplicacion tipo)
        {
            this.nombre = nombre;
            this.tamaño = tamaño;
            this.tipo = tipo;
        }

        // Propiedades
        public string Nombre
        {
            get { return nombre; }
        }

        public int Tamaño
        {
            get { return tamaño; }
        }

        public TipoAplicacion Tipo
        {
            get { return tipo; }
        }

        // Método para mostrar info
        public string Mostrar()
        {
            return $"Aplicación: {nombre}, Tamaño: {tamaño} MB, Tipo: {tipo}";
        }
    }
}
