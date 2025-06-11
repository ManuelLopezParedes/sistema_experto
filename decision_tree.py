# decision_tree.py

class NodoDecision:
    def __init__(self, pregunta, opciones=None, diagnostico=None):
        """
        Inicializa un nodo del árbol de decisiones.
        
        :param pregunta: Texto o pregunta a mostrar al usuario.
        :param opciones: Diccionario donde las claves son etiquetas (opciones) 
                         y los valores son instancias de NodoDecision.
        :param diagnostico: Valor a retornar (string) cuando el nodo es hoja.
        """
        self.pregunta = pregunta
        self.opciones = opciones or {}
        self.diagnostico = diagnostico

def construir_arbol():
    """
    Construye y retorna un árbol de decisiones multinivel.
    
    Ejemplo de estructura:
      - Nivel 1: Selección de categoría
         * "infecciones respiratorias" → nodo para decisiones respiratorias.
         * "problemas digestivos" → nodo para decisiones digestivas.
      
      - Nivel 2 (para infecciones respiratorias):
         * "gripe tipo b" → retorna "gripe_tipo_b"
         * "gripe tipo c" → retorna "gripe_tipo_c"
      
      - Nivel 2 (para problemas digestivos):
         * "gastritis" → retorna "gastritis"
    
    Nota: Asegúrate de que tu base de conocimientos tenga las claves correspondientes.
    """
    # Nodos hoja para infecciones respiratorias
    nodo_asma = NodoDecision("Has seleccionado Asma", diagnostico="Asma")
    nodo_enfermedad_pulmonar = NodoDecision("Has seleccionado (EPOC)", diagnostico="epoc")
    nodo_resfriado_y_gripe = NodoDecision("Has seleccionado Resfriado y gripe", diagnostico="resfriado_y_gripe")

    # Nodo hoja para un ejemplo del área digestiva
    nodo_ERGE = NodoDecision("Has seleccionado ERGE", diagnostico="erge")
    nodo_gastroenteritis = NodoDecision("Has seleccionado Gastroenteritis", diagnostico="gastroenteritis")
    nodo_sindrome_intestino_irritable = NodoDecision("Has seleccionado Síndrome del intestino irritable", diagnostico="sindrome_intestino_irritable")
    nodo_enfermedad_celiaca = NodoDecision("Has seleccionado Enfermedad celíaca", diagnostico="enfermedad_celiaca")

    # Nodo hoja para enfermedades cardiovasculares
    nodo_hipertension = NodoDecision("Has seleccionado Hipertensión", diagnostico="hipertension")
    nodo_Insuficiencia_cardiaca = NodoDecision("Has seleccionado Insuficiencia cardíaca", diagnostico="Insuficiencia_cardiaca")
    nodo_anemia = NodoDecision("Has seleccionado Anemia", diagnostico="anemia")

    # Nodo hoja para enfermedades endocrinas y metabólicas
    nodo_diabetes = NodoDecision("Has seleccionado Diabetes tipo 2", diagnostico="diabetes_tipo_2")
    nodo_hipertiroidismo = NodoDecision("Has seleccionado Hipertiroidismo", diagnostico="hipertiroidismo")
    nodo_hipotiroidismo = NodoDecision("Has seleccionado Hipotiroidismo", diagnostico="hipotiroidismo")

    #nodo hoja para enfermedades neurologicas
    nodo_epilepsia = NodoDecision("Has seleccionado Epilepsia", diagnostico="epilepsia")
    nodo_parkinson = NodoDecision("Has seleccionado Parkinson", diagnostico="parkinson")
    nodo_migraña = NodoDecision("Has seleccionado Migraña", diagnostico="migraña")

    #nodo hoja para enfermedades psiquiatricas
    nodo_depresion = NodoDecision("Has seleccionado Depresión", diagnostico="depresion")
    nodo_esquizofrenia = NodoDecision("Has seleccionado Esquizofrenia", diagnostico="esquizofrenia")

    #nodo hoja para enfermedades autoinmunes
    nodo_artritis = NodoDecision("Has seleccionado Artritis reumatoide", diagnostico="artritis_reumatoide")
    nodo_psoriasis = NodoDecision("Has seleccionado Psoriasis", diagnostico="psoriasis")
    nodo_fibromialgia = NodoDecision("Has seleccionado Fibromialgia", diagnostico="fibromialgia")

    # nodo hoja para enfermedades infecciosas
    nodo_hepatitis_viral = NodoDecision("Has seleccionado Hepatitis viral", diagnostico="hepatitis_viral")
    nodo_infeccion_urinaria = NodoDecision("Has seleccionado Infección urinaria", diagnostico="infeccion_urinaria")

    # nodo hoja para enfermedades renales y del sistema urinario
    nodo_insuficiencia_renal_cronica = NodoDecision("Has seleccionado Insuficiencia renal crónica", diagnostico="insuficiencia_renal_cronica")

    # nodo hoja para enfermedades oseas y articulares
    nodo_osteoporosis = NodoDecision("Has seleccionado Osteoporosis", diagnostico="osteoporosis")
    nodo_artritis_reumatoide = NodoDecision("Has seleccionado Artritis reumatoide", diagnostico="artritis_reumatoide")

    # nodo hoja para enfermedades alergicas e inmunologicas
    nodo_alergia = NodoDecision("Has seleccionado Alergias", diagnostico="alergias")
    nodo_conjuntivitis_alergica = NodoDecision("Has seleccionado Conjuntivitis alérgica", diagnostico="conjuntivitis_alergica")

    # Nodo interno para la categoría "Infecciones Respiratorias"
    nodo_respiratorio = NodoDecision(
        "Selecciona un padecimiento respiratorio:",
        opciones={
            "Asma":nodo_asma,
            "Enfermedad Pulmonar Obstructiva Crónica (EPOC)": nodo_enfermedad_pulmonar,
            "Resfriado y gripe": nodo_resfriado_y_gripe,
        }
    )
    
    # Nodo interno para la categoría "Problemas Digestivos"
    nodo_digestivos = NodoDecision(
        "Selecciona un padecimiento digestivo:",
        opciones={
            "Enfermedad de reflujo gastroesofágico (ERGE)": nodo_ERGE,
            "Gastroenteritis": nodo_gastroenteritis,
            "Síndrome del intestino irritable": nodo_sindrome_intestino_irritable,
            "Enfermedad celíaca": nodo_enfermedad_celiaca,
        }
    )

    #nodo interno para la categoría "Enfermedades Cardiovasculares"
    nodo_cardiovascular = NodoDecision(
        "Selecciona un padecimiento cardiovascular:",
        opciones={
            "hipertension": nodo_hipertension,
            "Insuficiencia cardíaca": nodo_Insuficiencia_cardiaca,
            "Anemia": nodo_anemia,
        }
    )

    #nodo interno para la categoría "Enfermedades Endocrinas y Metabólicas"
    nodo_endocrino = NodoDecision(
        "Selecciona un padecimiento endocrino o metabólico:",
        opciones={
            "Diabetes tipo 2": nodo_diabetes,
            "Hipertiroidismo": nodo_hipertiroidismo,
            "Hipotiroidismo": nodo_hipotiroidismo,
        }
    )

    #nodo interno para la categoría "Enfermedades Neurológicas"
    nodo_neurologico = NodoDecision(
        "Selecciona un padecimiento neurológico:",
        opciones={
            "Epilepsia": nodo_epilepsia,
            "Parkinson": nodo_parkinson,
            "Migraña": nodo_migraña,
        }
    )

    #nodo interno para la categoría "Enfermedades Psiquiatricas"
    nodo_psiquiatrico = NodoDecision(
        "Selecciona un padecimiento psiquiátrico:",
        opciones={
            "Depresión y ansiedad": nodo_depresion,
            "Esquizofrenia": nodo_esquizofrenia,
        }
    )

    #nodo interno para la categoría "Enfermedades Autoinmunes"
    nodo_autoinmune = NodoDecision(
        "Selecciona un padecimiento autoinmune:",
        opciones={
            "Artritis reumatoide": nodo_artritis,
            "Psioriasis": nodo_psoriasis,
            "Fibromialgia": nodo_fibromialgia,
        }
    )

    # nodo interno para la categoría "Enfermedades Infecciosas"
    nodo_infeccioso = NodoDecision(
        "Selecciona un padecimiento infeccioso:",
        opciones={
            "Hepatitis viral": nodo_hepatitis_viral,
            "Infeccion urinaria": nodo_infeccion_urinaria,
        }
    )

    # nodo interno para la categoría "Enfermedades Renales y del sistema urinario"
    nodo_renal = NodoDecision(
        "Selecciona un padecimiento renal o del sistema urinario:",
        opciones={
            "Insuficiencia renal crónica": nodo_insuficiencia_renal_cronica,
            "Infeccion urinaria": nodo_infeccion_urinaria,
        }
    )

    # nodo interno para la categoría "Enfermedades Oseas y Articulares"
    nodo_oseo = NodoDecision(
        "Selecciona un padecimiento óseo o articular:",
        opciones={
            "Osteoporosis": nodo_osteoporosis,
            "Artritis reumatoide": nodo_artritis_reumatoide,
        }
    )

    # nodo interno para la categoría "Enfermedades Alergicas e inmunologicas"
    nodo_alergico = NodoDecision(
        "Selecciona un padecimiento alérgico o inmunológico:",
        opciones={
            "Alergias": nodo_alergia,
            "Asma": nodo_asma,
            "Conjuntivitis alérgica": nodo_conjuntivitis_alergica,
        }
    )
    
    # Nodo raíz para elegir la categoría general
    raiz = NodoDecision(
        "Elige la categoría de padecimiento que deseas consultar:",
        opciones={
            "Enfermedades respiratorias": nodo_respiratorio,
            "Enfermedades digestivas": nodo_digestivos,
            "Enfermedades Cadiovasculares y Circulatorias": nodo_cardiovascular,
            "Enfermedades Endocrinas y Metabólicas": nodo_endocrino,
            "Enfermedades Neurológicas": nodo_neurologico,
            "Enfermedades Psiquiatricas": nodo_psiquiatrico,
            "Enfermedades Autoimune": nodo_autoinmune,
            "Enfermedades Infecciosas": nodo_infeccioso,
            "Enfermedades Renales y del sistema urinario": nodo_renal,
            "Enfermedades Oseas y Articulares": nodo_oseo,
            "Enfermedades Alergicas e inmunologicas": nodo_alergico,
        }
    )
    
    return raiz

def navegar_arbol(nodo):
    """
    Recorre el árbol de decisiones de forma recursiva.
    
    Si el nodo es hoja (posee un diagnóstico), retorna ese valor.
    De lo contrario, muestra la pregunta y las opciones numeradas para que el usuario elija.
    
    Retorna el código (diagnóstico) asociado a la opción elegida.
    """
    # Caso base: si el nodo es hoja, retornar el diagnóstico
    if nodo.diagnostico is not None:
        return nodo.diagnostico
    
    # Mostrar la pregunta
    print("\n" + nodo.pregunta)
    opciones = list(nodo.opciones.keys())
    for index, opcion in enumerate(opciones, start=1):
        print(f"{index}. {opcion.capitalize()}")
    
    eleccion = input("Elige una opción (número): ").strip()
    try:
        num = int(eleccion)
        if 1 <= num <= len(opciones):
            clave = opciones[num - 1]
            return navegar_arbol(nodo.opciones[clave])
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
            return navegar_arbol(nodo)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return navegar_arbol(nodo)

def seleccionar_diagnostico():
    """
    Función wrapper que construye el árbol de decisiones y lo recorre para seleccionar un diagnóstico.
    
    Retorna el código del padecimiento seleccionado (por ejemplo, "gripe_tipo_b").
    """
    arbol = construir_arbol()
    return navegar_arbol(arbol)

# Para pruebas independientes, descomenta lo siguiente:
# if __name__ == "__main__":
#     diag = seleccionar_diagnostico()
#     print("\nDiagnóstico seleccionado:", diag)