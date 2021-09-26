## CRYPTOCURRENCY QUERY #

### Tecnologías usadas

* Django
* MongoDB
* Python
* Json

Pasos para cargar el proyecto en tu pc 

* Linux

```console
$ git clone https://github.com/Pgragerai/cryptocurrency.git
```

Una vez clonado el proyecto debemos activar el entorno virtual 

```console
$ cd myenv/Scripts
$ activate
```

En el caso que se quiera desactivar el entorno virtual. En la misma ruta que la anterior consola ejecutamos lo siguiente 

```console
$ deactivate
```

En la ruta raíz del proyecto, ejecutamos el siguiente comando para instalar todo lo necesario para la app

```console
$ pip install -r requirements.txt
```

Debemos tener una base de datos mongo en el equipo y poner la configuración correspondiente en el apartado “DATABASES” del fichero settings.py

![alt text](project-img/settings.png)

## Proyecto

Una vez realizado los paso anteriores, lanzaremos la app

```console
$ python manage.py runserver   
```

Si todo ha ido bien debe aparecer en nuestra consola algo similar

![alt text](project-img/consola1.png)

Si se quiere ejecutar los test usaremos el siguiente comando

```console
$ python manage.py test 
```

La app consta de cuatro peticiones: 

* Carga de datos
* Estadísticas de compras
* Estadísticas de ventas
* Estadísticas generales

## Carga de datos

Para realizar la carga de datos debemos llamar a la siguiente dirección con la app levantada. Para realizar la llamada correctamente debemos pasarle como parámetro un símbolo compuesto de una criptomoneda y una moneda real, en este ejemplo “ETH-USD”, a través de coin.

http://127.0.0.1:8000/crypto/data_load?coin=ETH-USD/

Si ha ido bien la consola mostrará lo siguiente

```console
[26/Sep/2021 14:35:38] "GET /crypto/data_load?coin=ETH-EUR/ HTTP/1.1" 201 0
```

## Estadísticas de compras

Para obtener las estadísticas de compras debemos consultar la siguiente URL. Para indicarle que símbolo compuesto por una criptomoneda y una moneda real, usaremos el parámetro coin (ejemplo “ETH-EUR”)

http://127.0.0.1:8000/crypto/statistics_bids?coin=ETH-EUR

Ejemplo de JSON devuelto por la llamada a la URL

```json
{
"bids":
    {
    "average_value": 2100.74,
    "greater_value": {
        "px": 2564.41, 
        "qty": 11.38866479, 
        "num": 12745218079, 
        "value": 29205.21
         }, 
    "lesser_value": {
        "px": 1465.34,
        "qty": 0.03999596,
        "num": 12619708063,
        "value": 58.61
        },
    "total_qty": 68,
    "total_px": 154431
    }
}
```

## Estadísticas de ventas

Para obtener las estadísticas de ventas debemos consultar la siguiente URL. Para indicarle que símbolo compuesto por una criptomoneda y una moneda real, usaremos el parámetro coin (ejemplo “BTC-EUR”)

http://127.0.0.1:8000/crypto/statistics_asks?coin=BTC-EUR

Ejemplo de JSON devuelto por la llamada a la URL

```json
{
"asks": {
    "average_value": 6427.85,
    "greater_value": {
        "px": 1000000.0,
        "qty": 0.07539071,
        "num": 8288657536,
        "value": 75390.71
        },
    "lesser_value": {
        "px": 40000.0,
        "qty": 0.0006,
        "num": 8405443865,
        "value": 24.0},
    "total_qty": 12,
    "total_px": 4994609
    }
}
```

## Estadísticas generales

Si se desea consultar las estadísticas generales realizaremos la siguiente consulta a la siguiente dirección 

http://127.0.0.1:8000/crypto/statistics

Ejemplo de JSON devuelto por la llamada a la URL

```json
{
"ETH-USD": {
    "bids": {
        "count": 61,
        "qty": 174,
        "value": 473849
        }, 
    "asks": {
        "count": 65,
        "qty": 185,
        "value": 595294
        }
    },
    "ETH-EUR": {
        "bids": {
            "count": 74,
            "qty": 242,
            "value": 629304
            },
        "asks": {
            "count": 77,
            "qty": 347,
            "value": 1088049
        }
    }
}
```

Si surge algún problema con Django puede consultar el siguiente enlace

https://tutorial.djangogirls.org/es/python_installation/


