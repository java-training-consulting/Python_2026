# Hex -> Decimal

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.



# Modelierung Abstaktion
# AFDD -> Hex
# ff -> Hex
# string ->  int



# E 0,1,....A,...E, F  -> 0,1,...10,... 14, 15
def hexZifferToInt(param):
    if param[0] >= "0" and  param[0] <= "9":
        return ord(param[0]) - ord('0')
    if param[0] >= "A" and  param[0] <= "F":
        return ord(param[0]) - ord('A') + 10

def hexToInt(hexString):

    # Verarbeitung
    if len(hexString) == 0:
        return 0

    intValue = 0
    länge = len(hexString)
    intValue = intValue + ( hexZifferToInt(hexString[länge - 1 - 0]) * 16 ** 0 )
    intValue = intValue + ( hexZifferToInt(hexString[länge - 1 - 1]) * 16 ** 1 )
    intValue = intValue + ( hexZifferToInt(hexString[länge - 1 - 2]) * 16 ** 2 )
    #  länge der zeichen

    # intValue = intValue + ( hexZifferToInt(hexString[länge - 1 - ?]) * 16 ** ? )
    # Fertigstellen

    '''
    print(hexString[0])
    print(ord(hexString[0]))
    print(f"ord(hexString[0]) - ord('0')   {ord(hexString[0]) - ord("0")}")

    # A - F
    print(f"ord(hexString[0]) - ord('A')   {ord(hexString[0]) - ord("A") + 15}")
    print()
    '''
    return intValue



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(hexToInt("FFF"))  # 0
    print(int("FFF",16))
    print(int("fff", 16))

    '''
    print(hexToInt("2"))  # 2
    print(hexToInt("9"))  # 2
    print(hexToInt("A"))  # 10
    print(hexToInt("F"))  # 15
    print("Test hexZifferToInt")
    print(hexZifferToInt("0"))
    print(hexZifferToInt("1"))
    print(hexZifferToInt("9"))
    print(hexZifferToInt("A"))
    print(hexZifferToInt("E"))
    print(hexZifferToInt("F"))
    '''

# KI ChatGPT Prompt: Hier ist ein Python-Programm, das einen Hex-String mit einer Schleife in einen Integer umwandelt:


    hex_string = input("Hex-String eingeben: ").upper()

    zahl = 0

    for zeichen in hex_string:
        ziffer = int(zeichen, 16)
        zahl = zahl * 16 + ziffer

    print("Integer:", zahl)
