import os
from tkinter import Tk, filedialog

# Función para seleccionar una carpeta utilizando Tkinter
def select_folder():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    folder_selected = filedialog.askdirectory()  # Abrir diálogo para seleccionar carpeta
    return folder_selected

# Función para escribir la estructura del directorio en el archivo de salida
def write_directory_tree(root_folder, file_writer):
    for root, dirs, files in os.walk(root_folder):
        # Filtrar directorios que deben ser excluidos
        dirs[:] = [d for d in dirs if not (
            d == '__pycache__' or 
            d == 'migrations' or 
            d.startswith('env') or 
            d.endswith('env')
        )]
        
        level = root.replace(root_folder, '').count(os.sep)
        indent = '│' + ' ' * 4 * level
        sub_indent = '│' + ' ' * 4 * (level + 1)
        folder_name = os.path.basename(root)
        if folder_name:
            file_writer.write('{}├── {}/\n'.format(indent, folder_name))
        
        for i, f in enumerate(files):
            # Filtrar archivos que deben ser excluidos
            if f.endswith('.sqlite3') or f == '.DS_Store' or f == 'manage.py':
                continue
            file_writer.write('{}{}{}\n'.format(sub_indent, '├── ' if i < len(files) - 1 else '└── ', f))

# Función para escribir el contenido de los archivos en el archivo de salida
def write_file_contents(root_folder, file_writer):
    for root, dirs, files in os.walk(root_folder):
        # Filtrar directorios que deben ser excluidos
        dirs[:] = [d for d in dirs if not (
            d == '__pycache__' or 
            d == 'migrations' or 
            d.startswith('env') or 
            d.endswith('env')
        )]
        
        for f in files:
            # Filtrar archivos que deben ser excluidos
            if f.endswith('.sqlite3') or f == '.DS_Store' or f == 'manage.py':
                continue
            
            file_path = os.path.join(root, f)
            file_writer.write(f'**Ruta: {file_path}**\n')
            if f.endswith('.py'):
                file_writer.write('```Python\n')
            else:
                file_writer.write('```\n')
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                file_writer.write(file.read())
            
            file_writer.write('```\n\n')

# Función principal que selecciona la carpeta, genera el archivo de salida y escribe los datos
def main():
    selected_folder = select_folder()
    if not selected_folder:
        print("No se seleccionó ninguna carpeta.")
        return

    output_file_path = os.path.join(selected_folder, 'estructura_de_proyecto.md')

    with open(output_file_path, 'w', encoding='utf-8') as file_writer:
        file_writer.write("# Estructura del Directorio y Contenido de Archivos\n\n")
        file_writer.write("## Estructura del Directorio:\n")
        write_directory_tree(selected_folder, file_writer)
        file_writer.write("\n\n## Contenido de los Archivos:\n")
        write_file_contents(selected_folder, file_writer)

    print(f"Estructura del directorio y contenido de archivos guardados en: {output_file_path}")

if __name__ == "__main__":
    main()
