import string

## Partie 1 Chiffrement de Cesar
alphabet = string.printable + "éèêàôëùïü"
# Etape 1 : chiffrement de cesar (à droite)
def chiffre_cesar(chaine, decalage):
    chaine_chiffre = ''
    taille_alphabet = len(alphabet)
    for i in chaine:
        index_i = alphabet.index(i)
        index_chiffre = (index_i+decalage)%taille_alphabet # => 23 + 3 = 26 -26 = 0, 24 +3 = 27-26 = 1, 25+3= 28-26=2
        chaine_chiffre += alphabet[index_chiffre]

    return chaine_chiffre

chaine, decalage = "Nezir Abakar", 15
chaine_chiffree = chiffre_cesar(chaine, decalage)
print(f"Chiffrement de {chaine}: {chaine_chiffree}")

#Etape 2: Dechiffrement de Cesar
def dechiffre_cesar(chaine, decalage):
    return chiffre_cesar(chaine, -decalage)

#Test
print(f"Déchiffrement de {chaine_chiffree} est : {dechiffre_cesar(chaine_chiffree, decalage)}")

#Etape 3 : Brute force de chiffrement de cesar
def dechiffre_cesar_tout_cle(chaine):
    for i in range(0, 26):
        result = dechiffre_cesar(chaine=chaine, decalage=i)
        print(f"{i} : {result}")

all_string = "I love God, my dream is to come back healthy and godly!", 15 # decalage à droite --> QHCLU, => à gauche : kbwfo

#Test etape 3
#dechiffre_cesar_tout_cle(chaine=chaine_chiffree)

## Partie 2 : Chiffrement de Vigenère
# Etape 4 : chiffrement de vigenère

def chiffre_vigenere(chars, keys):
    keys_suits = [alphabet.index(key) for key in keys] # Convertir en liste des index la clé
    size_keys_suits = len(keys_suits)
    cripted_message =  ''
    for index, char in enumerate(chars):
        new_key = keys_suits[index%size_keys_suits]
        vigenere = chiffre_cesar(chaine=char, decalage=new_key)
        cripted_message +=vigenere
    
    return cripted_message

# Test chiffrement vigenère
name = 'HELLOWORLD'
keys = 'KEY'  # []
cripted_message =  chiffre_vigenere(name, keys)

print(f"Chiffrement de vigenere de {name} : est {cripted_message}\n")

# Etape 5 : Dechiffrement de Vigenère
def dechiffre_vignere(chars, keys):
    keys_suits = [alphabet.index(key) for key in keys]
    uncripted_message = ''
    for index, char in enumerate(chars):
        new_key = keys_suits[index%len(keys_suits)]
        uncripted_message += dechiffre_cesar(chaine=char, decalage=new_key)
    return uncripted_message


if __name__:
    chaine, decalage = "Nezir Abakar", 15
    #chaine_chiffree = chiffre_cesar(chaine, decalage)
    #print(f"Chiffrement de {chaine}: \n{chaine_chiffree}\n")
    dechff_vigenere = dechiffre_vignere(cripted_message, keys=keys)
    print(dechff_vigenere)



