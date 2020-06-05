# AWS Brasil - Conteúdo da série de Webinars para Educação apresentandos em 2020

## Serverless - Modernizando o seu LMS/EAD com serviços gerenciados da AWS (04/06)

Para esse webinar criamos uma API desenvolvida em Python utilizando **api gateway** e **lambda**, e **desacoplada** da nossa aplicação Moodle (https://moodle.awsunicorn.com). Essa API efetua consultas na base de dados do Moodle e envia notificações para os alunos através do serviço **Amazon SNS**. Essa arquitetura é uma evolução da arquitetura apresentada no webinar passado (webinar-05) onde mudamos ambos serviços que rodavam em um unico container para um serviço ainda mais desacoplado onde temos funções como serviço e servidores gerenciados pela AWS. Você pode visualizar as funcionalidades da API através dos seguitnes comandos:

```
curl -X GET https://fblgbivqgk.execute-api.us-east-1.amazonaws.com/v1/get-students/

curl -X POST https://fblgbivqgk.execute-api.us-east-1.amazonaws.com/v1/notify-students
```

_Obs.: Esse serviço que estamos criando é para fins de demonstração. Para não sobrecarregar a base de dados poderiamos criar uma Read Replica e para não criar inconsistência no banco de dados não deve ser feita nenhuma escrita._
