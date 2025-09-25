namespace clase08
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Celular c1 = new Celular("Iphtone", "444444");
            Celular c2 = new Celular("Iphone", "2222222");

            //c2.Bateria = 50;

            c1.Encender();
            c1.CargarBateria(-20);

            Console.WriteLine(c1.MostrarCelular());
        }
    }
}
