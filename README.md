# Monitor-Postura-YOLO
Trabalho em grupo sobre visão computacional com auxilio com IA

Monitor de postura 

Integrantes do grupo:
João Francisco da Silva Malaquias, 
Alber Alberguini Cabral, 
Adryel, 
Darvin do Nascimento Ferreira

🎯 Objetivo da Solução

O objetivo deste projeto é fornecer uma ferramenta de monitoramento preventivo e educativo para usuários que passam longos períodos em frente ao computador. Através da análise de Pose Estimation (Estimativa de Pose), o software identifica padrões posturais prejudiciais, como a inclinação excessiva da cabeça e o desalinhamento dos ombros, promovendo a conscientização ergonômica e auxiliando na prevenção de patologias como a cifose postural e tensões cervicais.

⚠️ Descrição do Problema

O trabalho remoto e o uso prolongado de dispositivos digitais levaram a um aumento significativo nos problemas de postura. A "síndrome da cabeça para frente" e a má postura sentada são causas principais de dores crônicas nas costas e no pescoço.

Muitas vezes, o usuário não percebe que está em uma posição prejudicial até que a dor apareça. Existe uma carência de sistemas acessíveis que utilizem hardware comum (webcams) para fornecer feedback imediato sem a necessidade de sensores vestíveis caros ou consultas constantes a especialistas.

🚀 Como Executar o Projeto

Para rodar o monitor de postura na sua máquina, siga os passos abaixo:

1. Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado em seu sistema.

2. Instalação das Bibliotecas

Abra o seu terminal (ou CMD) e instale as dependências necessárias utilizando o gerenciador de pacotes pip:

pip install ultralytics opencv-python

3. Download do Modelo

Não é necessário baixar o modelo manualmente. Ao executar o código pela primeira vez, a biblioteca Ultralytics fará o download automático do arquivo yolov8n-pose.pt.

4. Execução

Com a webcam conectada, execute o script:

python seu_arquivo.py

5. Interação

    O programa abrirá uma janela com o feed da sua câmera.
    As marcações verdes indicam Boa Postura.
    As marcações vermelhas indicam Má Postura ou Corcunda.
    Para encerrar o monitoramento, pressione a tecla 'q' no teclado.
