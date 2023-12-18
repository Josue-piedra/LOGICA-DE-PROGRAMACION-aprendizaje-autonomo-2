Nombre = input ("Ingresar su nombre:")
Sexo = input ("Ingresar su sexo (M/F):")

if Sexo.upper() == "M" and Nombre.upper() > "N" or Sexo. upper() == "F" and Nombre.upper() < "M" :
    Grupo = "A"
else:
     Grupo = "B"

print("Ustede pertenece al grupo", Grupo)
