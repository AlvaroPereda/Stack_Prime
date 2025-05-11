# Práctica 5: Configuración de un entorno de clúster con Docker

**Alumno:** Álvaro Pereda Sánchez

**Calificación:** /10

He elegido el apartado D del [enunciado](./Practica5.pdf)

## Comandos utilizados

A continuación se describen los comandos esenciales para configurar, desplegar, visualizar y limpiar el entorno de clúster. 
Todos estos comandos se deben realizar desde la carpeta raiz del proyecto.

### Construcción del entorno

```bash
docker compose build
```

Este comando construye los contenedores definidos en el archivo `docker-compose.yaml`.

### Despliegue del clúster

```bash
docker stack deploy -c docker-compose.yaml mystack
```

Este comando despliega el stack definido con Docker Compose bajo el nombre `mystack`.

Si se quiere modificar la cantidad de réplicas worker se debe cambiar el valor definido en el archivo [.env](./.env)

### Visualización de logs

```
docker service logs -f mystack_worker
```

Permite observar cómo se están ejecutando los distintos contenedores `worker`, con los parámetros asignados a cada uno para su cálculo.

### Eliminación del stack

```
docker stack rm mystack
```

Este comando elimina el stack desplegado.

### Eliminación de imágenes

Una vez que el stack ha sido eliminado, se pueden borrar las imágenes con el siguiente comando:

```
docker rmi worker; docker rmi coordinator
```

Esto asegura que las imágenes de los servicios `worker` y `coordinator` sean eliminadas completamente.

---
