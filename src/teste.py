import jogovelha
import sys

erroinicializar=False
jogo=jogovelha.inicializar()

if len(jogo) != 3:
    erroinicializar=True
else:
    for linha in jogo:
        if len(linha) !=3:
            erroinicializar = True
        else:
            for elemento in linha:
                if elemento != '.':
                    erroinicializar = True
if erroinicializar:
    sys.exit(1)
else:
    sys.exit(0)
