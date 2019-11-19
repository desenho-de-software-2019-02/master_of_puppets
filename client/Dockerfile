FROM node:11

WORKDIR /front

COPY . /front

RUN yarn global add @angular/cli

RUN npm install

CMD ng serve --host=0.0.0.0
