im  jogovelha 
import sys

erroInicializar  = False

jogovelha.iniciazar ()
jogo = jogovelha.tabuleiro()

i f  len(jogo) !=3:
    erroInicializar  = True
else:
     for linha  in jogo:
          if  len(linha) ! = 3:
              erroInicilizar = True
          else:
               for  elemento in linha:
                      if  elemento  !='.':
                          erroInicializar  = True
                          
if                           erroInicializar :
   print  ('Erro!')
   sys                          .exit(1)
else:
   sys.exit(0)
                 
                 
