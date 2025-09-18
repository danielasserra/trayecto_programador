namespace FN_ejercicio_promedio
{
    internal class Program
    {
        /* FN pide 5 numeros y retorne promedio */

        //static int promedio (int primerNum, int segundoNum, int tercerNum, int cuartoNum, int quintoNum)
        //{
        //    int suma;
        //    int prom;

        //    suma = primerNum + segundoNum + tercerNum + cuartoNum + quintoNum;

        //    prom = suma / 5;

        //    return prom;

        //}
        static float Promedio()
        {
            float promedio = 0.0f;
            int suma = 0;
            int numero;

            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Ingrese el {i + 1}° número: ");
                numero = int.Parse(Console.ReadLine());
                suma += numero;  
            }

            promedio = (float)suma / 5;
            return promedio;
        }


        static void Main(string[] args)
        {
            //int primerNum;
            //int segundoNum;
            //int tercerNum;
            //int cuartoNum;
            //int quintoNum;

            //Console.WriteLine("Ingrese primer numero: ");
            //primerNum = int.Parse(Console.ReadLine());
            //Console.WriteLine("Ingrese segundo numero: ");
            //segundoNum = int.Parse(Console.ReadLine());
            //Console.WriteLine("Ingrese tercer numero: ");
            //tercerNum = int.Parse(Console.ReadLine());
            //Console.WriteLine("Ingrese cuarto numero: ");
            //cuartoNum = int.Parse(Console.ReadLine());
            //Console.WriteLine("Ingrese quinto numero: ");
            //quintoNum = int.Parse(Console.ReadLine());

            //Console.WriteLine($"El promedio es: " + promedio(primerNum, segundoNum, tercerNum, cuartoNum, quintoNum));
        }
    }
}
