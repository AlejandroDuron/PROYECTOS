import java.util.Arrays;
import java.util.Scanner;

//Ana y yo somos novios Desde que Ana era pequeña tu y yo somos humanos


public class TextProcessor {
    public static void main(String[] args) {
        String texto = "Ana y Juan miraban el mar desde una ventana";
        Scanner s = new Scanner(System.in);

        int contadorPalabra = 1;
        String palabras[] = texto.split(" ");  //agregamos las palabras a un array eliminando espacios por medio del metodo split


        // Creamos un menu dentro de un bucle para que el usuario pueda acceder a este en cualquier momento
        System.out.println("Bienvenido al sistema de gestión de textos :D");
        while (true){
            System.out.println("Seleccione una opción:");
            System.out.println("1. Contabilizar palabras");
            System.out.println("2. Encontrar la palabra más frecuente ");
            System.out.println("3. Encontrar todas las palabras palíndromas en el texto");
            System.out.println("4. Generar estadísticas de vocales y consonantes");
            System.out.println("5. Invertir cada palabra de 4 letras o más que aparece en el texto");
            System.out.println("6. Salir");
            System.out.println("Opcion: ");

            int opcion = s.nextInt();

            // debemos hacer un bucle que almacene la palabra en una variable

            if (opcion == 1){
                for (int i = 0; i < texto.length(); i++ ){
                   if (texto.charAt(i) == ' ' && !(texto.charAt(i+1) == ' ')){  //Identificamos si no hay doble espacio
                      contadorPalabra ++;
                   }
                }
                System.out.println("Su texto contiene " + contadorPalabra + " palabras");
            }

            if (opcion == 2){
                int maxRepeticiones = 0;
                String palabraMasFrecuente = " ";

                for (int i = 0; i < palabras.length; i++) {
                    if (!palabras[i].equals("0")) { // Evitar contar palabras ya marcadas
                        int contadorRepeticion = 1;

                        for (int j = i + 1; j < palabras.length; j++) {
                            if (palabras[i].equals(palabras[j])) {
                                contadorRepeticion++;
                                palabras[j] = "0"; // Marcamos la palabra como contada
                            }
                        }

                        if (contadorRepeticion > maxRepeticiones) {
                            maxRepeticiones = contadorRepeticion;
                            palabraMasFrecuente = palabras[i];
                        }
                    }
                }
                System.out.println("La palabra mas frecuente es '" + palabraMasFrecuente + "' con " + maxRepeticiones + " repeticiones");
            }

            // A N A
            // 0 1 2

            if (opcion == 3){

                for (int i = 0; i < palabras.length ; i++) {
                    String palabra = palabras[i].toLowerCase();

                    if (palabra.length() > 2) {    //identificamos que la palabra tenga mas de dos letras

                        String palabraInvertida = "";

                        for (int j = palabra.length() - 1; j >= 0; j--) {
                            palabraInvertida += palabra.charAt(j);   //almacenamos las palabras invertidas para luego compararlas
                        }

                        if (palabra.equals(palabraInvertida)) {
                            System.out.println("Se encontro la palabra " + palabras[i] + ", que es palindroma, y se encuentra en la posicion " + (i+1) + " del texto");

                        }
                    }
                }
            }


            if (opcion == 4) {
                int[] contadorVocales = {0, 0, 0, 0, 0}; // indices: 0 = 'a', 1 = 'e', 2 = 'i', 3 = 'o', 4 = 'u'
                int totalVocales = 0, totalConsonantes = 0;
                char[] vocales = {'a', 'e', 'i', 'o', 'u'};

                texto = texto.toLowerCase();

                for (int i = 0; i < texto.length(); i++) {
                    char caracter = texto.charAt(i);

                    //Verificamos si es una vocal recorriendo el array de vocales
                    boolean esVocal = false;
                    for (int j = 0; j < vocales.length; j++) {
                        if (caracter == vocales[j]) {
                            contadorVocales[j]++;
                            totalVocales++;
                            esVocal = true;
                            break;
                        }
                    }

                    //si no es vocal pero es una letra entonces se considera consonante
                    if (!esVocal && caracter >= 'a' && caracter <= 'z') {
                        totalConsonantes++;
                    }
                }


                System.out.println("Estadisticas de vocales:");
                for (int i = 0; i < vocales.length; i++) {
                    double porcentaje;
                    if (totalVocales > 0) {
                        porcentaje = (contadorVocales[i] * 100.0) / totalVocales;
                    } else {
                        porcentaje = 0;
                    }
                    System.out.println(vocales[i] + ": " + contadorVocales[i] + ", " + porcentaje);
                }
                System.out.println("Total de vocales: " + totalVocales);
                System.out.println("Total de consonantes: " + totalConsonantes);

                //calculamos el ratio vocales/consonantes

                if (totalConsonantes > 0) {
                    double ratio = (double) totalVocales / totalConsonantes;
                    System.out.println("Ratio vocales/consonantes: " + ratio);
                } else {
                    System.out.println("No hay consonantes en el texto.");
                }
            }

            if (opcion == 5){
                for (int i = 0; i < palabras.length; i++) {
                    String palabra = palabras[i];

                    if (palabra.length() >= 4) { //invertimos solo si tiene 4 o mas letras
                        String palabraInvertida = "";

                        for (int j = palabra.length() - 1; j >= 0; j--) {
                            palabraInvertida += palabra.charAt(j);
                        }

                        System.out.print(palabraInvertida + " "); //imprime la palabra invertida
                    } else {
                        System.out.print(palabra + " "); //si no tiene 4 o mas letras se imprime la palabra sin cambios
                    }
                }
                System.out.println(); //salto de linea
            }

            if (opcion == 6){
                System.out.println("Saliendoo.... vuelve pronto");
                break;
            }
        }
    }
}
