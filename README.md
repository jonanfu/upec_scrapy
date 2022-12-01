
# Scrapy upec

Scrapy para extraer la información del repositorio de la UPEC

## Autor

- [@Jonathan Narvàez Urresta](https://www.github.com/jonanfu)


## Correr el projecto

Clonar el proyecto

```bash
  git clone git@github.com:jonanfu/upec_scrapy.git
```

 directorio

```bash
  cd upec_scrapy
```

Crear entorno virtual

```bash
  python -m venv venv
```

activar entorno virtual

Windows

```bash
  .venv/lib/activate
```
Mac o Linux

```bash
  source venv/bon/activate
```
instalar dependencias
```bash
  pip install -r requirements.txt
```
ir al directorio upec_scrapy

```bash
  cd upec_scrapy
```
correr el scrapy

```bash
  scrapy crawl repository
```