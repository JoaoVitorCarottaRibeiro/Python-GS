João Vitor Carotta Ribeiro - RM 555187

Diego Eleutério Fadul da Costa - RM 557218

Detalhes do projeto Econect:

Para realizar o projeto em python, criamos uma inteligência artificial que futuramente foi integrada ao nosso site via FastAPI.

Essa IA foi treinada com base em um banco de dados pegando valores em R$ e consumo de energia limpa em kW. Depois lemos essa base de dados via pandas e criamos o modelo de machine learning com a biblioteca sklearn, pegando seu modelo linear, o modelo de teste e o r2_score, que faz uma verificação de acertividade do modelo treinado. Definimos x e y como eixos para serem treinados com base no nome da coluna da base de dados, depois, importamos com pickle a IA já treinada.

Carregando o modelo treinado em um arquivo app.py elaboramos uma função que calculo o consumo com base no predict da IA e depois só fizemos uma estilização simples da página com streamlit.
Depois fizemos a verificação do botão de calcular com base no tipo de energia, onde, ele multiplica o valor do predict pelo valor fixo de cada energia, resultando em  um valor muito próximo do que vemos na realidade.

Para ver a IA funcionando na prática instale o python em seu dispositivo, importe a biblioteca streamlit, abra o terminal e digite: streamlit run app.py

Outros scripts realizados já foram explicados dentro do arquivo analise.ipynb
