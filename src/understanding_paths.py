from pathlib import Path

base = Path(__file__).resolve().parent.parent
print(base)

raw = base / "data" / "raw"
clean = base / "data" / "clean"

"Creacion de las carpetas"
raw.mkdir(parents=True, exist_ok=True)
clean.mkdir(parents=True, exist_ok=True)

#Escribir a un archivo txt
txt_path = raw / "notas.txt"
txt = """
    Los alumnos que van a reprobar son
    todos los que no tienen asistencia
    hoy. Y asi
"""
txt_path.write_text(txt, encoding="utf-8")

contenido = txt_path.read_text(encoding="utf-8")
print(contenido)