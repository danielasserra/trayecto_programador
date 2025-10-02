using static System.Net.Mime.MediaTypeNames;

namespace clase08
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Celular c1 = new Celular("Iphtone", "444444");

            c1.Encender();
            c1.InstalarApp("Facebook", 10, EnumTipo.RedSocial);
            
            
            /*
            //Crear app

            Aplicacion app1 = new Aplicacion("Facebook", 10, EnumTipo.RedSocial);
            Aplicacion app2 = new Aplicacion("Calculadora", 10, EnumTipo.Herramienta);
            Aplicacion app3 = new Aplicacion("Call of duty", 10, EnumTipo.Juego);

            // Encender y mostrar cel
            c1.Encender();
            Console.WriteLine(c1.MostrarCelular());
            c1.InstalarApp(app1);

            */


            /*
            // Instalar app
            if (c1.InstalarApp(app1))
            {
                Console.WriteLine("App instalada con exito");
            }
            else
            {
                Console.WriteLine("no hay espacio");
            }
            */


            /*Celular c2 = new Celular("Iphone", "2222222");

            //c2.Bateria = 50;

            c1.Encender();
            c1.CargarBateria(-20);

            Console.WriteLine(c1.MostrarCelular());
            */
        }
    }
}
