# numero por extenso:
# pegar um numero de 0 a 100
# fazer o programa escrever ele por exenso.

nomes_1_20 = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezesete',
    18: 'dezoito',
    19: 'dezenove',
}
nome20_100 = {
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
    100: 'cem'
}
numero100_900 = {
    0: 'zero',
    100: 'cento',
    200: 'duzentos',
    300: 'trezentos',
    400: 'quatrocentos',
    500: 'quinhentos',
    600: 'seicentos',
    700: 'setecentos',
    800: 'oitocentos',
    900: 'novecentos'
}
numero = (int(input('Número de 0 a 1000:\n')))
if 0 <= numero < 101:
    if numero < 20:
        print(nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print('vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print('trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print('quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print('cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print('sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print('setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print('oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print('noventa e ' + nomes_1_20[nov])
    else:
        print(nome20_100[numero])
elif 100 < numero < 200:
    cent = numero100_900[100]
    numero = numero - 100
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 200 < numero < 300:
    cent = numero100_900[200]
    numero = numero - 200
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 300 < numero < 400:
    cent = numero100_900[300]
    numero = numero - 300
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 400 < numero < 500:
    cent = numero100_900[400]
    numero = numero - 400
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 500 < numero < 600:
    cent = numero100_900[500]
    numero = numero - 500
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 600 < numero < 700:
    cent = numero100_900[600]
    numero = numero - 600
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 700 < numero < 800:
    cent = numero100_900[700]
    numero = numero - 700
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 800 < numero < 900:
    cent = numero100_900[800]
    numero = numero - 800
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
elif 900 < numero < 1000:
    cent = numero100_900[900]
    numero = numero - 900
    if numero < 20:
        print(cent + ' e ' + nomes_1_20[numero])
    elif 20 < numero < 30:
        vinte = numero - 20
        print(cent + ' e vinte e ' + nomes_1_20[vinte])
    elif 30 < numero < 40:
        trinta = numero - 30
        print(cent + ' e trinta e ' + nomes_1_20[trinta])
    elif 40 < numero < 50:
        quare = numero - 40
        print(cent + ' e quarenta e ' + nomes_1_20[quare])
    elif 50 < numero < 60:
        cinq = numero - 50
        print(cent + ' e cinquenta e ' + nomes_1_20[cinq])
    elif 60 < numero < 70:
        sex = numero - 60
        print(cent + ' e sessenta e ' + nomes_1_20[sex])
    elif 70 < numero < 80:
        seten = numero - 70
        print(cent + ' e setenta e ' + nomes_1_20[seten])
    elif 80 < numero < 90:
        oit = numero - 80
        print(cent + ' e oitenta e ' + nomes_1_20[oit])
    elif 90 < numero < 100:
        nov = numero - 90
        print(cent + ' e noventa e ' + nomes_1_20[nov])
    else:
        print(cent + ' e ' + nome20_100[numero])
else:
    print(numero100_900[numero])
