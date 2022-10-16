FROM node:16
WORKDIR /app 
COPY package-lock.json .
COPY package.json .
RUN npm install
COPY . .

RUN chown -R node /app/node_modules
USER node