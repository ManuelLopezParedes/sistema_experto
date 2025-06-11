# logic.py

from database import get_padecimientos, get_farmacos

def verificar_contraindicaciones(farmaco):
    """
    Pregunta al usuario si padece alguna de las contraindicaciones del fármaco.
    
    Parámetros:
      - farmaco: Diccionario con la información del fármaco (nombre, dosis, contraindicaciones)
      
    Retorna:
      - True si el usuario NO tiene contraindicaciones.
      - False si el usuario tiene alguna contraindicación.
    """
    contra = farmaco['contraindicaciones']
    if not contra or contra.lower() == "ninguna":
        return True
    
    print(f"\n⚠️ Advertencia para {farmaco['nombre']}:")
    print(f"Contraindicaciones: {contra}")
    respuesta = input("¿Padeces alguna de estas condiciones? (si/no): ").strip().lower()
    
    return respuesta != "si"

def recomendar_tratamiento(codigo_diagnostico, diabetico, hipertenso, alergias=None, medicamentos_actuales=None):
    """
    Genera recomendaciones basadas en el diagnóstico y las condiciones del paciente.
    
    Parámetros:
      - codigo_diagnostico: Código del padecimiento (ej. 'gripe_tipo_b')
      - diabetico: "si" o "no"
      - hipertenso: "si" o "no"
      
    Retorna un diccionario con:
      - 'diagnostico': la descripción del padecimiento
      - 'farmaceuticos': lista de fármacos recomendados (según la condición)
      - 'riesgosos': lista de fármacos con contraindicaciones para el usuario
    """
    # Obtener la información del padecimiento filtrando por código.
    padecimientos = get_padecimientos()
    info = next((p for p in padecimientos if p["codigo"] == codigo_diagnostico), None)
    if info is None:
        return {"error": "Diagnóstico no válido"}
    
    # Selección de categoría: si es diabético se usan los fármacos de 'diabeticos',
    # si es hipertenso, los de 'hipertensos'. Si no cumple ninguno, se utiliza 'diabeticos' por defecto.
    if diabetico.lower() == "si":
        categoria = "diabeticos"
    elif hipertenso.lower() == "si":
        categoria = "hipertensos"
    else:
        categoria = "diabeticos"
    
    farmacos = get_farmacos(codigo_diagnostico, categoria)
    
    # Filtrar fármacos según contraindicaciones
    farmacos_recomendados = []
    farmacos_riesgosos = []
    
    for farmaco in farmacos:
        if verificar_contraindicaciones(farmaco):
            farmacos_recomendados.append(farmaco)
        else:
            farmacos_riesgosos.append(farmaco)
    
    return {
        "diagnostico": info["descripcion"],
        "farmaceuticos": farmacos_recomendados,
        "riesgosos": farmacos_riesgosos    
    }

