# API FLASK Usando joblauncher 

## Objetivo:

A ideia é ter um projeto padrão para poder facilitar 
o start de novas apis.

## Funcionamento:

Nesse exemplo temos a resposta dos requests padrão de
uma api. 
Porém aqui também temos execuções automatizadas configurando
a frequencia em que fazemos essa tarefa, sem receber nenhuma 
requisição.


## Exemplo:

http://0.0.0.0:8085/api/status

{"message": "Api respondendo com sucesso."}

## Jobloaucher

Esse é responsavel por fazer os processos automaticos. 
Nesse caso configuramos no arquivo job_loacher.py
```
    # Roda o reset todos os dias a 03:00
    scheduler.every().day.at("03:00").do(ClassFunction)
```