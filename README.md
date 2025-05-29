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

[cómo realizar un fork](https://github.com/djesuscp/WAD_Practice3.1)
