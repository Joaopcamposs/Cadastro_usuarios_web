FROM node:lts-alpine

# set work directory
WORKDIR /frontend

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install dependencies
RUN npm install

# copy project
COPY . .

# expose the 3000 port from the localhost system
EXPOSE 3000

# build and run app
CMD ["npm", "start"]
