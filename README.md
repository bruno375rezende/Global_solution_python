Alunos: Bruno Lisboa Rezende rm: 562228
ALunos: Rafael Ali Oliveira Khalil rm 561240


Este projeto simula uma solução voltada para preparar jovens e profissionais para o futuro do trabalho, considerando áreas de interesse e tendências tecnológicas, como IA, automação e ambientes híbridos.

Estruturas utilizadas

 Estrutura de entrada
A função coletar_dados() coleta informações do usuário:
- Nome
- Idade
- Área de interesse

Estrutura de repetição
A função coletar_varios_usuarios() utiliza um loop while para permitir a inserção de múltiplos usuários.

Funções
O projeto é modularizado em funções:
- coletar_dados()
- coletar_varios_usuarios()
- criar_dataframe()
- recomendar_carreira()
- mostrar_resultados()

 Função dentro de função
Dentro de coletar_dados(), há a função input_questao() que encapsula a entrada de dados de forma reutilizável.

 Estrutura de condição
Na função recomendar_carreira(), utilizamos if/elif/else para gerar recomendações de carreira baseadas na área de interesse do usuário.

Dataframe
A função criar_dataframe() utiliza a biblioteca pandas para organizar os dados coletados em uma estrutura tabular, facilitando análise e relatórios.

Estrutura de saída
A função mostrar_resultados() exibe o relatório final com recomendações de carreira para cada usuário.

Como usar

1. Clone ou baixe o repositório.
2. Certifique-se de ter o Python e a biblioteca pandas instalados:
```bash
pip install pandas



