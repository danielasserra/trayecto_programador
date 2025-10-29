using System;
using System.Text;

namespace Empleado
{
    public class Empleado
    {
        string nombre;
        int legajo;
        double salarioBase;

        public Empleado(string nombre, int legajo, double salario)
        {
            this.nombre = nombre;
            this.legajo = legajo;
            this.salarioBase = salario;
        }

        public string Nombre { get => nombre; set => nombre = value; }
        public int Legajo { get => legajo; set => legajo = value; }
        public double SalarioBase { get => salarioBase; set => salarioBase = value; }

        public virtual string MostrarInfo()
        {
            
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"nombre: {nombre}");
            sb.AppendLine($"legajo: {legajo}");
            sb.AppendLine($"salario base: {salarioBase}");

            return sb.ToString();
        }
    }
}
