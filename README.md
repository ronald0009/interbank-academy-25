# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI) - Ronald Alarcon

## Introducción

Este proyecto tiene como objetivo desarrollar una herramienta de línea de comandos (CLI) en Python para procesar un archivo CSV con transacciones financieras. El programa calcula el saldo final de una cuenta, identifica la transacción de mayor valor (solo créditos) y clasifica las transacciones en créditos y débitos.

El reto consiste en manejar adecuadamente los datos de transacciones, aplicar la lógica financiera adecuada, y proporcionar un reporte claro y útil para el usuario.

## Instrucciones de Ejecución

### Requisitos
Este proyecto está basado en Python. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo con el siguiente comando:

```bash
python --version
```

### Instalación de Dependencias

Este proyecto no tiene dependencias externas más allá de las bibliotecas estándar de Python (`csv`, `argparse`, `unicodedata`). Por lo tanto, no es necesario instalar ningún paquete adicional.

### Ejecución del Programa

1. Clona el repositorio a tu máquina local:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2. Ejecuta el script pasando el archivo CSV con las transacciones como argumento. El archivo debe tener los encabezados `id`, `tipo` y `monto`.

    ```bash
    python procesar_transacciones.py ruta_al_archivo.csv
    ```

3. El programa mostrará el saldo final, la transacción con el mayor monto (solo créditos), y el total de créditos y débitos.

## Enfoque y Solución

La solución implementada se basa en procesar un archivo CSV de transacciones financieras. Los pasos principales son:

1. **Leer el archivo CSV**: Se utiliza `csv.DictReader` para leer el archivo y convertir cada fila en un diccionario.
2. **Procesar las transacciones**:
   - Se identifican las transacciones de tipo **"credito"** y **"debito"**.
   - Se calculan el saldo final sumando los créditos y restando los débitos.
   - Se busca la transacción con el mayor monto, considerando solo los créditos.
3. **Salida del programa**: Al final, se muestra el saldo final, la transacción con el monto más alto y los totales de créditos y débitos.

### Decisiones de Diseño:
- Se decidió ignorar las transacciones de tipo **débitos** al buscar la transacción con el mayor monto, ya que se asumió que el máximo se refiera solo a créditos.
- Se incluyó un paso para **eliminar acentos** en los valores de las transacciones para garantizar una comparación insensible a acentos y tildes, particularmente en idiomas como el español.
  
## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos y carpetas:

```
/procesar_transacciones.py      # Script principal que procesa el archivo CSV y genera el reporte
README.md                      # Este archivo con las instrucciones y detalles del proyecto
```

### Descripción de los Archivos:

- **`procesar_transacciones.py`**: El script que contiene la lógica para procesar el archivo CSV y generar el reporte de transacciones.
- **`README.md`**: Documento con la descripción del proyecto, instrucciones de ejecución, enfoque y solución.
