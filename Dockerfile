FROM node:18

WORKDIR /api

COPY package*.json ./
COPY tsconfig.json ./
COPY usersDB.json ./
RUN npm ci

COPY . .
RUN npm run build

CMD npm run start
