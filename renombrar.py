"""
🎈 La Fábrica de Sonrisas — Renombrador SEO de imágenes
=======================================================
Ejecuta este script dentro de la carpeta que contiene
tus 4 carpetas de imágenes (decoraciones, eventos, etc.)

USO:
  1. Instala Python si no lo tienes: https://python.org
  2. Pon este archivo en la misma carpeta que tus 4 carpetas de fotos
  3. Abre una terminal en esa carpeta
  4. Escribe:  python renombrar.py
  5. ¡Listo!
"""

import os
import shutil

# ─── CONFIGURACIÓN ────────────────────────────────────────────────
# Nombre base SEO para cada carpeta
CARPETAS = {
    "decoracion cumpleanos webp": "decoracion-cumpleanos-infantil-pozuelo",
    "eventos especiales webp": "evento-especial-infantil-pozuelo",
    "manualidades webp": "taller-manualidades-infantil-pozuelo",
    "instalaciones webp": "sala-fiestas-infantil-pozuelo",
}

# Formatos de imagen que se van a renombrar
EXTENSIONES = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".gif", ".bmp"}
# ──────────────────────────────────────────────────────────────────


def normalizar_extension(ext):
    ext = ext.lower()
    if ext in {".jpeg", ".heic", ".heif"}:
        return ".jpg"
    return ext


def renombrar_carpeta(ruta_carpeta, nombre_base, hacer_copia=True):
    archivos = sorted([
        f for f in os.listdir(ruta_carpeta)
        if os.path.splitext(f)[1].lower() in EXTENSIONES
    ])

    if not archivos:
        print(f"  ⚠️  Sin imágenes en: {ruta_carpeta}")
        return 0

    # Crear subcarpeta _renombradas para no tocar los originales
    if hacer_copia:
        salida = os.path.join(ruta_carpeta, "_renombradas")
        os.makedirs(salida, exist_ok=True)
    else:
        salida = ruta_carpeta

    contador = 0
    for i, archivo in enumerate(archivos, start=1):
        ext_original = os.path.splitext(archivo)[1]
        ext_final = normalizar_extension(ext_original)
        nuevo_nombre = f"{nombre_base}-{i:02d}{ext_final}"
        origen = os.path.join(ruta_carpeta, archivo)
        destino = os.path.join(salida, nuevo_nombre)

        if hacer_copia:
            shutil.copy2(origen, destino)
        else:
            os.rename(origen, destino)

        print(f"    {archivo}  →  {nuevo_nombre}")
        contador += 1

    return contador


def main():
    directorio_actual = os.getcwd()
    print("\n🎈 La Fábrica de Sonrisas — Renombrador SEO")
    print("=" * 50)
    print(f"📁 Carpeta raíz: {directorio_actual}\n")

    total = 0
    encontradas = 0

    for nombre_carpeta, nombre_base in CARPETAS.items():
        ruta = os.path.join(directorio_actual, nombre_carpeta)
        if os.path.isdir(ruta):
            encontradas += 1
            print(f"📂 {nombre_carpeta}/")
            n = renombrar_carpeta(ruta, nombre_base, hacer_copia=True)
            total += n
            print(f"   ✅ {n} imágenes renombradas\n")

    if encontradas == 0:
        print("❌ No se encontró ninguna carpeta reconocida.")
        print("   Asegúrate de que este script está en la misma")
        print("   carpeta que tus carpetas de imágenes.\n")
        print("   Carpetas buscadas:")
        for nombre in CARPETAS:
            print(f"     - {nombre}")
    else:
        print("=" * 50)
        print(f"✅ Total: {total} imágenes renombradas")
        print("📁 Las imágenes renombradas están en cada")
        print("   carpeta dentro de la subcarpeta '_renombradas'")
        print("   Los originales NO se han tocado.\n")

    input("Pulsa Enter para cerrar...")


if __name__ == "__main__":
    main()
