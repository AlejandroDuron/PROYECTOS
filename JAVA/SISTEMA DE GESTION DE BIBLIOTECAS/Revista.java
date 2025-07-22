package Documentos;

public class Revista extends Documento{
    private String editor;
    private int numeroEdicion;
    private String issn;
    private String periodicidad;

    public Revista(String titulo, String codigo, String editor, int numeroEdicion, String issn, String periodicidad) {
        super(titulo, codigo);
        this.editor = editor;
        this.numeroEdicion = numeroEdicion;
        this.issn = issn;
        this.periodicidad = periodicidad;
    }

    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }

    public int getNumeroEdicion() {
        return numeroEdicion;
    }

    public void setNumeroEdicion(int numeroEdicion) {
        this.numeroEdicion = numeroEdicion;
    }

    public String getIssn() {
        return issn;
    }

    public void setIssn(String issn) {
        this.issn = issn;
    }

    public String getPeriodicidad() {
        return periodicidad;
    }

    public void setPeriodicidad(String periodicidad) {
        this.periodicidad = periodicidad;
    }


    @Override
    public String getTipoDocumento() {
        return "Revista";
    }

    @Override
    public String toString() {
        return  super.toString() +
                "El editor de esta revista es: " + editor +
                "El numero de edicion de la revista es: " + getNumeroEdicion() +
                "El issn de la revista es: " + issn +
                "La periodicidad de la revista es: " + periodicidad;
    }

    @Override
    public int hashCode() { // Usar el issn para el hash
        return issn.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        // Primero verifica si ambos objetos son el mismo (misma referencia en memoria)
        if (this == obj) {
            return true;
        }

        // Llama al metodo equals de la clase base (Documento) para comparar los atributos comunes
        if (!super.equals(obj)) {
            return false;
        }

        // Convierte el objeto recibido a tipo Libro
        Revista otra = (Revista) obj;

        return issn.equals(otra.issn);  // Comparar por issn
    }
}
