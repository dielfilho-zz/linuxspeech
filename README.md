# Script para reconhecimento de voz em ambiente GNU/Linux

# Depêndencias:
	- Python 2.7 +
	- PyAudio
  	- SpeechRecognition 3.2.0 : https://github.com/Uberi/speech_recognition

# Modo de uso:
 	- Adicione uma NOVA linha no arquivo .actions
 	- Ex: {"voiceCommand":"open spotify", "args":"spotify", "active": true}
 		- Voice Command: Comando de voz a ser reconhecido
    		- Args: Comando que será executado no terminal
    		- Active: Informa se o comando poderá ser executado ou não
	- Comandos padrões:
		- Turn off : Desabilita a execução das funções
		- Turn on  : Habilita a execução das funções
		- Goodbye  : Finaliza o script 
	- Execute python voice_main.py no seu terminal
	- OBS: É necessário ter acesso a internet


 Em caso de dúvidas entre em contato pelo e-mail stringdanielf@gmail.com
