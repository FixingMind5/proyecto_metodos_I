# Proyecto final de métodos numéricos I

El proyecto está completamente desarrollado en python.
Se programaron los siguientes métodos

1. Método de Newton
1. Método de la secante
1. Método de Gauss Jordan particionado
1. Método de intercambio
1. Método de Doolittle

### Para poder visualizar el proyecto necesitas:

1. Clonar el repositorio
```cli
git clone https://github.com/FixingMind5/proyecto_metodos_I.git
```

2. Inicializar un ambiente virtual ya sea con virtualenv o con anaconda, depende cuál uses.

Con virtualenv (para instalar y usar virtualenv siga [esta documentación](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/))
```cli
python3 -m virtualenv .venv
```

Con anaconda (para instalar y usar anaconda siga [esta documentación](https://docs.anaconda.com/anaconda/install/))
```cli
conda create --name myenv
```

3. Instalar las dependencias
```cli
pip3 install -r requirements.txt
```

4. Correr el archivo `main.py` y seguir las instrucciones
````
python3 main.py
````

<span style="color:ref">Si te saltas algún paso no correrá satisfactoriamente el programa</span>.

##### Finalmente
Siéntete con la libertad de contribuir con el proyecto, la verdad le falta mucho, cosas como:
* Organizar los módulos en carpetas (también los tests)
* Corregir algunas validaciones con los tipos de objetos
* Arreglar algunos parámetros que quedaron sueltos por ahí
* Crear una clase del tipo fracción para no manejar tantos decimales en las matrices

Entre muchas otras cosas que seguro encontrarás en qué contribuir. Muchas gracias. 😉
