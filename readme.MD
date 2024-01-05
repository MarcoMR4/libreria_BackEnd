## Recomendaciones. 

. Activar entorno virtual: .\venv\scripts\activate 

. Instalar librerias:    pip install -r requirements.txt

. Base de datos local en archivo db.sqlite3 

### Endpoints

**Registro de usuario**
localhost:8000/api/auth/register/

request
```
{
    "name" : "Nombre de usuario",
    "email" : "ejemplo1@mail.com",
    "password" : "12345"
}
```

**Login**
localhost:8000/api/auth/login/

request:
```
{
    "email" : "ejemplo1@mail.com",
    "password" : "12345"
}
```

**delete books**

localhost:8000/api/books/(colocar id de libro)/