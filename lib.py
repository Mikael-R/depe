tabela = {
    "1": ["Hidrogênio", "H"],
    "2": ["Hélio", "He"],
    "3": ["Lítio", "Li"],
    "4": ["Beŕilio", "Be"],
    "5": ["Boro", "B"],
    "6": ["Carbono", "C"],
    "7": ["Nitrogênio", "N"],
    "8": ["Oxigênio", "O"],
    "9": ["Flúor", "F"],
    "10": ["Neônio", "Ne"],
    "11": ["Sódio", "Na"],
    "12": ["Magnésio", "Mg"],
    "13": ["Alumínio", "Al"],
    "14": ["Silício", "Si"],
    "15": ["Fósforo", "P"],
    "16": ["Enxofre", "S"],
    "17": ["Cloro", "Cl"],
    "18": ["Argônio", "Ar"],
    "19": ["Potássio", "Po"],
    "20": ["Cálcio", "Ca"],
    "21": ["Escândio", "Sc"],
    "22": ["Titânio", "Ti"],
    "23": ["Vanádio", "V"],
    "24": ["Crômio", "Cr"],
    "25": ["Manganês", "Mg"],
    "26": ["Ferro", "Fe"],
    "27": ["Cobalto", "Co"],
    "28": ["Níquel", "Ni"],
    "29": ["Cobre", "Cu"],
    "30": ["Zinco", "Zn"],
    "31": ["Gálio", "Ga"],
    "32": ["Germânio", "Ge"],
    "33": ["Arsênio", "As"],
    "34": ["Selénio", "Se"],
    "35": ["Bromo", "Br"],
    "36": ["Criptônio", "Kr"],
    "37": ["Rubídio", "Rb"],
    "38": ["Estrôncio", "Sr"],
    "39": ["Lítrio", "Y"],
    "40": ["Zircônio", "Zr"],
    "41": ["Nióbio", "Nb"],
    "42": ["Molibdênio", "Mo"],
    "43": ["Tecnécio", "Tc"],
    "44": ["Rutênio", "Ru"],
    "45": ["Ródio", "Rh"],
    "46": ["Paládio", "Pd"],
    "47": ["Prata", "Ag"],
    "48": ["Cádmio", "Cd"],
    "49": ["Índio", "In"],
    "50": ["Estanho", "Sn"],
    "51": ["Antimônio", "Sb"],
    "52": ["Telúrio", "Te"],
    "53": ["Iodo", "I"],
    "54": ["Xenônio", "Xe"],
    "55": ["Césio", "Cs"],
    "56": ["Bário", "Ba"],
    "57": ["Latânio", "La"],
    "58": ["Cério", "Ce"],
    "59": ["Praseodímio", "Pr"],
    "60": ["Neodímio", "Nd"],
    "61": ["Promécio", "Pm"],
    "62": ["Samário", "Sm"],
    "63": ["Európio", "Eu"],
    "64": ["Gadolínio", "Gd"],
    "65": ["Térbio", "Tb"],
    "66": ["Disprósio", "Dy"],
    "67": ["Hólmio", "Ho"],
    "68": ["Érbio", "Er"],
    "69": ["Túlio", "Tm"],
    "70": ["Itérbio", "Yb"],
    "71": ["Lutécio", "Lu"],
    "72": ["Háfnio", "Hf"],
    "73": ["Tântalo", "Ta"],
    "74": ["Tungstênio", "W"],
    "75": ["Rênio", "Re"],
    "76": ["Ósmio", "Os"],
    "77": ["Irídio", "Ir"],
    "78": ["Platina", "Pt"],
    "79": ["Ouro", "Au"],
    "80": ["Mercúrio", "Hg"],
    "81": ["Tálio", "Tl"],
    "82": ["Chumbo", "Pb"],
    "83": ["Bismuto", "Bi"],
    "84": ["Polônio", "Po"],
    "85": ["Astrato", "At"],
    "86": ["Randônio", "Rn"],
    "87": ["Frâncio", "Fr"],
    "88": ["Rádio", "Ra"],
    "89": ["Actínio", "Ac"],
    "90": ["Tório", "Th"],
    "91": ["Protactínio", "Pa"],
    "92": ["Urânio", "U"],
    "93": ["Netúnio", "Np"],
    "94": ["Plutônio", "Pu"],
    "95": ["Amerício", "Am"],
    "96": ["Cúrio", "Cm"],
    "97": ["Berquélio", "Bk"],
    "98": ["Califórnio", "Cf"],
    "99": ["Einstênio", "Es"],
    "100": ["Férmio", "Fm"],
    "101": ["Mendelévio", "Md"],
    "102": ["Nobélio", "No"],
    "103": ["Laurêcio", "Lr"],
    "104": ["Ruthenfórdio", "Rf"],
    "105": ["Dúbnio", "Db"],
    "106": ["Seabórgio", "Sg"],
    "107": ["Bóhrio", "Bh"],
    "108": ["Hássio", "Hs"],
    "109": ["Meitnério", "Mt"],
    "110": ["Darmstádio", "Ds"],
    "111": ["Roentgênio", "Rg"],
    "112": ["Copernício", "Cn"],
    "113": ["Nihônio", "Nh"],
    "114": ["Fleróvio", "Fl"],
    "115": ["Moscóvio", "Mc"],
    "116": ["Livermório", "Lv"],
    "117": ["Tennesso", "Ts"],
    "118": ["Oganessónio", "Og"],
}


def pesquisar(elemento):
    if elemento.isnumeric():
        for n in range(1, 119):
            if str(n) == elemento:
                elemento_lista = [
                    n,
                    tabela[str(n)][0],
                    tabela[str(n)][1]
                ]
                return elemento_lista

    elif len(elemento) <= 2 and elemento.isalpha() == True:
        for n in range(1, 119):
            if tabela[str(n)][1] == elemento:
                elemento_lista = [
                    n,
                    tabela[str(n)][0],
                    tabela[str(n)][1],
                ]
                return elemento_lista

    elif len(elemento) > 2 and elemento.isalpha() == True:
        for n in range(1, 119):
            if tabela[str(n)][0] == elemento:
                elemento_lista = [
                    n,
                    tabela[str(n)][0],
                    tabela[str(n)][1]
                ]
                return elemento_lista

    else:
        return None


def distribuir(z, s1=0, s2=0, p2=0, s3=0, p3=0, s4=0, d3=0, p4=0, s5=0,
 d4=0, p5=0, s6=0, f4=0, d5=0, p6=0, s7=0, f5=0, d6=0, p7=0):
    ########## 1s2 ##########
    while True:
        if z == 0 or s1 == 2:
            break
        s1 += 1
        z -= 1
    ########## 2s2 ##########
    while True:
        if z == 0 or s2 == 2:
            break
        s2 += 1
        z -= 1
    ########## 2p6 ##########
    while True:
        if z == 0 or p2 == 6:
            break
        p2 += 1
        z -= 1
    ########## 3s2 ##########
    while True:
        if z == 0 or s3 == 2:
            break
        s3 += 1
        z -= 1
    ########## 3p6 ##########
    while True:
        if z == 0 or p3 == 6:
            break
        p3 += 1
        z -= 1
    ########## 4s2 ##########
    while True:
        if z == 0 or s4 == 2:
            break
        s4 += 1
        z -= 1
    ########## 3d10 ##########
    while True:
        if z == 0 or d3 == 10:
            break
        d3 += 1
        z -= 1
    ########## 4p6 ##########
    while True:
        if z == 0 or p4 == 6:
            break
        p4 += 1
        z -= 1
    ########## 5s2 ##########
    while True:
        if z == 0 or s5 == 2:
            break
        s5 += 1
        z -= 1
    ########## 4d10 ##########
    while True:
        if z == 0 or d4 == 10:
            break
        d4 += 1
        z -= 1
    ########## 5p6 ##########
    while True:
        if z == 0 or p5 == 6:
            break
        p5 += 1
        z -= 1
    ########## 6s2 ##########
    while True:
        if z == 0 or s6 == 2:
            break
        s6 += 1
        z -= 1
    ########## 4f14 ##########
    while True:
        if z == 0 or f4 == 14:
            break
        f4 += 1
        z-= 1
    ########## 5d10 ##########
    while True:
        if z == 0 or d5 == 10:
            break
        d5 += 1
        z -= 1
    ########## 6p6 ##########
    while True:
        if z == 0 or p6 == 6:
            break
        p6 += 1
        z -= 1
    ########## 7s2 ##########
    while True:
        if z == 0 or s7 == 2:
            break
        s7 += 1
        z -= 1
    ########## 5f14 ##########
    while True:
        if z == 0 or f5 == 14:
            break
        f5 += 1
        z -= 1
    ########## 6d10 ##########
    while True:
        if z == 0 or d6 == 10:
            break
        d6 += 1
        z -= 1
    ########## 7p6 ##########
    while True:
        if z == 0 or p7 == 6:
            break
        p7 += 1
        z -= 1

    return {
        "1s": s1,
        "2s": s2,
        "2p": p2,
        "3s": s3,
        "3p": p3,
        "4s": s4,
        "3d": d3,
        "4p": p4,
        "5s": s5,
        "4d": d4,
        "5p": p5,
        "6s": s6,
        "4f": f4,
        "5d": d5,
        "6p": p6,
        "7s": s7,
        "5f": f5,
        "6d": d6,
        "7p": p7
    }
