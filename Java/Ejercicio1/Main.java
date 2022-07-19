public class Main {

    public static void main(String[] args) {
        int res=suma(5,3,8);
        System.out.println(res);
        Coche miCoche= new Coche();
        System.out.println("El coche tiene " + miCoche.incrementoPuertas() + " puertas");
    }


    public static int suma( int a, int b, int c){
        int resultado=a+b+c;
        return resultado;
    };
}