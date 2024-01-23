lista_tuplas_cafe = [("frapuchino",1900),("capuchino",1200),("expresso lungo",500),("cafe au late",1800)]
def cafe_mas_caro(lista_tuplas_cafe):
    cafe_mais_caro = " "
    precio_mais_caro=0
    for cafe,precio in lista_tuplas_cafe:
        if precio_mais_caro < precio:
            precio_mais_caro = precio
            cafe_mais_caro = cafe
        else:
            pass
    return (cafe_mais_caro,precio_mais_caro)

print(cafe_mas_caro(lista_tuplas_cafe))
            