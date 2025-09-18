namespace PooEjercicioSmartPen
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Boligrafo boliAzul = new Boligrafo("fino", "azul");
            Boligrafo boliRojo = new Boligrafo("grueso", "rojo");

            Console.WriteLine(boliAzul.Escribir("Este bolígrafo es de color azul y tiene punta fina"));
            Console.WriteLine(boliAzul.Recargar(88));

            Console.WriteLine(boliRojo.Escribir("Este bolígrafo es de color rojo y tiene punta gruesa"));
            Console.WriteLine(boliRojo.Recargar(88));
        }
    }
}
