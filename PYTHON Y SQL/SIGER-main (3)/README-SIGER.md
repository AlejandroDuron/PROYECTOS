## README | PLATAFORMA DE GESTIÓN DE DATOS | SIGER

El grupo de gestión de datos Kastle ha implementado una plataforma que resolverá todos los inconvenientes con el manejo de data en la empresa: Sistema de Generación y Calidad de Energía SA. de CV. (SIGER).

La plataforma que ha venido a marcar un antes y un después en el mercado de El Salvador. SIGER, podrá gestionar sus datos de una manera eficiente y fugaz.

## Comenzando 🚀
  ### Pre-requisitos 📋

Para la correcta ejecución de la plataforma se necesita que tenga acceso a los siguientes componentes en su entorno virtual. Para el desarrollo de esta plataforma se trabajo con Visual Studio Code, en su última versión lanzada.

Además, incorporar un entorno virtual /vent. y las librerias a utlizar: PyQt6, pymysql, Matplotlib, mariadb. Por otra parte, sería fabuloso si isntala la última versión de mariabd y usa Dbeaver como su gestor con las siguientes credenciales de acceso ---> host: "localhost", user: "root", password: "1234", database: "siger", port: "3306".

```
---Aquí un ejemplo de lo que debe implementar en la terminal de su IDE:
pip install PyQt6
```

### Instalación 🔧

Primero, cargue la base de datos en su gestor de preferencia. Por motivos de optimización e implementación, nuestro grupo de desarrollo KASTLE lo realizó en Dbeaver.

El archivo será Script_DB_SIGER.sql (lo encontrará en el .zip)
```
Script_DB_SIGER.sql
```

Luego, ingrese al entorno virtual que desee. Al igual, KASTLE, por motivos prácticos, decidió utilizar VS. Estando dentro de su IDE abra la carpeta "SIGEREntregaFinalGrupoKASTLE"

```
SIGEREntregaFinalGrupoKASTLE
```

Incorpore todas las librerias, anteriormente mencionadas, y deje fluir su instalación.

Estando en su IDE y con los archivos listos, ejecute el archivo: "login_principal.py".
Este le permitirá inicializar la plataforma y loggearse con las credenciales que le corresponden.
Por motivos practicos, puede ingresar con ----> user: admin1, password: 1234. Automaticamente, se cargará la pantalla menú donde podrá visualizar o editar los datos que maneja su empresa. La ventaja de que la platafroma esté enlazada con la base de datos facilita que los cambios realizados en la plataforma se visualicen, efectivamente, en la base de datos de SIGER.

## Ejecutando las pruebas ⚙️

En el menú, seleccioné cualquier acción que desee visualizar o modificar. Por ejemplo, si selecciona "Clientes podrá acceder al CRUD de está tabla. Además, si deseea agregar un cliente nuevo se cargará un formulario para su respectivo registro. En todo caso, puede cancelar la acción y volver al menú con su respectivo boton.

### Analizando las pruebas end-to-end 🔩

Nos permitió una correcta modularización entre la plataforma y la base de datos de la empresa.

```
llenado de formulario ----> carga inmediata a la BD.
```

### Estilo de codificación ⌨️

Se realizó con un estilo de MVC (modelo, vista, controlador) para una mayor organización y limpieza de trabajo. 

```
SIGER/
├── App/
│   ├── controlador/       # Lógica de la plataforma
│   ├── modelo/            # Acceso a los datos y conexión BD
│   ├── vista/             # Interfaces gráficas UX/UI
```


## Terminos y condiciones de KASTLE 🖇️

KASTLE no se hace responsable por cualquier error en la modularización de esta plataforma. Ya que tenemos al profe mas crack del país impartiendonos DAI.
Además, fue divertido integrar cada uno de los archivos de este proyecto. Nos llevamos un aprendizaje enorme de esta materia y esperamos que nos impulse a motivarnos en proyectos similares. 

PD: Si en nuestras PCs corría, no existe viento, lluvia o mala señal que lo impida en la del profe Alvin.

## Versionado 📌

Usamos github para el versionado. Para todas las versiones disponibles, mira los detalles en: https://github.com/EsmeMejia29/SIGER.git


## Autores ✒️
El grupo KASTLE se conforma por estas grandes mentes intelectuales que no pierden ningún desafio y siempre buscan la excelencia:

Kathleen Abigail Argueta Gómez - PM
Alejandro Javier Durón Rodriguez - RRHH Manager
Kevin Elías Luna Palacios - Finance Manager
Lorena Esmeralda Mejía Ramos -  Full Stack developer
Sheyla Alexandra Sarmiento Aragón - BI Manager

## Licencia 📄

Este proyecto está bajo la Licencia de KASTLE y no puede ser plageado por terceros al equipo organizador de este increible proyecto.
