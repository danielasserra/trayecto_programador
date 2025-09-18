namespace FN_Guia03
{
    internal class Program
    {
        /* Diseñar una función que calcule el índice
        de masa corporal (IMC) de una persona a partir de su peso y altura.
        El IMC se calcula dividiendo el peso de una persona en kilogramos entre 
        la estatura (altura) en metros, elevada al cuadrado. 
        La fórmula es: IMC = peso (kg) / estatura (m²). 
        Por ejemplo, una persona que pesa 70 kg y mide 1.75 m tiene un IMC de 22.9 (70 / (1.75 * 1.75)).
        */

        static float calculadoraIMC(float peso, float altura)
        {
            return (peso / altura);
        }


        static void Main(string[] args)
        {
            float peso;
            float altura;

            Console.WriteLine("--------------------");
            Console.WriteLine("* Calculadora IMC *");
            Console.WriteLine("--------------------");

            Console.WriteLine("Ingrese su peso en kilos: ");
            peso = float.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese su altura en metros: ");
            altura = float.Parse(Console.ReadLine());

            Console.WriteLine($"Su IMC es de {calculadoraIMC(peso,altura):0.00}");
        }
    }
}
