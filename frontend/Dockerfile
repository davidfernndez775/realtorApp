# Usar una imagen base de Node.js basada en Alpine
FROM node:23.5-alpine3.20

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar pnpm globalmente como root
RUN npm install -g pnpm

# Crear un usuario no root para ejecutar la aplicación
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Configurar el directorio global de pnpm y su almacenamiento
ENV PNPM_HOME=/pnpm
ENV PNPM_STORE_PATH=/app/.pnpm-store
ENV PATH="$PNPM_HOME:$PATH"

# Crear los directorios de pnpm y asignar permisos
RUN mkdir -p $PNPM_HOME $PNPM_STORE_PATH && \
    chmod -R 777 $PNPM_HOME $PNPM_STORE_PATH && \
    chown -R appuser:appgroup $PNPM_HOME $PNPM_STORE_PATH

# Configurar pnpm antes de cambiar de usuario
RUN pnpm config set store-dir /app/.pnpm-store && \
    pnpm config set prefer-offline true && \
    pnpm config set fetch-retries 100000 && \
    pnpm config set fetch-retry-mintimeout 100 && \
    pnpm config set fetch-retry-maxtimeout 100

# Cambiar la propiedad del directorio de trabajo al usuario no root
RUN chown -R appuser:appgroup /app /pnpm /app/.pnpm-store

# Cambiar al usuario no root
USER appuser

# Copiar el archivo package.json y pnpm-lock.yaml (si existe)
COPY --chown=appuser:appgroup package.json pnpm-lock.yaml* ./

# Instalar dependencias usando pnpm con --prefer-offline
RUN pnpm install --prefer-offline

# Instalar librerías adicionales
RUN pnpm add @angular/material @angular/cdk @angular/animations primeflex dotenv --prefer-offline

# Copiar el resto de los archivos de la aplicación
COPY --chown=appuser:appgroup . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 4200

# Comando por defecto para mantener el contenedor en ejecución
CMD ["tail", "-f", "/dev/null"]