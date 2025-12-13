def remove_null_and_not_numeric(data, aplatir_current=True):
    if isinstance(data, dict):
        resultat = {}
        for k, v in data.items():
            if k == 'current' and isinstance(v, dict) and aplatir_current:
                sous_dict = remove_null_and_not_numeric(v, aplatir_current=False)
                resultat.update(sous_dict)
            else:
                valeur_nettoyee = remove_null_and_not_numeric(v, aplatir_current=False)
                if value_Is_Good(valeur_nettoyee):
                    resultat[k] = valeur_nettoyee
                elif isinstance(valeur_nettoyee, dict) and valeur_nettoyee:
                    resultat[k] = valeur_nettoyee
                elif isinstance(valeur_nettoyee, list) and valeur_nettoyee:
                    resultat[k] = valeur_nettoyee
        
        return resultat
        
    elif isinstance(data, list):
        return [
            remove_null_and_not_numeric(item, aplatir_current=False)
            for item in data
            if value_Is_Good(item) or isinstance(item, (dict, list))
        ]
    else:
        return data
def multiply_value_json(data):
    def extract_value(obj):
        valeurs = []
        if isinstance(obj, dict):
            for valeur in obj.values():
                valeurs.extend(extract_value(valeur))
        elif isinstance(obj, list):
            for element in obj:
                valeurs.extend(extract_value(element))
        elif isinstance(obj, (int, float)):
            valeurs.append(obj)
        return valeurs
    value = extract_value(data)
    if not value:
        return None
    
    resultat = 1
    for valeur in value:
        resultat *= valeur
    
    return resultat

def value_Is_Good(valeur):
    if isinstance(valeur, (int, float)) and not isinstance(valeur, bool):
        return valeur != 0
    return False