
Link do vídeo explicativo: https://drive.google.com/file/d/1SkAbFOZo7k_HGviJRsaa6TJFrnZOqqJz/view?usp=sharing

Passo 1 - conectar na máquina virtual via SSH

Passo 2 - criar uma pasta que indique a finalidade da máquina, por exemplo: client1, client2 ou server...

Passo 3 - criar dentro da pasta 5 arquivos .py conforme abaixo

	mkdir client1		# criar pasta
	cd client1		# abrir pasta
	touch client.py	# criar arquivos
	touch constRPC.py	
	touch dbclient.py
	touch rpc3.py
	touch server.py

Passo 4 - em cada pasta há os códigos necessários para a execução da atividade, é necessário realizar a alteração no arquivo client.py adicionando o IP da máquina que está sendo utilizada.

Passo 5 - realizar a alteração no arquivo constRPC.py informando o endereço IP das máquinas que você criou e definindo as portas que você criou no seu grupo de segurança... os valores que aparecem no exemplo abaixo e no arquivo constRPC.py são referentes a minha simulação...

	OK       = '1'
	ADD      = '2'
	APPEND   = '3'
	GETVALUE = '4'
	CREATE   = '5'
	STOP     = '6'
	HOST    = '172.31.93.109'	# adicionar o IP do servidor
	PORT    = 12306		# adicionar a porta do servidor
	CLIENT1 = 12307		# adicionar a porta do cliente 1
	CLIENT2 = 12308		# adicionar a porta do cliente 2
	HOSTCL1 = '172.31.87.243'	# adicionar IP cliente 1
	HOSTCL2 = '172.31.84.169'	# adicionar IP cliente 2

Passo 6 - dentro da pasta criada, abrir cada arquivo com o comando [vi nomeDoArquivo.py] e copiar o código correspondente, lembre de conferir o IP

	touch nomeDoArquivo.py 	# criar um arquivo .py
	vi nomeDoArquivo.py		# abrir o arquivo para que possa ser editado
	
Obs: Para editar o arquivo aberto, basta clicar na letra "i" do teclado, a palavra INSERT será exibida na última linha do terminal... Assim que as edições foram concluídas, basta clicar em "Esc" (observe que a palavra INSERT não aparece mais) e em seguida digite ":wq" dessa forma o arquivo será salvo e você voltará para o local onde estava.
	
Passo 7 - Assim que todas as configurações forem realizadas, é preciso iniciar o servidor e os clientes:

	- na máquina do servidor execute: python3 rpc3.py, observe que o servidor será iniciado e ficará em espera
	- na máquina do cliente 2 execute o mesmo comando, observe que ele ficará aguardando dados...
	- na máquina do cliente 1 execute o mesmo comando, observe que será criado uma referência remota que permitirá a comunicação do cliente 1 e 2 com o servidor.
	

Dica: Caso ocorra o erro "OSError: [Errno 98] Address already in use" então a conexão não foi finalizada... nesse caso execute o seguinte comando:

	ps -fA | grep python
	
	Esse comando apresenta todos os processos com o padrão de correspondência python, será possível ver quantos arquivos rpc3.py ainda estão em execução..

	Após identificar os processos, copie o PID (número que estárá na frente do nome do usuário ubuntu) e execute o comando:
	
	kill -9 numeroDoProcesso
	

Depois disso, pode executar normalmene o comando python3 rpc3.py...

Fique a vontade para solucionar esse problema ;)
	
	




