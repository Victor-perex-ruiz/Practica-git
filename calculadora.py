otra="si".strip().lower();
while otra=="si":
    print("****Bienvenido A la Calculadora Portatil XD*****\n")
    print("**Seleccione que Operacion deseas realizar con los numeros respectivos")
    sumar=print("1.Sumar = ");
    restar=print("2.Restar =");
    multiplicar=print("3.Multiplicar =");
    dividir=print("2.Dividir =");
    print("");
    
    operacion=int(input(""));
    nom={1:"Suma",2:"Resta",3:" Multiplicacion",4:"Divicion"};

    print("INGRESE 2 NUMEROS \n")
    a=int(input("Numero °1 ="))
    b=int(input("Numero °2 ="))

    def Calcular(a,b , operacion):
        
        if operacion == 1:
            respuesta= a+b
        
        if operacion == 2:
            respuesta =a-b 

        if operacion == 3:
            respuesta =a*b

        if operacion == 4:
            respuesta=a/b
        
        return respuesta,nom[operacion]
    
    respuesta,nombre= Calcular(a, b, operacion);
    
    print(f"El RESULTADO ES = {respuesta}\n")
    print(f"Operacion ralizada {nombre}\n")

    print("Si deseas Continuar Escribe SI/No")
    otra=input("").strip().lower();
    if otra != "si":
        break



