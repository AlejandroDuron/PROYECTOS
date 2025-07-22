package Biblioteca;

import Documentos.*;
import Estudiantes.*;

import java.util.HashMap;
import java.util.HashSet;

public class Biblioteca {
    // Colección de documentos en la biblioteca
    private final HashSet<Documento> documentos;
    // Registra qué documento está prestado a qué estudiante, usando el código del documento
    private final HashMap<String, Estudiante> registrosPrestamos;

    // Constructor de la biblioteca
    public Biblioteca() {
        // Inicializa las colecciones
        documentos = new HashSet<>();
        registrosPrestamos = new HashMap<>();
    }

    // Añadir un nuevo documento a la colección
    public void agregarDocumento(Documento documento) {
        // Añade el documento al conjunto de documentos
        documentos.add(documento);
    }

    // Eliminar un documento de la colección por su código
    public boolean eliminarDocumento(String codigo) {
        // Recorre los documentos y elimina el que coincida con el código
        for (Documento documento : documentos) {
            if (documento.getCodigo().equals(codigo)) {
                documentos.remove(documento);
                return true; // Documento eliminado con éxito
            }
        }
        return false; // Documento no encontrado
    }

    // Prestar un documento a un estudiante
    public boolean prestarDocumento(String codigo, Estudiante estudiante) {
        // Verifica si el documento existe y está disponible
        for (Documento documento : documentos) {
            if (documento.getCodigo().equals(codigo) && documento.isDisponible()) {
                // Marca el documento como no disponible y lo registra como prestado
                documento.setDisponible(false);
                registrosPrestamos.put(codigo, estudiante);
                return true; // Documento prestado con éxito
            }
        }
        return false; // Documento no disponible o no encontrado
    }

    // Devolver un documento prestado

    public boolean devolverDocumento(String codigo) {
        // Verifica si el documento está prestado
        if (registrosPrestamos.containsKey(codigo)) {
            // Elimina el registro de préstamo
            registrosPrestamos.remove(codigo);
            // Marca el documento como disponible
            for (Documento documento : documentos) {
                if (documento.getCodigo().equals(codigo)) {
                    documento.setDisponible(true);
                    return true; // Documento devuelto con éxito
                }
            }
        }
        return false; // Documento no prestado o no encontrado
    }

    // Encontrar todos los documentos prestados a un estudiante

    public HashSet<Documento> encontrarDocumentosPrestadosA(Estudiante estudiante) {
        // Crea un conjunto para almacenar los documentos prestados
        HashSet<Documento> documentosPrestados = new HashSet<>();
        // Recorre los registros de préstamos
        for (String codigo : registrosPrestamos.keySet()) {
            if (registrosPrestamos.get(codigo).equals(estudiante)) {
                // Añade el documento al conjunto si el estudiante tiene este documento prestado
                for (Documento documento : documentos) {
                    if (documento.getCodigo().equals(codigo)) {
                        documentosPrestados.add(documento);
                    }
                }
            }
        }
        return documentosPrestados; // Devuelve el conjunto de documentos prestados
    }

    // Encontrar todos los libros de un autor específico
    public HashSet<Libro> encontrarLibrosPorAutor(String autor) {
        // Crea un conjunto para los libros del autor
        HashSet<Libro> librosPorAutor = new HashSet<>();
        // Recorre los documentos y filtra los libros por autor

        for (Documento documento : documentos) {
            if (documento instanceof Libro) {
                Libro libro = (Libro) documento;
                if (libro.getAutor().equals(autor)) {
                    librosPorAutor.add(libro); // Añade el libro al conjunto
                }
            }
        }
        return librosPorAutor; // Devuelve el conjunto de libros del autor
    }

    // Encontrar todas las revistas de un editor específico
    public HashSet<Revista> encontrarRevistasPorEditor(String editor) {
        // Crea un conjunto para las revistas del editor
        HashSet<Revista> revistasPorEditor = new HashSet<>();
        // Recorre los documentos y filtra las revistas por editor

        for (Documento documento : documentos) {
            if (documento instanceof Revista) {
                Revista revista = (Revista) documento;
                if (revista.getEditor().equals(editor)) {
                    revistasPorEditor.add(revista); // Añade la revista al conjunto
                }
            }
        }
        return revistasPorEditor; // Devuelve el conjunto de revistas del editor
    }

    // Imprimir todos los documentos en la biblioteca
    public void imprimirTodosLosDocumentos() {
        // Recorre y imprime los detalles de todos los documentos
        for (Documento documento : documentos) {
            System.out.println(documento);
        }
    }

    // Imprimir todos los documentos prestados y quién los tomó prestados
    public void imprimirDocumentosPrestados() {
        // Recorre los registros de préstamos e imprime los documentos y los estudiantes
        for (String codigo : registrosPrestamos.keySet()) {
            Estudiante estudiante = registrosPrestamos.get(codigo);
            for (Documento documento : documentos) {
                if (documento.getCodigo().equals(codigo)) {
                    System.out.println("Documento: " + documento + " - Estudiante: " + estudiante);
                }
            }
        }
    }

    // Imprimir estadísticas de la biblioteca
    public void imprimirEstadisticas() {
        // Calcula estadísticas de la biblioteca
        int totalDocumentos = documentos.size();
        int totalLibros = 0;
        int totalRevistas = 0;
        int documentosPrestados = registrosPrestamos.size();
        int documentosDisponibles = totalDocumentos - documentosPrestados;

        // Recorre los documentos para contar libros y revistas
        for (Documento documento : documentos) {
            if (documento instanceof Libro) {
                totalLibros++;
            } else if (documento instanceof Revista) {
                totalRevistas++;
            }
        }

        // Imprime las estadísticas
        System.out.println("Total de documentos: " + totalDocumentos);
        System.out.println("Total de libros: " + totalLibros);
        System.out.println("Total de revistas: " + totalRevistas);
        System.out.println("Documentos prestados: " + documentosPrestados);
        System.out.println("Documentos disponibles: " + documentosDisponibles);
    }
}


