FROM node:11

WORKDIR /front

COPY . /front

RUN npm install @angular/cli

RUN npm install --save-dev @angular-devkit/build-angular

RUN npm install

CMD ng serve --host=0.0.0.0
