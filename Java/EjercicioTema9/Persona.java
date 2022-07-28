public  class Persona{
    int edad;
    String nombre;
    int telefono;

    public static class Cliente extends Persona{//hay que poner  static, ya que da error al crear el objeto
        int credito;
    }
    public static class Trabajador extends Persona{
        int salario;
    }

    public static void main(String[] args) {

        Cliente cliente1 = new Cliente();

            cliente1.edad=55;
            cliente1.nombre="Eduardo";
            cliente1.telefono=555555555;
            cliente1.credito=24586589;
        

        System.out.println("El cliente " + cliente1.nombre +" tiene "+ cliente1.edad+" años, su telefono es el "+ cliente1.telefono +" y tiene un credigo de "+cliente1.credito);

        
    }

        //con una interface se solucionaria lo de heredar de una clase varias clases
        //pero como en el enunciando ponde que tiene que ser de una clase dejo comentado el codigo para que no de error


//         Trabajador trabajador1 = new Trabajador();
//         trabajador1.edad=25;
//         trabajador1.nombre="Manolo";
//         trabajador1.telefono=645676134941;
//         trabajador1.salario=2500;

// System.out.println("El trabajador" + trabajador1.nombre +" tiene "+ trabajador1.edad+" años, su telefono es el "+ trabajador1.telefono +" y tiene un salario de "+ trabajador1.salario);


}