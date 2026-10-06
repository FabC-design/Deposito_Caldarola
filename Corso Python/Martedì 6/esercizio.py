livello1 = input("Inserisci la password del primo livello: ")
if livello1 == "ciao":
    print("Primo livello superato")
    livello2 = input("Inserisci la password del secondo livello: ")
    if livello2 == "python":
        print("Secondo livello superato")
        livello3 = input("Inserisci la password del terzo livello: ")
        if livello3 == "123":
            print("Terzo livello superato")
            print("Puoi passare")
        else:
            print("Non puoi passare")
    else:
        print("Non puoi passare")
else:
    print("Non puoi passare")