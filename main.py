import musicalbeeps
import random

player = musicalbeeps.Player(volume = 0.1,
                            mute_output = False)
notas = ['C','D','E','F','G','A','B']
notasCompletas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
acidentes = {'C':'C#','D':'D#','E':'E#','F':'F#','G':'G#','A':'A#','B':'B#'}
campo_harmonico = {
    'C': ['C','D','F','A','E','G','B','F','G','A','C','E','pause']
}

tamanhoCampo = len(campo_harmonico.get('C'))

qtdNotas = range(300)

# Acorde maior 1# nota raiz + (4 paços até próxima nota) +  (5 paços até próxima nota)
# Acorde menor 1# nota raiz + (3 paços até próxima nota) +  (4 paços até próxima nota)

#    - Função para coletar nota e retornar o som passando a oitava como parametro
# Ter controle de oitava para não ficar estranho
#    - Função para tocar um acorde
#    - Deve decidir aleatóriamente se o próximo som vai ser uma nota sozinha ou um acorde
#    - Deve ter uma duração aleatória da nota/acorde
#    - Deve ter espaços aleatórios entre frases


for i in qtdNotas:
    print(i)
    notaIndex = random.randint(0, tamanhoCampo)
    nota = campo_harmonico.get('C')[notaIndex -2 ]
    nota2 = campo_harmonico.get('C')[notaIndex -1 ]
    nota3 =  campo_harmonico.get('C')[notaIndex -3 ]
    player.play_note(nota3,random.uniform(0,1))
    player.play_note(nota3,0.1)
    player.play_note(nota,random.uniform(0,1))
    player.play_note(nota,0.1)
    player.play_note(nota2,random.uniform(0,1))
    player.play_note(nota2,0.1)
    player.play_note(nota3,random.uniform(0,1))
    player.play_note(nota3,0.1)
    player.play_note(nota3,0.1)

    # player.play_note(nota3,0.1)
    # player.play_note(nota,0.1)
    # player.play_note(nota2,0.1)
    # player.play_note(nota3,0.1)









