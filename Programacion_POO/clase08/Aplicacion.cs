using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace clase08
{
    // Es el tipo de dato (reemplaza string, int, etc)
    // Definicion (como si fueran constantes) Juego es el 0, redsocial 1, etc
    public enum TipoAplicacion
    {
        Juego,
        RedSocial,
        Herramienta,
        Otro
    }
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
        }
    }
}
/*
 Entre celular y aplicacion hay una situacion de agregacion.
Un celular se compone de una o mas apps.
Se dibuja como rombo vacio desde app hasta cel
¿El cel podria funcionar sin esas apps? SI

La relacion entre el todo y las partes no es fuerte
podria no exisitr la clase app y el cel seguiria siendo un cel
POR ESO ES UNA AGREGACION

Si el celular no pudiera existir sin apps
La rel se llamaria COMPOSICION
se representa con un rombo pintado
LA REL ENTRE TODO Y PARTES ES FUERTE

-----

 Entre Aplicacion y TIPO hay una relacion
Se llama DEPENDENCIA
se representa flecha punteada

-----

Otras relaciones ej: REALIZACION

--

En los lenguajes orientados a objetos, todo es un objeto.
Al crear un objeto, hay cosas q existen dentro suyo aunq no llas hayamos creado nosotros

 */