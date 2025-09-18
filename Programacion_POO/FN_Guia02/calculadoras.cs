namespace FN_Guia02
{
    internal class calculadoras
    {
        // Hacer una calculadora con funciones para sumar, restar, multiplicar
        // y dividir dos números (verificar la división por cero).

        static float suma(float primerNumero, float segundoNumero)
        {
            return primerNumero + segundoNumero;
        }

        static float resta(float primerNumero, float segundoNumero)
        {
            return primerNumero - segundoNumero;
        }

        static float multiplicacion(float primerNumero, float segundoNumero)
        {
            return primerNumero * segundoNumero;
        }

        static float division(float primerNumero, float segundoNumero)
        {
            return primerNumero / segundoNumero;
        }

        static void calculadora()
        {

            int opcion;
            float primerNumero;
            float segundoNumero;

            do
            {
                Console.WriteLine("-----------------");
                Console.WriteLine("-- Calculadora --");
                Console.WriteLine("-----------------");
                Console.WriteLine("1. Suma");
                Console.WriteLine("2. Resta");
                Console.WriteLine("3. Multiplicación");
                Console.WriteLine("4. Division");
                Console.WriteLine("5. Salir");

                Console.WriteLine("Seleccione una opción: ");
                opcion = int.Parse(Console.ReadLine());

                if (opcion >= 1 && opcion <= 4)
                {

                    Console.WriteLine("Ingrese el primer numero: ");
                    primerNumero = float.Parse(Console.ReadLine());
                    Console.WriteLine("Ingrese el segundo numero: ");
                    segundoNumero = float.Parse(Console.ReadLine());

                    switch (opcion)
                    {
                        case 1:
                            Console.WriteLine($"Resultado suma: " + suma(primerNumero, segundoNumero));
                            break;
                        case 2:
                            Console.WriteLine($"Resultado resta: " + resta(primerNumero, segundoNumero));
                            break;
                        case 3:
                            Console.WriteLine($"Resultado multiplicacion: " + multiplicacion(primerNumero, segundoNumero));
                            break;
                        case 4:
                            while (segundoNumero == 0)
                            {
                                Console.WriteLine("Error. No se puede dividir por cero");
                                Console.WriteLine("Ingrese otro numero");
                                segundoNumero = float.Parse(Console.ReadLine());
                            }
                            Console.WriteLine($"Resultado division: " + division(primerNumero, segundoNumero));
                            break;

                    }
                }
                else if (opcion != 5)
                {
                    Console.WriteLine("Opción no válida. Intente nuevamente.");
                }
            } while (opcion != 5);

            Console.WriteLine("Saliendo...");
            Console.WriteLine("Gracias por utilizar la calculadora");

        }


        static void Main(string[] args)
        {

            calculadora();

        }
    }
}