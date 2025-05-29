# Práctica 7: Introduccción a CI-CD.

## 1. Introducción y conceptos clave a CI-CD.

### 1.1. Significado de CI-CD.

La abreviatura CI/CD corresponde a "Integración Continua" (Continuous Integration) y "Entrega o Despliegue Continuo" (Continuous Delivery/Deployment).

Se puede definir CI/CD como un conjunto de metodologías que ayudan a los equipos de desarrollo de software a automatizar procesos como la integración de código, la ejecución de pruebas y la implementación de aplicaciones de forma ágil y confiable.

CI (Integración Continua): Esta práctica implica incorporar los cambios realizados en el código fuente de una aplicación dentro de un repositorio común. Para asegurar la compatibilidad del nuevo código con el ya existente, es necesario que este pase diversas pruebas (unitarias, de integración, entre otras) que certifiquen su correcto funcionamiento.

CD (Entrega/Despliegue Continuo): Una vez comprobado que el código no presenta errores, el proceso de CD se encarga de automatizar su entrega e implementación en los diferentes entornos definidos, como pueden ser los de pruebas, preproducción o producción.

### 1.2. Pipelines.

Un pipeline es una cadena de pasos automatizados que se ejecutan de manera secuencial con el objetivo de compilar, probar e implementar software. Cada uno de estos pasos se conoce como etapa (stage), y puede incluir actividades como:

- La compilación del código fuente.

- La ejecución de pruebas (unitarias, de integración, entre otras).

- La generación de artefactos, como por ejemplo una imagen de Docker.

- La implementación en distintos entornos, tales como pruebas, preproducción o producción.

Normalmente, los pipelines se configuran mediante archivos escritos en formato YAML.

En el caso de GitHub Actions, estos pipelines reciben el nombre de workflows.

## 2. Objetivos de esta práctica.

- Integración Continua (CI) con GitHub Actions.

Se configurará la automatización de la ejecución de pruebas unitarias cada vez que se realice un push a la rama principal (main).

- Entrega Continua (CD).

Una vez superadas las pruebas unitarias, se automatizará la generación y publicación de una imagen Docker en Docker Hub.

- Despliegue Continuo (CD).

El siguiente paso será automatizar el proceso de despliegue de dicha imagen Docker en la infraestructura de AWS.

## 3. Estructura del proyecto.

Con el objetivo de realizar esta práctica, en primera lugar, se ha realizado un fork de este [repositorio](https://github.com/josejuansanchez/ci-cd-flask). El usuario debe recordar que ya se explicó detalladamente [cómo realizar un fork](https://github.com/djesuscp/WAD_Practice3.1) en una práctica anterior, por lo que se le invita a volver a la misma para recordar el proceso.

Asimismo, se ha clonado el repositorio forkeado en la máquina que servirá para realizar la práctica.

Dicho repositorio consta de:

- Aplicación Flask: ubicada en el directorio: `/src/app.py`.

- Pruebas unitarias situadas en el directorio: `/test/test.py`.

- Archivo `requirements.txt` que alberga las dependencias requeridas para la ejecución de la aplicación y las pruebas unitarias.

- Archivo `.yml` de workflow que se encarga de ejecutar unas pruebas que, si devuelven un resultado correcto, dejarán paso a la creación de la imagen Docker, para finalmente subir la imagen a Docker Hub. Además, el workflow contiene dos disparadores o "triggers": el arranque manual del workflow, y el evento git push.

- Un archivo Dockerfile configurado para específicamente para esta aplicación, en el cual se detallan tanto el entorno, como las instrucciones necesarias para llevar a cabo la construcción de la imagen Docker.

## 4. Instrucciones.

Tal como se ha explicado en otra práctica previa, el usuario deberá seguir las instrucciones del punto 6.2 para [realizar login en Docker Hub a través de la terminal](https://github.com/djesuscp/WAD_Practice5.4_2048.git) de su máquina, así como también deberá tener en cuenta el punto 7.2 para [configurar variables en su repositorio GitHub](https://github.com/djesuscp/WAD_Practice5.4_2048.git).

Una vez realizado esto, en el repositorio forkeado, el usuario podrá acceder al apartado de "Actions" y podrá hacer click sobre el botón "Run workflow" para ejecutar el primer proceso de workflow manual.
