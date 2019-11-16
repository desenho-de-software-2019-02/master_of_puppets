bundle check || bundle update

gem install rails

while ! pg_isready -h users-db -p 5432 -q -U postgres; do
	>&2 echo "postgres is unavailable"
	sleep 1
done

>&2 echo "postgres is up"

if !(bundle exec rake db:migrate); then
  >&2 echo "=========== DATABASE DOES NOT EXIST... yet"
	bundle exec rake db:create
	>&2 echo "=========== DATABASE CREATED"
	bundle exec rake db:migrate
	>&2 echo "=========== DATABASE MIGRATED"
  bundle exec rake db:seed
  >&2 echo "=========== DATABASE SEEDED"
else
  >&2 echo "=========== DATABASE EXIST.... yay"
	bundle exec rake db:migrate
	>&2 echo "=========== DATABASE MIGRATED (already exists)"
fi

if (cat ./tmp/pids/server.pid); then
  >&2 echo "SERVER PID EXISTS... REMOVING..."
  rm ./tmp/pids/server.pid
  >&2 echo "SERVER PID REMOVED"
else
  >&2 echo "SERVER PID DO NOT EXISTS... yay"
fi

echo 'Starting server...'

bundle exec rails s -p 3000 -b '0.0.0.0'
