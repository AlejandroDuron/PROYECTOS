package Main;

import Biblioteca.Biblioteca;
import Documentos.Libro;
import Documentos.Revista;
import Estudiantes.Estudiante;

import java.util.HashSet;
import java.util.Scanner;

public class SistemaGestionBiblioteca {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Biblioteca biblioteca = new Biblioteca();

        // Creación de nostros los estudiantitos de software
        Estudiante estudiante1 = new Estudiante("Ale", "2024001");
        Estudiante estudiante2 = new Estudiante("Kathleen", "2024002");

        // Crear libros y revistas
        Libro libro1 = new Libro("Cien Años de Soledad", "L001", true, "Gabriel García Márquez", "ISBN001",345);
        Libro libro2 = new Libro("Allá por 1984", "L002", true, "George Orwell", "ISBN002", 678);
        Revista revista1 = new Revista("National Geographic", "R001", "Milli  Jhackuzca", 4,"87625364", "Cada año");

        // Agregar documentos
        biblioteca.agregarDocumento(libro1);
        biblioteca.agregarDocumento(libro2);
        biblioteca.agregarDocumento(revista1);

        boolean ciclo = true;

        while (ciclo) {
            System.out.println("\nMenú sistema de biblioteca Softplaya");
            System.out.println("1. Mostrar todos los libros");
            System.out.println("2. Prestar libro");
            System.out.println("3. Devolver libro");
            System.out.println("4. Mostrar libros prestados");
            System.out.println("5. Buscar libros por autor");
            System.out.println("6. Buscar revistas por editor");
            System.out.println("7. Ver estadísticas de la biblioteca");
            System.out.println("8. Ver libros prestados a un estudiante");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion) {
                case 1:
                    biblioteca.imprimirTodosLosDocumentos();
                    break;
                case 2:
                    System.out.print("Código del libro a prestar: ");
                    String codPrestamo = sc.nextLine();
                    System.out.print("ID del estudiante  ");
                    String idPrestamo = sc.nextLine();
                    Estudiante estP = idPrestamo.equals("001") ? estudiante1 : estudiante2;
                    if (biblioteca.prestarDocumento(codPrestamo, estP)) {
                        System.out.println("Libro prestado con éxito.");
                    } else {
                        System.out.println("No se pudo prestar el libro.");
                    }
                    break;
                case 3:
                    System.out.print("Código del libro a devolver: ");
                    String codDevolucion = sc.nextLine();
                    if (biblioteca.devolverDocumento(codDevolucion)) {
                        System.out.println("Libro documento con éxito.");
                    } else {
                        System.out.println("No se pudo devolver el documento.");
                    }
                    break;
                case 4:
                    biblioteca.imprimirDocumentosPrestados();
                    break;
                case 5:
                    System.out.print("Autor a buscar: ");
                    String autor = sc.nextLine();
                    HashSet<Libro> libros = biblioteca.encontrarLibrosPorAutor(autor);
                    if (libros.isEmpty()) {
                        System.out.println("No se encontraron libros de ese autor.");
                    } else {
                        libros.forEach(System.out::println);
                    }
                    break;
                case 6:
                    System.out.print("Editor a buscar: ");
                    String editor = sc.nextLine();
                    HashSet<Revista> revistas = biblioteca.encontrarRevistasPorEditor(editor);
                    if (revistas.isEmpty()) {
                        System.out.println("No se encontraron revistas de ese editor.");
                    } else {
                        revistas.forEach(System.out::println);
                    }
                    break;
                case 7:
                    biblioteca.imprimirEstadisticas();
                    break;
                case 8:
                    System.out.print("ID del estudiante: ");
                    String idEst = sc.nextLine();
                    Estudiante estD = idEst.equals("001") ? estudiante1 : estudiante2;
                    HashSet<Documentos.Documento> prestados = biblioteca.encontrarDocumentosPrestadosA(estD);
                    if (prestados.isEmpty()) {
                        System.out.println("El estudiante no tiene documentos prestados.");
                    } else {
                        prestados.forEach(System.out::println);
                    }
                    break;
                case 0:
                    ciclo = false;
                    break;
                default:
                    System.out.println("Opción inválida.");
            }
        }
        sc.close();
        System.out.println("Sistema finalizado.");
    }
}