import time
import fluidsynth
import random
import pyaudio
import numpy
from scipy.io.wavfile import write




# fluidsynth c:\users\matheus\appdata\local\pip\cache\wheels\dc\16\09\eb08b4e34e6b638f113d2018cf0b22de1d8dca22a3a71873f7
piano = fluidsynth.Synth()
piano.start(driver ='dsound')  # use DirectSound driver
piano_som = piano.sfload(r'C:\Users\Matheus\Downloads\fluidsynth-2.3.0-win10-x64\FluidR3_GM\FluidR3_GM.sf2')  # replace path as needed
piano.program_select(0, piano_som, 0, 0)
piano.set_reverb(100, 1, 100, 1)
piano.set_chorus(99, 1, 99, 1)

violino = fluidsynth.Synth()
violino.start(driver = 'dsound')  # use DirectSound driver
violino_som = violino.sfload(r'C:\Users\Matheus\Downloads\fluidsynth-2.3.0-win10-x64\FluidR3_GM\336_Massive_strings.sf2')  # replace path as needed
violino.program_select(0, piano_som, 0, 0)
violino.set_reverb(100,1,100,1)
violino.set_chorus(99,1,99,1)

notas_oitavas ={
    1: {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11},
    2: {'C':12,'C#':13,'D':14,'D#':15,'E':16,'F':17,'F#':18,'G':19,'G#':20,'A':21,'A#':22,'B':23},
    3: {'C':24,'C#':25,'D':26,'D#':27,'E':28,'F':29,'F#':30,'G':31,'G#':32,'A':33,'A#':34,'B':35},
    4: {'C':36,'C#':37,'D':38,'D#':39,'E':40,'F':41,'F#':42,'G':43,'G#':44,'A':45,'A#':46,'B':47},
    5: {'C':48,'C#':49,'D':50,'D#':51,'E':52,'F':53,'F#':54,'G':55,'G#':56,'A':57,'A#':58,'B':59},
    '':{'C':48,'C#':49,'D':50,'D#':51,'E':52,'F':53,'F#':54,'G':55,'G#':56,'A':57,'A#':58,'B':59},
    6: {'C':60,'C#':61,'D':62,'D#':63,'E':64,'F':65,'F#':66,'G':67,'G#':68,'A':69,'A#':70,'B':71},
    7: {'C':72,'C#':73,'D':74,'D#':75,'E':76,'F':77,'F#':78,'G':79,'G#':80,'A':81,'A#':82,'B':83},
    8: {'C':84,'C#':85,'D':86,'D#':87,'E':88,'F':89,'F#':90,'G':91,'G#':92,'A':93,'A#':94,'B':95},
    9: {'C':96,'C#':97,'D':98,'D#':99,'E':100,'F':101,'F#':102,'G':103,'G#':104,'A':105,'A#':106,'B':107},
}

campos_harmonicos = {
    'C': ['C','Dm','Em','F','G7','Am','B'],
    'C#': ['C#','D#m','Fm','F#','G#7','A#m','C'],
    'D': ['D','Em','F#m','G','A7','Bm','C#'],
    'D#': ['D#','Fm','Gm','G#','A#7','Cm'],
    'E': ['E','F#m','G#m','A','B7','C#m','D#'],
    'F': ['F','Gm','Am','A#','C7','Dm','E'],
    'F#': ['F#','G#m','A#m','B','C#7','D#m','F'],
    'G': ['G','Am','Bm','C','D7','Em','F#'],
    'G#': ['G#','A#m','Cm','C#','D#7','Fm','G'],
    'A': ['A','Dm','C#m','D','E7','F#m','G#'],
    'A#': ['A#','Cm','Dm','D#','F7','Gm','A'],
    'B': ['B','C#m','D#m','E','F#7','G#m','A#'],

    'Cm': ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'],
    'C#m': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'Dm': ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
    'D#m': ['D#', 'E#', 'F#', 'G#', 'A#', 'B','C#'],
    'Em': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'Fm': ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#'],
    'F#m': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'Gm': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
    'G#m': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
    'Am': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'A#m': ['A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#'],
    'Bm': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']
}


notas_completas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def getNota(oitava,nota):
    notas = notas_oitavas.get(oitava)
    notaValue = notas.get(nota)
    return (notaValue)

def getNotasAcordes(oitava,nota_tonica,casas):
    indexTonica = notas_completas.index(nota_tonica)
    if (0 <= indexTonica + casas) and ((indexTonica + casas) < len(notas_completas)):
        return {'oitava': oitava, 'nota': notas_completas[indexTonica + casas] }
    else:
        debito_notas = len(notas_completas) - indexTonica
        notas_restantes = casas - debito_notas
        oitava = oitava + 1
        return {'oitava': oitava,  'nota': notas_completas[notas_restantes]}

def getAcorde(oitava, acorde):
    aux = acorde.replace('7','')
    nota_tonica = aux.replace('m','')
    terca = ""
    quinta = getNotasAcordes(oitava,nota_tonica,7) # notas_completas[indexTonica + casas]
    setima = ""
    if('m' in acorde):
        terca= getNotasAcordes(oitava,nota_tonica,3) #notas_completas[notas_completas.index(nota_tonica) + 3]
        if ('7' in acorde):
            setima = getNotasAcordes(oitava,nota_tonica,9) #notas_completas[notas_completas.index(nota_tonica) + 9]
    else:
        terca = getNotasAcordes(oitava,nota_tonica,4) #notas_completas[notas_completas.index(nota_tonica) + 4]
        if ('7' in acorde):
            setima = getNotasAcordes(oitava,nota_tonica,10) #notas_completas[notas_completas.index(nota_tonica) + 10]
    # print(nota_tonica)
    # print(terca.get('nota'))
    # print(quinta.get('nota'))
    # print(setima.get('nota')) if setima != "" else ''

    n_notaTonica = getNota(oitava,nota_tonica)
    n_terca = getNota(terca.get('oitava'),terca.get('nota'))
    n_quinta = getNota(quinta.get('oitava'),quinta.get('nota'))
    n_setima = getNota(setima.get('oitava'),setima.get('nota')) if setima != "" else ''

    return {'nota_tonica': n_notaTonica, 'terca': n_terca, 'quinta': n_quinta, 'setima': n_setima if setima != "" else ''}



def play(campo_hamornico, duracao):
    notas = campos_harmonicos.get(campo_hamornico)
    tempo = 1

    for step in range(duracao):
        n_acorde_aleatorio = random.randint(0, len(campos_harmonicos.get(campo_hamornico))) -1
        acorde = getAcorde(random.randint(4,6), notas[n_acorde_aleatorio])

        nota_tonica = acorde.get('nota_tonica')
        terca = acorde.get('terca')
        quinta = acorde.get('quinta')
        setima = acorde.get('setima')  if acorde.get('setima') != "" else ''

        violino.noteon(0,nota_tonica,127)

        piano.noteon(0, nota_tonica, 127)
        piano.noteon(0, terca, 127)
        piano.noteon(0, quinta, 127)
        piano.noteon(0, setima, 127) if setima != "" else ''

        time.sleep(tempo)

        piano.noteoff(0, nota_tonica)
        piano.noteoff(0, terca)
        piano.noteoff(0, quinta)
        piano.noteoff(0, setima) if setima != "" else ''



        #time.sleep(0.1)

        n_acorde_aleatorio_reserva = random.randint(0, len(campos_harmonicos.get(campo_hamornico))) -1
        acorde_reserva = getAcorde(random.randint(3,5), notas[n_acorde_aleatorio_reserva])
        notas_acordes = [nota_tonica, terca, quinta, acorde_reserva.get('nota_tonica'), acorde_reserva.get('terca'),acorde_reserva.get('quinta')]
        for dedilhado in range(random.randint(2,20)):

            nota_aleatoria = notas_acordes[random.randint(0,5)]


            piano.noteon(0, nota_aleatoria, 127)
            time.sleep(tempo/2)
            piano.noteoff(0, nota_aleatoria)
        violino.noteoff(0,nota_tonica)


play('Bm',50000)
piano.delete()




