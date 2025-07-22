package Documentos;

public abstract class Documento {
    private String titulo;
    private String codigo;
    private boolean disponible;

    public abstract String getTipoDocumento();

    public Documento(String titulo, String codigo) {
        this.titulo = titulo;
        this.codigo = codigo;
        disponible = true;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public boolean isDisponible() {
        return disponible;
    }


    @Override
    public String toString() {
        return  "El titulo del documento es: " + titulo +
                "Su estado de disponibilidad es: " + disponible;
    }

    @Override
    public boolean equals(Object obj) {
        // Comparamos si ambos objetos son el mismo en memoria (misma referencia)
        if (this == obj) {
            return true;
        }

        // Verificamos si el objeto es nulo, si lo es no puede ser igual
        if (obj == null) {
            return false;
        }

        // Comprobamos si los objetos son de la misma clase
        if (getClass() != obj.getClass()) {
            return false;
        }

        // Convertimos el objeto recibido a tipo Documento para acceder a sus atributos
        Documento otro = (Documento) obj;

        // Comparamos los códigos de ambos documentos
        return codigo.equals(otro.codigo);  // Comparar por codigo
    }

    @Override
    public int hashCode() {
        return codigo.hashCode(); // Usar el código para el hash
    }
}
