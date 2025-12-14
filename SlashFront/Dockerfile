FROM node:20-alpine AS builder

ENV NODE_ENV=production

WORKDIR /app

COPY package*.json ./

COPY . .

RUN npm run install

