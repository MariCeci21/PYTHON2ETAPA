Windows PowerShell
Copyright (C) Microsoft Corporation. Todos os direitos reservados.


PS H:\PYTHON\Etapa2\Aula15-API> ^C
PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Diario do Marcos","autor":"Ana Clara","ano":2025}'
>>


ano          : 2025
autor        : Ana Clara
data_criacao : 2026-07-29 09:34:51.516158
id           : 4
titulo       : Diario do Marcos



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Amores","autor":"Ana Luiza","ano":2015}'
>>


ano          : 2015
autor        : Ana Luiza
data_criacao : 2026-07-29 09:37:19.743439
id           : 5
titulo       : Amores



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Poderes","autor":"Ana Luiza","ano":2016}'
>>


ano          : 2016
autor        : Ana Luiza
data_criacao : 2026-07-29 09:37:47.869753
id           : 6
titulo       : Poderes



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Poderes","autor":"Ana Laura","ano":2017}'
>>


ano          : 2017
autor        : Ana Laura
data_criacao : 2026-07-29 09:38:09.613128
id           : 7
titulo       : Poderes



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Desamores","autor":"Ana Laura","ano":2018}'
>>


ano          : 2018
autor        : Ana Laura
data_criacao : 2026-07-29 09:39:05.802680
id           : 8
titulo       : Desamores



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Diarios","autor":"Ana Laura","ano":2019}'
>>


ano          : 2019
autor        : Ana Laura
data_criacao : 2026-07-29 09:39:23.348690
id           : 9
titulo       : Diarios



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Lupass","autor":"Ana Julia","ano":2019}'
>>


ano          : 2019
autor        : Ana Julia
data_criacao : 2026-07-29 09:39:45.274737
id           : 10
titulo       : Lupass



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Parque","autor":"Ana Paula","ano":2020}'
>>


ano          : 2020
autor        : Ana Paula
data_criacao : 2026-07-29 09:40:23.549442
id           : 11
titulo       : Parque



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"GG Game","autor":"Maria Paula","ano":2021}'
>>


ano          : 2021
autor        : Maria Paula
data_criacao : 2026-07-29 09:41:03.502047
id           : 12
titulo       : GG Game



PS H:\PYTHON\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Carlo Acutis","autor":"Maria Cecilia","ano":2022}'
>>


ano          : 2022
autor        : Maria Cecilia
data_criacao : 2026-07-29 09:41:26.956323
id           : 13
titulo       : Carlo Acutis



PS H:\PYTHON\Etapa2\Aula15-API>