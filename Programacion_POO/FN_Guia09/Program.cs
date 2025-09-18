namespace FN_Guia09
{
    internal class Program
    {
        // Crear una función que ingrese un monto entero y devuelva el valor del IVA del producto.

        static float CalcularIVA (int monto)
        {
            return (monto * 0.21f);
        }

        static void Main(string[] args)
        {
            int monto;
            Console.WriteLine("Ingrese el monto");
            monto = int.Parse(Console.ReadLine());
            float montoConIVA = CalcularIVA(monto);
            Console.WriteLine("El IVA para el monto ingresado es de: " + montoConIVA);
        }
    }
}
