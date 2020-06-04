As informações apresentadas neste repositório são de responsabilidade de seus autores. Esta iniciativa é uma produção independente que visa apresentar de diferentes formas as informações repassadas pelas prefeituras municipais acerca da evolução da COVID-19. Junte-se à nós e colabore!

### Instrução para construção do CSV:   

| data | confirmados | recuperados | mortes_residencia | mortes_ocorrencia | isolamento | restricao |  
| --- | --- | --- | --- | --- | --- | --- |  
| yyyy-mm-dd | decimal | decimal | decimal | decimal | porcento | ver tipos abaixo |  

#### Tipos de restrições:
- 0 => Comércio aberto
- 1 => Comércio fechado (exceto serviços essenciais)
- 2 a 23 => Horário do toque de recolher
- 24 => Saída do toque de recolher
- 50 => Entrada no lockdown
- 51 => Saída do lockdown
- 61 => Fase 1 de abertura do comércio
- 62 => Fase 2 de abertura do comércio
- 63 => Fase 3 de abertura do comércio
- 64 => Fase 4 de abertura do comércio
- 65 => Fase 5 de abertura do comércio

#### Sobre as tabelas de mortes
A SESAB alterou a forma de divulgação do número de mortos. Por isso, o número de mortos deverá ser apresentado nas colunas `mortes_residencia` e `mortes_ocorrencia` assim que o município disponibilizar essa forma de apresentação dos dados.

#### Linha de expectativa
Fonte da linha de expectativa: https://github.com/cidacslab/Mathematical-and-Statistical-Modeling-of-COVID19-in-Brazil
- O repositório utiliza Aprendizagem de Máquina que leva em consideração a quantidade de casos confirmados. O modelo utilizado é o **Susceptible-Infected-Recovered (SIR)**.

## Lista de Cidades
- Feira de Santana (Responsável: Flávio Pereira - IFBA):
  - Colab: https://github.com/covidba/covid/blob/master/covid19_feira_de_santana.ipynb
- Ilhéus (Responsável: Allan Alves - IFBA):
  - Colab: https://github.com/covidba/covid/blob/master/covid19_ilheus.ipynb
- Itabuna (Responsável: Allan Alves - IFBA):
  - Colab: https://github.com/covidba/covid/blob/master/covid19_itabuna.ipynb
- Jequié (Responsável: Ramon Fontes - IFBA): 
  - Colab: https://github.com/covidba/covid/blob/master/covid19_jequie.ipynb
- Salvador (Responsável: Ramon Fontes- IFBA):
  - Colab: https://github.com/covidba/covid/blob/master/covid19_salvador.ipynb
- Vitória da Conquista (Responsável: Ramon Fontes - IFBA): 
  - Colab: https://github.com/covidba/covid/blob/master/covid19_vitoria_da_conquista.ipynb


# Jequié  
![](https://drive.google.com/uc?export=view&id=1--7gWAbvW57H4hPYLVNNDfe1liSJMdGQ)
![](https://drive.google.com/uc?export=view&id=1-4ajTz45wsrtxxV-JPjSK0JCx51cdE8P)

# Vitória da Conquista
![](https://drive.google.com/uc?export=view&id=1-BPW6LzbxpqJyytyVgxiEQPtgEsw5Sj3)
![](https://drive.google.com/uc?export=view&id=1-HBgOUsMP-Cc0MhUlwbXQmWXrahisJK_)

# Salvador
![](https://drive.google.com/uc?export=view&id=1lfhHG3Uw49iXTS3KstmyFlR2xaFItWCI)
![](https://drive.google.com/uc?export=view&id=1-1RagKSDoxavOP4-QngCp5XxU9zMqJ6X)

# Bahia
![](https://drive.google.com/uc?export=view&id=1--s_e86HJ5OkyjnQIciFwDm7hOLWFPYH)
![](https://drive.google.com/uc?export=view&id=1--walWIG8ahzWuXSxo6ZYgh-4G1W199U)
![](https://drive.google.com/uc?export=view&id=1yssvgzc7ST5JTODHGPaxXaxJBQXDkzA_)
