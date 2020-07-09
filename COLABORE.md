## Quem sou eu?

Meu nome é Ramon Fontes, sou professor da UFRN e procurei criar o **covidba** para apresentar dados estatísticos acerca da evolução da COVID-19 para a população de minha cidade natal e também para algumas outras cidades da Bahia. Dois meses depois após ter criado o **covidba** eu pensei em desenvolver o aplicativo **CovidBR** com o mesmo propósito, mas agora com abrangência nacional. A grande maioria dos dados que apresento no aplicativo tem como fonte https://github.com/wcota/covid19br. Porém, como é sabido que existem divergências entre os dados apresentados pelos estados e municípios, eu habilitei uma opção no aplicativo que permite extrair dados através de colaborações. Nesse caso, algumas pessoas seriam responsáveis por alimentar os dados que os municípios divulgam para a suas populações.


## Como colaborar?

Antes de mais nada você precisa entrar em contato comigo através do meu email ramonreisfontes@gmail.com, pois preciso adicionar seu estado [aqui](https://github.com/covidba/covid/blob/master/estados_fonte.csv) para que o aplicativo reconheça sua contribuição. Você precisa me passar uma URL do github que possua o seguinte padrão github.com/**NOME**/covid. Sugiro que NOME referencie o teu estado de alguma forma, assim como **covidba** referencia a Bahia.

Em seguida, você precisa criar um arquivo chamado de [lista_cidades.csv](https://github.com/covidba/covid/blob/master/lista_cidades.csv) com a lista das cidades que fará parte da colaboração. Você também vai precisar criar um arquivo csv para cada cidade no diretório raiz **/covid** da mesma forma como foi feito com https://github.com/covidba/covid. Esse arquivo csv deverá obedecer a formatação descrita [aqui](https://github.com/covidba/covid#instru%C3%A7%C3%A3o-para-constru%C3%A7%C3%A3o-do-csv).
