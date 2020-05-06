#!/bin/bash
echo "Criando o pacote do tema..."
zip -r klass.zip webinar-01/theme/klass
aws s3 cp klass.zip s3://$1 --profile $2
echo "Pacote criado e armazenado com sucesso!"
