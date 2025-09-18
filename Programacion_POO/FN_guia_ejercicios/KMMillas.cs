namespace FN_guia_ejercicios
{
    internal class KMMillas
    {
        // Crear una función que convierta kilómetros a millas.
        
        const float MILLA = 0.621371f;
        static float KilometrosAMillas(float km)
        {
            
            return (km * MILLA);

        }
        static void Main(string[] args)
        {
            float km;
            Console.WriteLine("Ingrese la cantidad de kilómetros: ");
            km = float.Parse(Console.ReadLine());
            Console.WriteLine(km + " kilómetros equivalen a " + KilometrosAMillas(km));
        }
    }
}
