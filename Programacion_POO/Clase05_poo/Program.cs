namespace Clase05_poo
{
    internal class Program
    {
        /*
         * 
         * TEORIA
         * 
         * 
        Paradigma = conjunto de ideas, reglas, herramientas, que nos permiten lograr un objetivo.

        Paradigma orientada a objetos: La forma en la q vamos a encarar el desarrollo de un programa
        es pensando en objetos y como esos objetos interactuan entre sí. Cómo se comunican.

        Hay tecnicas q nos permiten agrupar variables en un concepto. 
        Ej. en bdd Entidad: Alumnos, Empleados, etc. 

        POO se basa en el paradigma de objetos. Por un lado va el paradigma y por otro la programación.
        Paradigma abarca: analisis, programacion, diseño, etc. Un monton de aspectos relacionados con el
        desarrollo de software q no necesariamente es la programación en sí.

        Ej. Programar operaciones de un banco, modelo el concepto de cuenta bancaria (n° de cuenta, saldo,
        transacciones q se realizaron, asociada a un cliente)

        Paradigma: ademas de modelar una entidad (definir cuales van a ser los campos) tambien hay que pensar
        en el comportamiento de ese objeto, de esa entidad).

        En una cuenta puedo depositar, extraer, dar de alta, dar de baja, etc.
        No sólo pensamos en una parte estatica, que son los datos, sino tambien en las acciones.
        ¿Como definimos esas acciones?
        Hasta ahora lo hicimos con funciones
        Las entidades que vamos a definir, no solo van a tener variables sino tambien funciones.
        Ahi cambia el paradigma, del paradigma funcional al orientado a objetos.

        Ej. para mostrar datos de un alumno, definiamos una funcion y esa función los mostraba.
        Ahora lo q vamos a hacer es q el alumno sepa mostrarse.
        Antes creaba una fn y esa fn mostraba un dato.
        Ahora es el dato quien va a ejecutar esa fn.

        Esos datos (ej. n° de cuenta, saldo) los vamos a llamar atributos.
        Y esas acciones que va a realizar una cuenta bancaria, las vamos a denominar comportamiento.
        Entre distintas cuentas puede haber relaciones que se van a llamar colaboraciones.

        Este paradigma de POO se sostienen en cuatro pilares:
        - Encapsulamiento: 
                        Permite a un objeto ocultar al mundo exterior (al resto de los objetos) sus detalles
                    de implementacion. Ej. usuario de TV ¿se como hace la tv para recibir la señal del 
                    control remoto para subir el volumen? NO. Y tampoco me interesa. Como usuario no me importa
                    Ahi surge el concepto de privado / publico.
        - Abstraccion:
                        Clasificar. Distinguir que un objeto es una silla y otro no porque tenemos la capacidad
                     de clasificar. Me permite hacer foco en lo que me interesa. Ej. si tengo que modelar un
                     sistema bancario, me interesa en qué colegio estudió el cliente? NO. Este proceso se 
                    basa en la ignorancia selectiva: voy a ignorar lo que no me importa.

                        Cuando creamos los planos de un sistema, vamos a tener distintos niveles de atracción.
                    Ej. Mapas, graficos, dibujos, fotos, planos, de un mismo objeto.

                    ¿Como aplicamos abstraccion?
                                - Identificar entidades
                                - Definir caracteristicas esenciales de entidad. Atributos (Campos en bdd), Comportamientos
                                - Descartar caracteristicas irrelevantes.

        
                    CLASES 
                            Cuando abstraemos: las caracteristicas y los comportamientos deben estar agrupados, hay 
                    algo que los tiene que contener. La clase será nuestra unidad de trabajo.
                    Clase: descripcion de conjunto de objetos q comparten los mismos atributos, metodos, relaciones y semántica.
                    Clase: molde que me va a permitir crear objetos. En principio pueden ser todos iguales.
                    Ej: galletitas. Son todas iguales, pero puedo decorarlas distinto

                    Clase compuesta por:
                        - atributos (las caracteristicas. Variables (python) Campos (bdd)) 
                                se escriben lower camel case
                                sustantivos
                        - metodos (comportamientos)
                                upper camel case (primer letra de cada palabra en mayuscula)
                                verbos

                RELACIONES
                    ASOCIACION
                    Una persona tiene una mascota.

                    GENERALIZACION: un gato es una mascota

                    DEPENDENCIA: el gato necesita comer para vivir

                SEMANTICA
                    No es lo mismo un banco de plaza que un banco de dinero



        - Herencia:
                        Me permite crear elementos o entidades, que me sirvan de molde para crear otras entidades
                    ej. Puedo tener un cliente pero también puedo tener un cliente premium. El premium toma todas
                    las caracteristicas del clasico pero suma otras. Por ej. En un banco: tiene limite descubierto
                    alto, mientras que un usuario de cuenta corriente no tiene descubierto. La base del cliente es
                    la misma pero despues adopta caracteristicas propias
        - Polimorfismo:
                        Me permite trabajar con una lista de clientes. Lista puede tener clientes de cuenta corriente,
                    de caja de ahorro, vip, etc. Puedo poner todos allí y tratarlos de la misma forma.
      

         
         
         
         ****************************************
        *
        *
        * PRACTICA
        * 
        * 
        * 
        Las clases las podemos crear en el mismo archivo o las podemos definir a parte

        Dentro de una solucion puedo tener varios proyectos,q ue pueden comunicarse entre sí.

        ir a Proyecto (clic derecho) - CLASE.

        Dentro de clase aparecen muchas opciones. Vamos a usar CLASE o interfaz.

        A esa clase le vamos a dar un nombre. Si estamos modelando un alumno, la clase será Alumno.
        No se usa plural, es la entidad Alumno.

        Tiene caracteristicas parecidas a las que se generaban x defecto:
        
        POR DEFECTO
        program dentro de un namespace
        clase program
        metodo (o funcion) main, que es donde empieza el programa.

        MI CLASE
        trae una funcion vacia que nos permitirá crear instancia de un alumno
        los atributos se definen como variables.

        // ATRIBUTOS DE LA CLASE
        string nombre;
        string apellido;
        int dni;
        float nota;

        Vamos a hacer una funcion
        Cuando la funcion está dentro de una clase, se llama METODO
        ya no hablamos de función.

        Los metodos se definen = q fn.
        Ya no vamos a usar el "static".
        directamente 
        void Estudiar {}
        int RendirExamen{}

        Creo el alumno en el Main

        new crea el espacio fisico en memeoria para que se guarde un objeto alumno (para guardar los datos del alumno)

        new Alumno(); (esto se llama CONSTRUCTOR DE LA CLASE)

        si pongo un objeto en Console.WriteLine() me muestra el tipo de objeto (str, int, etc)

        A traves de MiAlumno. tengo que poder ver los datos (nombre,apellido,nota)

        Cuando defino atributos y métodos dentro de una clase, en C# son PRIVADOS. Son locales a la clase.
        No se pueden ver desde afuera de la clase.
        La clase debe ser PUBLIC, no internal para que se pueda ver desde otro lado. 
        Cada atributo debe decir public para que se vea dentro de la clase.

        Por lo general, todos los atributos se ponen en privado.
        De momento, los vamos a poner en publico para poderlos ver.

        los METODOS tambien estan en privado.
        Por lo general, la mayoria de los metodos los ponemos publicos.

        */
        static void Main(string[] args)
        {
            Alumno miAlumno = new Alumno();

            miAlumno.nombre = "Juan";
            miAlumno.dni = 222222;
            miAlumno.apellido = "Ruiz";

            miAlumno.Estudiar();


            Console.WriteLine(miAlumno);
        }
    }
}
