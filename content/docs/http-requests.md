---
title: HTTP-запросы
---

# Протокол HTTP. Клиент-серверное взаимодействие

## GET-запрос через Telnet

Для выполнения GET-запроса был использован Telnet.

Команда подключения

```text
telnet meowfacts.herokuapp.com 80
```

Запрос

```text
GET / HTTP/1.1
Host: meowfacts.herokuapp.com
```

Сервер вернул ответ со статусом 200 OK и JSON-данными.

![GET через Telnet](/portfolio-hextra/images/http/telnet-get.png)

---

## GET-запрос через Ncat

Для выполнения HTTPS-запроса использовался Ncat.

Команда подключения

```text
ncat --ssl postman-echo.com 443
```

Запрос

```text
GET /get?name=Tigra HTTP/1.1
Host: postman-echo.com
```

Сервер вернул ответ со статусом 200 OK.

![GET через Ncat](/portfolio-hextra/images/http/ncat-get.png)

---

## POST-запрос через Ncat

Для отправки POST-запроса использовался Ncat.

Команда

```text
"POST /post HTTP/1.1`r`nHost: postman-echo.com`r`nContent-Type: application/json`r`nContent-Length: 34`r`n`r`n{""name"":""john"",""job"":""programmer""}`r`n" | ncat --ssl postman-echo.com 443
```

Тело запроса

```text
{"name":"john","job":"programmer"}
```

Сервер успешно обработал запрос и вернул ответ со статусом 200 OK.

![POST через Ncat](/portfolio-hextra/images/http/ncat-post.png)

---

## GET-запрос через cURL

Команда

```text
curl.exe https://postman-echo.com/get?name=Tigra
```

Сервер вернул JSON-ответ.

![GET через cURL](/portfolio-hextra/images/http/curl-get.png)

---

## POST-запрос через cURL

Команда

```text
curl.exe -X POST "https://postman-echo.com/post" -H "Content-Type: application/json" -d "{\"name\":\"john\",\"job\":\"programmer\"}"
```

Тело запроса

```text
{"name":"john","job":"programmer"}
```

Сервер успешно обработал запрос и вернул JSON-ответ.

![POST через cURL](/portfolio-hextra/images/http/curl-post.png)

---

## GET-запрос в Postman к API Банка России

Для получения курса валют был использован Postman.

URL запроса

```text
https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/06/2026&date_req2=10/06/2026&VAL_NM_RQ=R01235
```

Параметры

```text
date_req1 = 01/06/2026
date_req2 = 10/06/2026
VAL_NM_RQ = R01235
```

Сервер вернул XML-документ с курсом доллара США за выбранный период.

![GET через Postman к API Банка России](/portfolio-hextra/images/http/postman-cbr.png)
