from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    choice = int(input("1 - peržiūrėti, 2 - įvesti pajamas, 3 - įvesti išlaidas, 4 - balansas, 0 - išeiti\n"))
    match choice:
        case 1: print(biudzetas.zurnalas)
        case 2: biudzetas.prideti_pajamas()
        case 3: biudzetas.prideti_islaidas()
        case 4: print("Balansas", biudzetas.gauti_balansa())
        case 0: break
