---

## title: HTTP-запросы

# Протокол HTTP.


## GET-запрос через Telnet

Для выполнения GET-запроса был использован Telnet. Запрос был отправлен к публичному API `meowfacts.herokuapp.com`.

Команда подключения:

```powershell
telnet meowfacts.herokuapp.com 80
```

Текст HTTP-запроса:

```http
GET / HTTP/1.1
Host: meowfacts.herokuapp.com
```

В результате сервер вернул ответ со статусом `HTTP/1.1 200 OK` и JSON-данными.

![GET через Telnet](/portfolio-hextra/images/http/telnet-get.png)

---

## GET-запрос через Ncat

Для выполнения HTTPS-запроса в CLI был использован `ncat`.

Команда подключения:

```powershell
ncat --ssl postman-echo.com 443
```

Текст HTTP-запроса:

```http
GET /get?name=Tigra HTTP/1.1
Host: postman-echo.com
```

В результате сервер вернул ответ со статусом `HTTP/1.1 200 OK` и JSON-данными.

![GET через Ncat](/portfolio-hextra/images/http/ncat-get.png)

---

## POST-запрос через Ncat

Для отправки POST-запроса через CLI был использован `ncat`. В теле запроса передавались JSON-данные.

Команда:

```powershell
"POST /post HTTP/1.1`r`nHost: postman-echo.com`r`nContent-Type: application/json`r`nContent-Length: 34`r`n`r`n{""name"":""john"",""job"":""programmer""}`r`n" | ncat --ssl postman-echo.com 443
```

Тело запроса:

```json
{"name":"john","job":"programmer"}
```

Сервер успешно обработал запрос и вернул ответ со статусом `HTTP/1.1 200 OK`.

![POST через Ncat](/portfolio-hextra/images/http/ncat-post.png)

---

## GET-запрос через cURL

GET-запрос был выполнен с помощью утилиты `curl`.

Команда:

```powershell
curl.exe https://postman-echo.com/get?name=Tigra
```

В ответе сервер вернул JSON-объект с параметром `name`.

![GET через cURL](/portfolio-hextra/images/http/curl-get.png)

---

## POST-запрос через cURL

POST-запрос был выполнен с помощью `curl`. В запросе использовался заголовок `Content-Type: application/json`, а в теле передавались JSON-данные.

Команда:

```powershell
curl.exe -X POST "https://postman-echo.com/post" -H "Content-Type: application/json" -d "{\"name\":\"john\",\"job\":\"programmer\"}"
```

Тело запроса:

```json
{"name":"john","job":"programmer"}
```

В результате сервер вернул отправленные данные в ответе.

![POST через cURL](/portfolio-hextra/images/http/curl-post.png)

---

## GET-запрос в Postman к API Банка России

Для работы с HTTP API был установлен Postman.

С помощью Postman выполнен GET-запрос к API Банка России для получения курса доллара США за выбранный период.

URL запроса:

```text
https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/06/2026&date_req2=10/06/2026&VAL_NM_RQ=R01235
```

Параметры запроса:

```text
date_req1 = 01/06/2026
date_req2 = 10/06/2026
VAL_NM_RQ = R01235
```

В результате сервер вернул XML-документ со значениями курса доллара США за указанный период. Запрос был выполнен успешно, статус ответа — `200 OK`.

![GET через Postman к API Банка России](/portfolio-hextra/images/http/postman-cbr.png)
