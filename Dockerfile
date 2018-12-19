FROM node:8.12.0

RUN git clone -b NodeMongo https://github.com/airavata-courses/kr2.git

WORKDIR /kr2/

RUN rm -rf node_modules package-lock.json

RUN npm install

EXPOSE 30001

CMD [ "npm", "start" ]
