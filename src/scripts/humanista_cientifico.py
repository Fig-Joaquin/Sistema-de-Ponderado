import json

nota_promedio = None

def load_nem_scores():
    """Carga los puntajes NEM desde un archivo JSON."""
    with open('./files/nem_humanista-cientifico.json', 'r') as file:
        return json.load(file)

def get_nem_score(nota_nem, puntaje_nota):
    """Devuelve el puntaje NEM para una nota dada."""
    # Convertimos la nota a string, como en el JSON
    puntaje_nota = str(puntaje_nota)
    if puntaje_nota in nota_nem:
        return nota_nem[puntaje_nota]
    else:
        return "Nota no encontrada"

def main(nota_promedio):
    nota_nem = load_nem_scores()
    # Puedes cambiar este valor por cualquier otro para hacer la prueba
    grade = nota_promedio
    puntaje = get_nem_score(nota_nem, grade)
    #print(f"El puntaje NEM para la nota {puntaje_nota} es: {puntaje}")
    return puntaje

if __name__ == "__main__": 
    main(nota_promedio)
