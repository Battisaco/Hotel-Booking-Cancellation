
# Deploy de modelos Hotel-Booking-Cancellation

Olá!


-------------------------------------------------------------------------------

Essa sessão é dedicada ao deploy dos modelos, eles se encontra nesse link do google drive:


Ambos os modelos (Resort e city) foram salvos em pickle.

-------------------------------------------------------------------------------
 ------------------------------------------------------------------------------

O ambiente junto com as bibliotecas já estão salvos pelo pipenv, e ao abrir o docker ele fará uma copia interna dos arquivos:

*Pipfile;
*Pipfile.lock;
*Predict_city.py;
*Predict_resort.py
*/Models ~uma pasta com os 2 modelos necessário - Se faz necessária a crianção desse arquivo e colocar os modelos salvos em .bin

Vale lembrar que ele foi construido apartir do ambiente python 3.10-slim


Após construido o docker, ele fará a montagem do "Predict_resort:app" em localhost na porta 9697, caso queira mudar o algoritmo a ser lido, basta mudar o app, para "Predict_city".

Com o Docker rodando, pode ser rodado o Predict_test.py, que possui um json para test do algoritmo de prever booking de RESORT, porem, os dados podem ser mudados para serem testados, dando como saida um print se a reserva é um provavel cancelamento ou não.


