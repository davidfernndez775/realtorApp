# Usar una imagen base de Node.js basada en Alpine
FROM node:22.14-alpine3.20

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

# Crear directorios con los permisos adecuados
RUN install -o appuser -g appgroup -d /app /pnpm /app/.pnpm-store

# Configurar pnpm antes de cambiar de usuario
RUN pnpm config set store-dir /app/.pnpm-store && \
    pnpm config set prefer-offline true && \
    pnpm config set fetch-retries 100000 && \
    pnpm config set fetch-retry-mintimeout 100 && \
    pnpm config set fetch-retry-maxtimeout 100

# Instalar Angular CLI globalmente como root
RUN pnpm add -g @angular/cli

# Copiar archivos de dependencias con permisos correctos
COPY --chown=appuser:appgroup package.json pnpm-lock.yaml* ./

# Cambiar al usuario no root
USER appuser

# Instalar dependencias respetando las versiones en package.json
RUN pnpm install --frozen-lockfile --prefer-offline

# Copiar el resto del código de la aplicación
COPY --chown=appuser:appgroup . .

# Exponer el puerto para Angular
EXPOSE 4200

# Mantener el contenedor en ejecución
CMD ["tail", "-f", "/dev/null"]
