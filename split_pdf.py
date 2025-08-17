
import os
import sys
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path):
    """
    Extrae un rango de páginas de un fichero PDF y lo guarda como un nuevo fichero.
    """
    # 1. Validar que el fichero de entrada existe.
    if not os.path.isfile(input_path):
        print(f"Error: El fichero no existe en la ruta indicada: {input_path}")
        sys.exit(1)

    try:
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        print(f"El PDF original tiene {total_pages} páginas.")

        # 2. Pedir al usuario el rango de páginas.
        while True:
            try:
                start_page = int(input(f"Página inicial (1-{total_pages}): "))
                end_page = int(input(f"Página final ({start_page}-{total_pages}): "))
                
                if 1 <= start_page <= end_page <= total_pages:
                    break
                else:
                    print("Error: Rango de páginas inválido. Asegúrate de que 1 <= inicio <= fin <= total_páginas.")
            except ValueError:
                print("Error: Por favor, introduce un número entero válido.")

        # 3. Construir el nombre del fichero de salida.
        directory = os.path.dirname(input_path)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_filename = f"{base_name}_from_{start_page}-{end_page}_pages.pdf"
        output_path = os.path.join(directory, output_filename)

        # 4. Validar que el fichero de salida no exista.
        if os.path.exists(output_path):
            print(f"Error: El fichero de destino ya existe, no se sobreescribirá: {output_path}")
            sys.exit(1)

        # 5. Crear el nuevo PDF con las páginas seleccionadas.
        writer = PdfWriter()
        # Los índices de las páginas en pypdf son base 0, por eso restamos 1.
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        # 6. Guardar el fichero resultante.
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"\n¡Éxito! Se ha creado el fichero:")
        print(output_path)

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # El script espera la ruta completa del fichero como primer argumento.
    if len(sys.argv) < 2:
        print("Uso: python split_pdf.py \"/ruta/completa/al/fichero.pdf\"")
        print("Recuerda usar comillas si la ruta contiene espacios.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    split_pdf(file_path)
