namespace Condicionales_Ejercicio13
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
            Daniela Serra
            CONDICIONALES
            Ejercicio 13


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
            string marca;
            int cantidad;
            int PRECIO = 7500;
            double total_sin_desc; // precio * cantidad
            double porcentaje_desc;
            double porcentaje_ingresos_brutos;
            double descuento; // total_sin_desc * porcentaje_desc
            double total_con_desc; // total_sin_desc - descuento
            double ingresos_brutos; // total_con_desc * porcentaje_ingresos_brutos
            double total_a_pagar; // total_con_desc + ingresos_brutos


            Console.WriteLine("¿Qué marca de lamparitas quiere llevar? (ArgentinaLuz, FelipeLamparas, Otra)");
            marca = Console.ReadLine();
            Console.WriteLine("¿Qué cantidad de lamparitas quiere llevar?");
            cantidad = int.Parse(Console.ReadLine());

            total_sin_desc = PRECIO * cantidad;

            // A. Si compra 6 lamparitas o más, tiene un descuento del 50%.
            if (cantidad >= 6)
            {
                porcentaje_desc = 0.5; // total_sin_desc * porcentaje_desc

            }
            // B. Si compra 5 lamparitas marca “ArgentinaLuz” se aplica un 40% 
            // y si es de otra marca, el descuento es del 30 %.
            else if (cantidad == 5 && marca == "ArgentinaLuz")
            {
                porcentaje_desc = 0.4; // total_sin_desc - (total * porcentaje_desc)
            }
            else if (cantidad == 5 && marca != "ArgentinaLuz")
            {
                porcentaje_desc = 0.3; // total - (total * porcentaje_desc)
            }
            // C. Si compra 4 lamparitas marca “ArgentinaLuz” o “FelipeLamparas” 
            // se hace un descuento del 25 %, y si es de otra marca el descuento es del 20 %.
            else if (cantidad == 4 && (marca == "ArgentinaLuz" || marca == "FelipeLamparas"))
            {
                porcentaje_desc = 0.25; // total - (total * porcentaje_desc)
            }
            else if (cantidad == 4 && (marca != "ArgentinaLuz" && marca != "FelipeLamparas"))
            {
                porcentaje_desc = 0.2; // total - (total * porcentaje_desc)
            }
            // D. Si compra 3 lamparitas marca “ArgentinaLuz” el descuento es del 15 %, 
            // si es “FelipeLamparas se hace un descuento del 10 % y si es otra marca, 5 %.
            else if (cantidad == 3 && marca == "ArgentinaLuz")
            {
                porcentaje_desc = 0.15; // total - (total * porcentaje_desc)
            }
            else if (cantidad == 3 && marca == "FelipeLamparas")
            {
                porcentaje_desc = 0.1;
            }
            else if (cantidad == 3 && (marca != "ArgentinaLuz" && marca != "FelipeLamparas"))
            {
                porcentaje_desc = 0.05;
            }
            else
            {
                porcentaje_desc = 0;
            }

            descuento = total_sin_desc * porcentaje_desc;
            total_con_desc = total_sin_desc - descuento;

            // E.Si el importe final con descuento suma más de $10500, se debe agregar
            // el 10 % de ingresos brutos.
            if (total_con_desc > 10500)
            {
                porcentaje_ingresos_brutos = 0.1;
            }
            else
            {
                porcentaje_ingresos_brutos = 0;
            }


            ingresos_brutos = total_con_desc * porcentaje_ingresos_brutos;
            total_a_pagar = total_con_desc + ingresos_brutos;

            /*
            Informar: cantidad de lamparitas, marca, total sin descuento, descuento, 
            total con descuento, y si corresponde total de ingresos brutos y total a pagar.
            */

            Console.WriteLine("\n---------------------------------");
            Console.WriteLine("------- Resumen de Compra -------");
            Console.WriteLine("---------------------------------\n");
            Console.WriteLine($"Cantidad de lamparitas: {cantidad}\n");
            Console.WriteLine($"Marca: {marca}\n");
            Console.WriteLine($"Total sin descuento: ${total_sin_desc}\n");
            Console.WriteLine($"Descuento: ${descuento}\n");
            Console.WriteLine($"Total con descuento: ${total_con_desc}\n");
            if (ingresos_brutos  > 0)
            {
                Console.WriteLine($"Total de ingresos brutos: ${ingresos_brutos}\n");
            }
            Console.WriteLine($"Total a pagar: ${total_a_pagar}\n");
            Console.WriteLine("---------------------------------");
            Console.WriteLine("----- Gracias por su compra -----");
            Console.WriteLine("---------------------------------\n");



        }
    }
}
