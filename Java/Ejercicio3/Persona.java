public class Persona{
    
    private int edad;
    private String nombre;
    private int telefono;
    
    public void setEdad(int edad){
        this.edad=edad;
    }
    public int getEdad(){
        return edad;
    }
    
    public void setNombre(String nombre){
        this.nombre=nombre;
    }
    public String getNombre(){
        return nombre;
    }
    
    public void setTelefono(int telefono){
        this.telefono=telefono;
    }
    public int getTelefono(){
        return telefono;
    }
    
        public static void main(String[] args) {
        
            Persona persona1 = new Persona();
            persona1.setEdad(58);
            persona1.setNombre("Evaristo");
            persona1.setTelefono(658986523);
    
    
            System.out.println(persona1.getNombre()+" tiene " + persona1.getEdad() + " años de edad, su telefono es "+ persona1.getTelefono());
            
     };
    };