# Usar una imagen base de Node.js
FROM node:23.5-alpine3.20

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar pnpm globalmente
RUN npm install -g pnpm

# Copiar el archivo package.json y pnpm-lock.yaml (si existe)
COPY package.json pnpm-lock.yaml* ./

# Instalar dependencias usando pnpm
RUN pnpm install

# Instalar Angular CLI globalmente
RUN pnpm add -g @angular/cli

# Instalar librerías adicionales
RUN pnpm add @angular/material @angular/cdk @angular/animations primeflex dotenv

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 4200

# Comando por defecto para mantener el contenedor en ejecución
CMD ["tail", "-f", "/dev/null"]