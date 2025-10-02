namespace clase11
{
    /*
     SOBRECARGA

    Crear metodos que se llaman igual pero reciben distintos parametros
    Realizan distintas cosas segun los parametros que reciben

    Podemos sobrecargar:
    metodos
    cnstructores
    oepradores (aritmentics, relacionales)
    operadores de conversion

    Es una tecnica que permite mejorar la usabilidad y la legibilidad del codigo
    con la sobrecarga podemos REUTILIZAR

    Permite crear metodos con el mismo nombre dentro de la misma clase pero siempre que tengan distintos parámetros.

    EJ
    public int Sumar (num 1, num2)
    public int Sumar (num1, num2, num3)        ------ CANTIDAD parametros, tiene uno mas

    public int Sumar (int num 1, int num2)
    public int Sumar (float num1, float num2)   ---- DISTINTOS tipos de parametros (int float)

    public int Sumar (float num 1, int num2)
    public int Sumar (int num1, float num2)  ------ ORDEN de los parametros

    Mientras mas metodos tengamos con el mismo nombre, mas lento se va a hacer el proceso de ejecucion




     
     */
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
