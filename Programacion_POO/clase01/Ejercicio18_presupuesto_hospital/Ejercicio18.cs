namespace Ejercicio18_presupuesto_hospital
{
    internal class Ejercicio18
    {
        static void Main(string[] args)
        {
            /* EJERCITACION
 * 
 * En un hospital existen tres áreas: Cardiología, Pediatría y Traumatología. 
 * El presupuesto anual del hospital se reparte conforme a la siguiente tabla:


    Área        Porcentaje del presupuesto

Cardiología         40%

Pediatría           45%

Traumatología       15%

Necesitamos saber cuánto dinero le corresponde a cada área.	*/


            // Declaracion de Variables
            int cardiologia = 40;
            int pediatria = 45;
            int traumatologia = 15;
            int presupuesto;

            int prespuesto_cardio;
            int prespuesto_pediatria;
            int prespuesto_trauma;

            // Procesos
            Console.WriteLine("Ingrese el presupuesto anual del hospital");
            presupuesto = int.Parse(Console.ReadLine());

            // area*presupuesto/100
            prespuesto_cardio = cardiologia * presupuesto / 100;
            prespuesto_pediatria = pediatria * presupuesto / 100;
            prespuesto_trauma = traumatologia * presupuesto / 100;


            // Salida de datos
            Console.WriteLine($"La cantidad de dinero que le corresponde a cada área es: cardiologia: ${prespuesto_cardio}, pediatría: ${prespuesto_pediatria}, traumatologia: ${prespuesto_trauma}");
        }
    }
}
