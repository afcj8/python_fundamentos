def calcular_area_retangulo(largura, *args):
    areas = []
    for alturas in args:
        areas.append(largura * alturas)
        
    return areas

resultado = calcular_area_retangulo(2, 3, 4, 5)
print(resultado)    # [6, 8, 10]