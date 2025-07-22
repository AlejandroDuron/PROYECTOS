package Estudiantes;

public class Estudiante {
    private String nombre;
    private String carnet;

    public Estudiante(String nombre, String carnet) {
        this.nombre = nombre;
        this.carnet = carnet;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCarnet() {
        return carnet;
    }

    public void setCarnet(String carnet) {
        this.carnet = carnet;
    }

    @Override
    public String toString() {
        return  "El nombre del estudiante es: " + nombre +
                "El carnet del estudiante es: " + carnet;
    }

    @Override
    public boolean equals(Object obj) {
        // Comparamos si ambos son el mismo objeto
        if (this == obj) {
            return true;
        }

        // Si el objeto es nulo o de diferente clase, no son iguales
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }


        Estudiante otro = (Estudiante) obj;
        return carnet.equals(otro.carnet);  // Comparar por carnet
    }


    @Override
    public int hashCode() {
        return carnet.hashCode();  // Usar el carnet para el hash
    }
}
