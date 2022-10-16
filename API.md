# API Documentation for URL Shortener

## Create Shortened URL object
POST `shortenedurls/`
```
{
    "long_url": "http://www.example.com"
}
```

RESPONSE HTTP 201 Created:
```
{
    "long_url": "http://wwww.example.com",
    "short_url": "http://localhost:8000/J8lWEn"
}
```

</br>

---

## Redirect to URL from shortened URL
GET: `/{code}`
(where {code} is a unique id from 'short_url')

RESPONSE HTTP 302 FOUND