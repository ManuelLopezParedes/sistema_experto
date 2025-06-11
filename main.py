# main.py
from logic import recomendar_tratamiento
from decision_tree import seleccionar_diagnostico

def main():
    print("=== Sistema de Recomendación de Tratamientos ===")
    
    # Seleccionar el padecimiento mediante la consulta a la base de datos
    codigo_diagnostico = seleccionar_diagnostico()
    if not codigo_diagnostico:
        print("No se seleccionó un diagnóstico válido.")
        return
    
    # Solicitar las condiciones del paciente
    diabetico = input("¿Eres diabético? (si/no): ").strip().lower()
    hipertenso = input("¿Eres hipertenso? (si/no): ").strip().lower()
    
    # (Opcional) Mostrar datos ingresados para depuración
    print(f"\nDiagnóstico seleccionado: {codigo_diagnostico}")
    print(f"Diabético: {diabetico}, Hipertenso: {hipertenso}")
    
    # Obtener las recomendaciones
    resultado = recomendar_tratamiento(codigo_diagnostico, diabetico, hipertenso)
    if "error" in resultado:
        print(resultado["error"])
        return
    
    # Mostrar los resultados
    print(f"\nRecomendaciones para {codigo_diagnostico}:")
    print(f"Descripción: {resultado['diagnostico']}")
    
    print("\n✅ Fármacos recomendados:")
    for f in resultado["farmaceuticos"]:
        print(f"- {f['nombre']}: {f['dosis']}")
        contra = f['contraindicaciones'] if f['contraindicaciones'] else "Ninguna"
        print(f"  Contraindicaciones: {contra}")
    
    print("\n⚠️ Medicamentos riesgosos:")
    if resultado["riesgosos"]:
        for f in resultado["riesgosos"]:
            print(f"- {f['nombre']}")
    else:
        print("Ninguno")
    
    print("\n=== ADVERTENCIA ===")
    print("Consulte a un médico antes de seguir cualquier tratamiento.")
    
    input("\nPresiona Enter para confirmar que has leído las recomendaciones...")

if __name__ == "__main__":
    main()