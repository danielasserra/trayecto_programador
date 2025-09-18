namespace Programacion_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {

            ///*
            // * CLASE 2

            //******************
            // * CONDICIONALES
            //******************

            // CTRL + KD = para identar
            // CTRL + ALT + CLIC = Escribir a la vez en varios renglones

            // * 10. Realizar un programa que calcule la superficie de un rectángulo.*/

            //int ladoA;
            //int ladoB;
            //int superficie;

            //Console.WriteLine("Ingrese uno de los lados:");
            //ladoA = int.Parse(Console.ReadLine());

            //if (ladoA > 0) {
            //    Console.WriteLine($"El valor ingresado fue {ladoA}");
            //}
            //else {
            //    Console.WriteLine("El valor no es válido");
            //}

            //Console.WriteLine("Ingrese el otro lado:");
            //ladoB = int.Parse(Console.ReadLine());

            //superficie = ladoA * ladoB;
            //Console.WriteLine($"La superficie del rectángulo es {superficie}");


            ///* 
            // ********************** 
            // * OPERADORES LÓGICOS *
            // **********************
            // *
            //        && = AND
            //        || = OR
            // *
            // * Escribe un programa que pregunte al usuario su edad y si tiene 
            // * licencia de conducir. Si la edad es mayor o igual a 18 y tiene licencia de conducir, 
            // * muestra un mensaje que diga "Puedes conducir". De lo contrario, muestra un mensaje que diga "No puedes conducir".*/

            //int edad = 14;
            //bool licencia = false;
            //string mensaje;

            //if (edad >= 18 && licencia)
            //{
            //    mensaje = "puede conducir";

            //}
            //else
            //{
            //    mensaje = "no puede conducir";
            //}
            //Console.WriteLine(mensaje);

            ////--------------------------------------------------------

            ///*
            // Escribe un programa que pregunte al usuario si tiene un título universitario o 
            //si tiene experiencia laboral. Si tiene un título universitario o experiencia laboral, 
            //muestra un mensaje que diga "Eres elegible para el trabajo". De lo contrario, muestra un 
            //mensaje que diga "No eres elegible para el trabajo"
            // */
            //string titulo_universitario;
            //string experiencia_laboral;

            //Console.WriteLine("¿Tenes título universitario?");
            //titulo_universitario = Console.ReadLine();

            //Console.WriteLine("¿Tenes experiencia laboral?");
            //experiencia_laboral = Console.ReadLine();

            //if (titulo_universitario == "si" || experiencia_laboral == "si")
            //{
            //    mensaje = "Sos elegible para el trabajo";
            //}
            //else
            //{
            //    mensaje = "No sos elegible para el trabajo";
            //}

            string color;
            string mensaje;

            Console.WriteLine("ingrese un color:");
            color = Console.ReadLine();


            switch (color)  // switch evalua la variable (es la q esta entre parentesis)
            {
                case "verde":
                    mensaje = "puede pasar";
                    break;

                case "amarillo":
                    mensaje = "precaucion";
                    break;

                case "rojo":
                    mensaje = "no pasar";
                    break;

                default:
                    mensaje = "no corresponde";
                    break;

            }
            Console.WriteLine(mensaje);


            /////////////////////.

            int mes;
            Console.WriteLine("ingrese el mes:");
            mes = int.Parse(Console.ReadLine());

            switch (mes)
            {
                case 12:
                case 1:
                case 2:
                    mensaje = "verano";
                    break;

                case 3:
                case 4:
                case 5:
                    mensaje = "otoño";
                    break;

                case 6:
                case 7:
                case 8:
                    mensaje = "invierno";
                    break;

                case 9:
                case 10:
                case 11:
                    mensaje = "primavera";
                    break;

                default:
                    mensaje = "no corresponde a un mes";
                    break;

            }
            Console.WriteLine(mensaje);

            /*
             
            TAREA:
            Una empresa que se dedica a la comercialización de lámparas de bajo consumo, 
            registra de sus ventas, los siguientes datos: marca y cantidad. 
            El precio de cada lamparita es de $7500 (Sin importar la marca).
            El programa deberá calcular el precio total de la venta, aplicando un descuento 
            si es que corresponde.
            A.      Si compra 6 lamparitas o más, tiene un descuento del 50%.
            B.      Si compra 5 lamparitas marca “ArgentinaLuz” se aplica un 40% 
            y si es de otra marca, el descuento es del 30%.
            C.      Si compra 4 lamparitas marca “ArgentinaLuz” o “FelipeLamparas” 
            se hace un descuento del 25%, y si es de otra marca el descuento es del 20%.
            D.      Si compra 3 lamparitas marca “ArgentinaLuz” el descuento es del 15%, 
            si es “FelipeLamparas se hace un descuento del 10% y si es otra marca, 5%.
            E.       Si el importe final con descuento suma más de $10500, se debe agregar 
            el 10% de ingresos brutos.
            Informar: cantidad de lamparitas, marca, total sin descuento, descuento, 
            total con descuento, y si corresponde total de ingresos brutos y total a pagar.



             */
        }
    }
}
