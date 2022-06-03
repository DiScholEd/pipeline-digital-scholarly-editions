import re

def placeName(text):
    """Apply tags to the regex

    :param text str: place that has to be encoded
    :returns: place encoded with the proper tag
    :rtype: str
    """

    #This series of statements contains regex of places from the corpus
    l0001 = re.compile(r"P(aris|ARIS)")
    l0002 = re.compile(r"(l|L)a Flèche")
    l0003 = re.compile(r"N(.|ew|EW)(-| )?Y(ork|ORK)")
    l0004 = re.compile(r"((L|l)(E|e) )?M(ans|ANS)")
    l0005 = re.compile(r"(r|R)ue Molitor")
    l0006 = re.compile(r"((c|C)(l(e|é)rmont|LERMONT)(-| ))?C(réans|R(É|E)ANS)")
    l0007 = re.compile(r"C(roisic|ROISIC)")
    l0008 = re.compile(r"Guirec")
    l0009 = re.compile(r"Pas-de-Calais")
    l0010 = re.compile(r"Venise")
    l0011 = re.compile(r"(l')Atlanti(a|q)(u|n)e")
    l0012 = re.compile(r"9 Square Vergote")
    l0013 = re.compile(r"Ablain")
    l0014 = re.compile(r"Aboukir")
    l0015 = re.compile(r"Acropole")
    l0016 = re.compile(r"Adriatique")
    l0017 = re.compile(r"(l')?Afrique")
    l0018 = re.compile(r"A(gadir|GADIR)")
    l0019 = re.compile(r"Agen")
    l0020 = re.compile(r"Aisne")
    l0021 = re.compile(r"(l('|’))Aisne")
    l0022 = re.compile(r"Aix-la-C(l|h)apelle")
    l0023 = re.compile(r"Albanie")
    l0024 = re.compile(r"Albion")
    l0025 = re.compile(r"Alençon")
    l0026 = re.compile(r"Alexandrie")
    l0027 = re.compile(r"Algérie")
    l0028 = re.compile(r"(L')?(A|a)((l|i)le(g|m|p)ag(n|a)e|LLEMAGNE)")

    #This series of statements contains the encoding for the places from the corpus
    text = re.sub(l0001, r'<placeName ref="#l0001" type="pec">\g<0></placeName>', text)
    text = re.sub(l0002, r'<placeName ref="#l0002" type="pec">\g<0></placeName>', text)
    text = re.sub(l0003, r'<placeName ref="#l0003" type="pec">\g<0></placeName>', text)
    text = re.sub(l0004, r'<placeName ref="#l0004" type="pec">\g<0></placeName>', text)
    text = re.sub(l0005, r'<placeName ref="#l0005" type="pec">\g<0></placeName>', text)
    text = re.sub(l0006, r'<placeName ref="#l0006" type="pec">\g<0></placeName>', text)
    text = re.sub(l0007, r'<placeName ref="#l0007" type="pec">\g<0></placeName>', text)
    text = re.sub(l0008, r'<placeName ref="#l0008" type="pec">\g<0></placeName>', text)
    text = re.sub(l0009, r'<placeName ref="#l0009" type="pec">\g<0></placeName>', text)
    text = re.sub(l0010, r'<placeName ref="#l0010" type="pec">\g<0></placeName>', text)
    text = re.sub(l0011, r'<placeName ref="#l0011" type="pec">\g<0></placeName>', text)
    text = re.sub(l0012, r'<placeName ref="#l0012" type="pec">\g<0></placeName>', text)
    text = re.sub(l0013, r'<placeName ref="#l0013" type="pec">\g<0></placeName>', text)
    text = re.sub(l0014, r'<placeName ref="#l0014" type="pec">\g<0></placeName>', text)
    text = re.sub(l0015, r'<placeName ref="#l0015" type="pec">\g<0></placeName>', text)
    text = re.sub(l0016, r'<placeName ref="#l0016" type="pec">\g<0></placeName>', text)
    text = re.sub(l0017, r'<placeName ref="#l0017" type="pec">\g<0></placeName>', text)
    text = re.sub(l0018, r'<placeName ref="#l0018" type="pec">\g<0></placeName>', text)
    text = re.sub(l0019, r'<placeName ref="#l0019" type="pec">\g<0></placeName>', text)
    text = re.sub(l0020, r'<placeName ref="#l0020" type="pec">\g<0></placeName>', text)
    text = re.sub(l0021, r'<placeName ref="#l0021" type="pec">\g<0></placeName>', text)
    text = re.sub(l0022, r'<placeName ref="#l0022" type="pec">\g<0></placeName>', text)
    text = re.sub(l0023, r'<placeName ref="#l0023" type="pec">\g<0></placeName>', text)
    text = re.sub(l0024, r'<placeName ref="#l0024" type="pec">\g<0></placeName>', text)
    text = re.sub(l0025, r'<placeName ref="#l0025" type="pec">\g<0></placeName>', text)
    text = re.sub(l0026, r'<placeName ref="#l0026" type="pec">\g<0></placeName>', text)
    text = re.sub(l0027, r'<placeName ref="#l0027" type="pec">\g<0></placeName>', text)
    text = re.sub(l0028, r'<placeName ref="#l0028" type="pec">\g<0></placeName>', text)
    return text