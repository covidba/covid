As informações apresentadas neste repositório são de responsabilidade de seus autores. Esta iniciativa é uma produção independente que visa apresentar de diferentes formas as informações repassadas pelas prefeituras municipais acerca da evolução da COVID-19. Junte-se à nós e colabore!

### Instrução para construção do CSV:   

| data | confirmados | recuperados | mortes_residencia | mortes_ocorrencia | restricao |  
| --- | --- | --- | --- | --- | --- |  
| yyyy-mm-dd | decimal | decimal | decimal | decimal | ver tipos abaixo |  

#### Tipos de restrições:
- 0 => Comércio aberto
- 1 => Comércio fechado (exceto serviços essenciais)
- 2 a 23 => Horário do toque de recolher
- 24 => Saída do toque de recolher
- -1 => Entrada no lockdown
- -0 => Saída do lockdown

#### Sobre as tabelas de mortes
A SESAB alterou a forma de divulgação do número de mortos. Por isso, o número de mortos deverá ser apresentado nas colunas `mortes_residencia` e `mortes_ocorrencia` assim que o município disponibilizar essa forma de apresentação dos dados.

#### Linha de expectativa
Fonte da linha de expectativa: https://github.com/cidacslab/Mathematical-and-Statistical-Modeling-of-COVID19-in-Brazil
- O repositório utiliza Aprendizagem de Máquina que leva em consideração a quantidade de casos confirmados. O modelo utilizado é o **Susceptible-Infected-Recovered (SIR)**.

## Lista de Cidades
- Ilhéus (Responsável: Allan Alves - IFBA):
  - Colab: https://github.com/covidba/covid/blob/master/covid19_ilheus.ipynb
- Itabuna (Responsável: Allan Alves - IFBA):
  - Colab: https://github.com/covidba/covid/blob/master/covid19_itabuna.ipynb
- Jequié (Responsável: Ramon Fontes - IFBA): 
  - Colab: https://github.com/covidba/covid/blob/master/covid19_jequie.ipynb
- Vitória da Conquista (Responsável: Ramon Fontes - IFBA): 
  - Colab: https://github.com/covidba/covid/blob/master/covid19_vitoria_da_conquista.ipynb


# Jequié  
![](https://drive.google.com/uc?export=view&id=1BAYAVD6yGvQ9n54_x22u71y7EwJu8T7L)
![](https://drive.google.com/uc?export=view&id=1AwNiHHo8zKp7q2p53o5Lgb1rBsJ8YXdz)

# Vitória da Conquista
![](https://drive.google.com/uc?export=view&id=1-4PokJv6GlioL4uE8ljDoe4OpFx_UGQn)
![](https://drive.google.com/uc?export=view&id=1-9KrclqY9ajCwL86wcVJasA_20rq2xGW)

# Bahia
![](https://drive.google.com/uc?export=view&id=1--s_e86HJ5OkyjnQIciFwDm7hOLWFPYH)
![](https://drive.google.com/uc?export=view&id=1--walWIG8ahzWuXSxo6ZYgh-4G1W199U)
