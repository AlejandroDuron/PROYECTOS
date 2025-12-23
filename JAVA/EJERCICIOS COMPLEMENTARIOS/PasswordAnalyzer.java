import java.util.Scanner;

public class PasswordAnalyzer {
    public static void main(String[] args) {
        // Primero me gustaría solicitarle el nombre de usuario (tipo App) al usuario
        // para que sea más amigable
        Scanner scanner = new Scanner(System.in);
        String nombreDeUsuario;

        // Me aseguro de que el usuario ingrese un nombre válido.
        do {
            System.out.println("¡Hola! Ingrese su nombre de usuario por favor: ");
            nombreDeUsuario = scanner.nextLine().trim();

            if (nombreDeUsuario.isEmpty()) { // El metodo is.empty evita cadenas vacías
                System.out.println("⚠️ El nombre de usuario no puede estar vacío. Inténtelo de nuevo.");
            }
        } while (nombreDeUsuario.isEmpty());

        // Aquí comienza el sistema, pidiendo al usuario que ingrese una contraseña.
        String contrasena;
        do {
            System.out.println("¡Bienvenido, " + nombreDeUsuario + "! Ingrese la contraseña que desea analizar: ");
            contrasena = scanner.nextLine().trim();

            if (contrasena.isEmpty()) {
                System.out.println("⚠️ La contraseña no puede estar vacía. Inténtelo de nuevo.");
            }
        } while (contrasena.isEmpty());

        // Contador para evaluar la contraseña.
        int puntuacionContrasena = 0;

        // Booleanos para verificar que se cumplan las condiciones para que la contraseña sea válida.
        boolean tieneLongitud = contrasena.length() >= 8;
        boolean tieneMayuscula = false;
        boolean tieneMinuscula = false;
        boolean tieneNumero = false;
        boolean tieneCaracterEspecial = false;

        // Defino los caracteres especiales permitidos
        String caracteresEspeciales = "!@#$%^&*()_+-=[]{}|;:,.<>?";

        // Recorre la contraseña una sola vez para verificar todos los criterios
        for (char c : contrasena.toCharArray()) {
            if (Character.isUpperCase(c)) {
                tieneMayuscula = true;
            } else if (Character.isLowerCase(c)) {
                tieneMinuscula = true;
            } else if (Character.isDigit(c)) {
                tieneNumero = true;
            } else if (caracteresEspeciales.indexOf(c) != -1) {
                tieneCaracterEspecial = true;
            }
        }

        // Contar cuántos criterios se cumplen.
        if (tieneLongitud)
            puntuacionContrasena++;
        if (tieneMayuscula)
            puntuacionContrasena++;
        if (tieneMinuscula)
            puntuacionContrasena++;
        if (tieneNumero)
            puntuacionContrasena++;
        if (tieneCaracterEspecial)
            puntuacionContrasena++;

        // Le informo al usuario cuál es la puntuación de su contraseña.
        System.out.println("Su contraseña cumple " + puntuacionContrasena + " criterios.");

        // Brindo el mensaje de retroalimentación.
        String retroalimentacion = "";

        if (puntuacionContrasena == 5) {
            retroalimentacion = "✅ La contraseña proporcionada es de tipo fuerte.";
        } else if (puntuacionContrasena >= 3) {
            retroalimentacion = "⚠️ La contraseña proporcionada es de tipo media. Podría asegurarla más para mayor privacidad.";
        } else {
            retroalimentacion = "❌ La contraseña ingresada es de tipo débil. Debe mejorarla para mayor seguridad.";
        }

        // Finalmente imprimo las condiciones de mejora.
        if (!tieneLongitud)
            retroalimentacion += "Agregue más caracteres a su contraseña.";
        if (!tieneMayuscula)
            retroalimentacion += "Incluya al menos una letra mayúscula.";
        if (!tieneMinuscula)
            retroalimentacion += "Incluya al menos una letra minúscula.";
        if (!tieneNumero)
            retroalimentacion += "Agregue al menos un número.";
        if (!tieneCaracterEspecial)
            retroalimentacion += "Use al menos un carácter especial.";

        System.out.println(retroalimentacion);

        // Mensaje de despedida
        System.out.println("Gracias por utilizar el analizador de contraseñas, " + nombreDeUsuario + ". ¡Que tenga un gran día! 🌟");

    }
}