# Hotel-Booking-Cancellation

Olá!


Esse notebook 
-------------------------------------------------------------------------------

Esse trabalho apresenta os passos tomados para o projetos de dados em cima do dataset de Hotel booking. É valido comentar que teve uma aproximação diferente para o problema, foi percebido que havia valor em separar o dataset em dois, e fazer um modelo para cada caso, diferente de muitas das vezes que só se utiliza os dados para um modelo unico.
-------------------------------------------------------------------------------
 ------------------------------------------------------------------------------

O objetivo não foi de encontrar os melhore resultados possiveis, por isso as etapas de cross-validation, foi cortada na parte de modelagem por demorar a rodar e não haver disponilização de uma GPU. Para tanto, os algoritmos testados foram montados com seus parametros default/

Nele você encontratará 

*   Os passos da analise exploratória de dados, que conta com limpeza de dados, feature engeneering, uma explicação da separação dos tipos de hotéis, uma analise dos tipos de clientes e seu comportamento

*   Uma sessão de modelagem para hotéis de Resort e outra para hotéis de cida.

*   Os resultado dos testes de algoritmos.

Valem lembrar que essa notebook é um compilado inteiro, no Github tbm está disponibilizado os modelos salvos, um script para treinamento, outro para predição, os dados limpos e os arquivos para deploy. 
