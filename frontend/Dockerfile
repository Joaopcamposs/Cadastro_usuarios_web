FROM node:lts

# set work directory
WORKDIR /frontend

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install dependencies
RUN npm install

# copy project
COPY . .

EXPOSE 3000

# build app for production with minification
CMD npm start
