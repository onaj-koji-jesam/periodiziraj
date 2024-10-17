elementi = ["H" ,                                                                                "He",
            "Li","Be",                                                  "B" ,"C" ,"N" ,"O" ,"F" ,"Ne",
            "Na","Mg",                                                  "Al","Si","P", "S" ,"Cl","Ar",
            "K" ,"Ca","Sc","Ti","V" ,"Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
            "Rb","Sr","Y" ,"Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I" ,"Xe",
            "Cs","Ba","__","Hf","Ta","W" ,"Re","Os","Ir","Pt","Au","Hg","Ti","Pb","Bi","Po","At","Rn",
            "Fr","Ra","__","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]

elementi = elementi[:56] + ["La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"] + (
         elementi[57:74] + ["Ac","Th","Pa","U" ,"Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr"]) + elementi[75:]

imena_elemenata = ["vodik","helij","litij","berilij","bor","ugljik","dušik","kisik","fluor","neon","natrij","magnezij","aluminij","silicij",
                   "fosfor","sumpor","klor","argon","kalij","kalcij","skandij","titanij","vanadij","krom","mangan","željezo","kobalt","nikal",
                   "bakar","cink","galij","germanij","arsen","selenij","brom","kripton","rubidij","stroncij","itrij","cirkonij","niobij",
                   "molibden","tehnecij","rutenij","rodij","paladij","srebro","kadmij","indij","kositar","antimon","telurij","jod","ksenon",
                   "cezij","barij","lantan","cerij","praseodimij","neodimij","prometij","samarij","europij","gadolinij","terbij","disprozij","holmij","erbij",
                   "tulij","iterbij","lutecij","hafnij","tantal","volfram","renij","osmij","iridij","platina","zlato","živa","talij","olovo","bizmut",
                   "polonij","astat","radon","francij","radij","aktinij","torij","protaktinij","uranij","neptunij","plutonij","americij",
                   "kurij","berkelij","kalifornij","einsteinij","fermij","mendelevij","nobelij","lawrencij","rutherfordij","dubnij","seaborgij","bohrij",
                   "hassij","meitnerij","darmštatij","roentgenij","kopernicij","nihonij","flerovij","moskovij","livermorij","tenes","oganeson"]

lista_elemenata = []

tekst = input("periodiziraj: ").upper() + ' '

def odredi_element(oe_slova, oe_elementi = elementi):
    if oe_slova[0].capitalize() in oe_elementi and oe_slova[1].capitalize() in oe_elementi:
        return oe_slova[0].capitalize()
    if oe_slova.capitalize() in oe_elementi:
        return oe_slova.capitalize()
    if oe_slova[0].capitalize() in oe_elementi:
        return oe_slova[0].capitalize()
    return f">{oe_slova[0].capitalize()}<"

def optimizirano(op_lista_elemenata_nm, op_elementi = elementi):
    op_lista_elemenata = op_lista_elemenata_nm[:]
    for op_i in range(len(op_lista_elemenata)):
        if op_lista_elemenata[op_i][1] == ">-<" and op_i > 0 and len(op_lista_elemenata[op_i-1][0]) == 2:
            if op_lista_elemenata[op_i-1][0][0] in op_elementi and str(op_lista_elemenata[op_i-1][0][1]+op_lista_elemenata[op_i][0][1]).capitalize() in op_elementi:
                op_lista_elemenata[op_i] = [str(op_lista_elemenata[op_i-1][0][1]+op_lista_elemenata[op_i][0][1]).capitalize(), op_elementi.index(
                str(op_lista_elemenata[op_i-1][0][1]+op_lista_elemenata[op_i][0][1]).capitalize())+1]
                op_lista_elemenata[op_i-1] = [op_lista_elemenata[op_i-1][0][0], op_elementi.index(op_lista_elemenata[op_i-1][0][0])+1]
    return op_lista_elemenata

def vidljivo(v_lista, v_lista_imena = imena_elemenata):
    v_tekst = ''
    v_brojevi = []
    v_imena = ''
    for v_i in v_lista:
        v_tekst += v_i[0]
        v_brojevi.append(v_i[1])
        if v_i[1] == " ":
            v_imena += " --  "
        elif v_i[1] == ">-<":
            v_imena += ">-<, "
        else:
            v_imena += v_lista_imena[v_i[1]-1] + ', '
    return (v_tekst, v_brojevi, v_imena)


skip = 0
for i in range(len(tekst)-1):
    if skip > 0:
        skip -= 1
    else:
        el = odredi_element(tekst[i:i+2])
        if el == '> <':
            lista_elemenata.append([" ", " "])
        elif "<" in el:
            lista_elemenata.append([el, ">-<"])
        else:
            lista_elemenata.append([el, elementi.index(el)+1])
        if len(el) == 2:
            skip = 1

#print(lista_elemenata)
#print(vidljivo(lista_elemenata))
#print(f'{(len(tekst)-1-vidljivo(lista_elemenata)[1].count(">-<"))/(len(tekst)-1)*100}%')
#print()

#print(lista_elemenata)
lista_elemenata = optimizirano(lista_elemenata)
print(vidljivo(lista_elemenata))
print(f'{(len(tekst)-1-vidljivo(lista_elemenata)[1].count(">-<"))/(len(tekst)-1)*100}%')

