namespace clase04
{
    internal class Program
    {
        /* 
             * static void NombreFuncion ()
             * {
             *      
             * }
             Las funciones las programamos dentro de una clase:
                static 
            void = tipo de dato que indica vacio: significa q la fn no devuelve nada
            NombreFuncion = upper cammel case
            () = vacios porq no devuelve nada
            {} = determinan la extensión de la funcion

            */
        static void SumaNumeros()
        {
            int unNumero;
            int otroNumero;
            int suma;

            Console.WriteLine("Ingrese un numero:");
            unNumero = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero:");
            otroNumero = int.Parse(Console.ReadLine());

            suma = unNumero + otroNumero;

            Console.WriteLine(suma);
        }

        static int SumaNumerosIngreso()
        {
            int unNumero;
            int otroNumero;
            int suma;

            Console.WriteLine("Ingrese un numero:");
            unNumero = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero:");
            otroNumero = int.Parse(Console.ReadLine());

            suma = unNumero + otroNumero;

            return suma;
        }
        static int SumaNumerosReturn()
        {
            int unNumero;
            int otroNumero;
            int suma;

            Console.WriteLine("Ingrese un numero:");
            unNumero = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero:");
            otroNumero = int.Parse(Console.ReadLine());

            suma = unNumero + otroNumero;

            return suma;
        }
        


        static void SumaNumerosIngreso(int unNumero, int otroNumero)
        {
            int suma;

            
            suma = unNumero + otroNumero;

            Console.WriteLine(suma);
        }


        static void SumaNumerosIngresoRetorno(int unNumero, int otroNumero)
        {
            int suma;


            suma = unNumero + otroNumero;

            return suma;
        }




        static void Main(string[] args)
        {
            // Funcion 1: no ingresa ni devuelve
            SumaNumeros();

            // Funcion dos: no ingresa, si devuelve
            int resultado;
            resultado = SumaNumerosReturn();
            Console.WriteLine($"La suma es " + resultado);

            // FN 3: ingresa


            int unNumero;
            int otroNumero;

            Console.WriteLine("Ingrese un numero:");
            unNumero = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero:");
            otroNumero = int.Parse(Console.ReadLine());

            SumaNumerosIngreso(unNumero, otroNumero);

            //FN 4: ingresa y retorna

            int unNumero;
            int otroNumero;

            Console.WriteLine("Ingrese un numero:");
            unNumero = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese otro numero:");
            otroNumero = int.Parse(Console.ReadLine());

            SumaNumerosIngreso(unNumero, otroNumero);

            // ingresa y retorna
            SumaNumerosIngresoRetorno(unNumero, otroNumero);


            /* FN pide 5 numeros y retorne promedio */
        }
    }
}
