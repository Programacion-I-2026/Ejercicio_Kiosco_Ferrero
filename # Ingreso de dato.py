 # Ingreso de dato
total_comida = float(input("Ingrese el gasto total en comida: "))
total_bebidas_sin_alcohol = float(input("Ingrese el gasto en bebidas sin alcohol: "))
total_bebidas_con_alcohol = float(input("Ingrese el gasto en bebidas con alcohol: "))

cantidad_invitados = int(input("Ingrese la cantidad total de invitados: "))
cantidad_toman_alcohol = int(input("Ingrese cuántos invitados consumen alcohol: "))

# Validación básica
if cantidad_toman_alcohol > cantidad_invitados:
    print("Error: no puede haber más personas que toman alcohol que invitados.")
else:
    # Cálculos
    costo_comida_por_persona = total_comida / cantidad_invitados
    costo_sin_alcohol_por_persona = total_bebidas_sin_alcohol / cantidad_invitados
    
    if cantidad_toman_alcohol > 0:
        costo_alcohol_por_persona = total_bebidas_con_alcohol / cantidad_toman_alcohol
    else:
        costo_alcohol_por_persona = 0

    # Resultados
    print("\n--- COSTOS ---")
    print("Cada invitado paga (comida + bebida sin alcohol): $", round(costo_comida_por_persona + costo_sin_alcohol_por_persona, 2))
    
    print("\nPersonas que consumen alcohol pagan además: $", round(costo_alcohol_por_persona, 2))
    
    print("\n--- RESUMEN ---")
    print("Invitado SIN alcohol paga: $", round(costo_comida_por_persona + costo_sin_alcohol_por_persona, 2))
    print("Invitado CON alcohol paga: $", round(costo_comida_por_persona + costo_sin_alcohol_por_persona + costo_alcohol_por_persona, 2))