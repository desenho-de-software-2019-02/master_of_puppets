FROM ruby:2.5.7

WORKDIR /mop_user_auth 
COPY . /mop_user_auth

RUN apt-get update -qq && \
  apt-get install -y nodejs postgresql-client && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt update && \
  apt install yarn

COPY Gemfile /events-api/Gemfile

COPY Gemfile.lock /events-api/Gemfile.lock

RUN gem install bundler && bundle install

EXPOSE 3000

CMD ./start-run.sh
