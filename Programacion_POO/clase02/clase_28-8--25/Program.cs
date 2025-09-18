namespace clase_28_8__25
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*10. Realizar un programa que calcule la superficie de un rectángulo.*/

            int ladoA;
            int ladoB;
            int superficie;

            Console.WriteLine("Ingrese uno de los lados:");
            ladoA = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese el otro lado:");
            ladoB = int.Parse(Console.ReadLine());

            superficie = ladoA * ladoB;
            Console.WriteLine($"La superficie del rectángulo es {superficie}");
        }
    }
}
