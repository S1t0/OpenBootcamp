public class Main {
    public static void main(String[] args) {
        //USANDO IF
        int numeroIf=-35;
        if(numeroIf<0){
            System.out.println("El numero "+numeroIf+ " es negativo");
        }else{
            System.out.println("l numero "+numeroIf+ " es positivo");
        }
        //USNADO WHILE
        int numeroWhile=0;

        while(numeroWhile<3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        //USANDO DO WHILE
        int numerowhile=3;
        do{
            System.out.println("Bucle dowhile" + numerowhile);
        }
        while(numerowhile<3);

        //USANDO FOR

        int numeroFor=0;
        for(int i=numeroFor;i<=3;i++){
            System.out.println("Bucle for " + i);
        }

        String estacion="MAYO";

        switch(estacion){
            case "DICIEMBRE":
            case "ENERO":
            case "FEBRERO":
            System.out.println("Estamos en Invierno");
            break;
            case "MARZO":
            case "ABRIL":
            case "MAYO":
            System.out.println("Estamos en Primavera");
            break;
            case "JUNIO":
            case "JULIO":
            case "AGOSTO":
            System.out.println("Estamos en Verano");
            break;
            case "SEPTIEMBRE":
            case "OCTUBRE":
            case "NOVIEMBRE":
            System.out.println("Estamos en Otoño");
            break;


        }
}   
}
