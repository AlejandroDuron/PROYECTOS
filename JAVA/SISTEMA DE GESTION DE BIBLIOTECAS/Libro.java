package Documentos;

public class Libro extends Documento{
    private String autor;
    private String isbn;
    private int numeroPaginas;

    public Libro(String titulo, String codigo, boolean disponible, String autor, String isbn, int numeroPaginas) {
        super(titulo, codigo);
        this.autor = autor;
        this.isbn = isbn;
        this.numeroPaginas = numeroPaginas;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public int getNumeroPaginas() {
        return numeroPaginas;
    }

    public void setNumeroPaginas(int numeroPaginas) {
        this.numeroPaginas = numeroPaginas;
    }

    @Override
    public String getTipoDocumento() {
        return "Libro";
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
        Libro otro = (Libro) obj;

        return isbn.equals(otro.isbn);  // Comparar por isbn
    }

    @Override
    public int hashCode() {
        return isbn.hashCode(); // Usar isbn para el hash
    }

    @Override
    public String toString() {
        return  super.toString() +
                "El autor del libro es: " + autor +
                "La codigo isbn de este libro es: " + isbn +
                "El numero de paginas de este libro es: " + numeroPaginas;
    }
}
