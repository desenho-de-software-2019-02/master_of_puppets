if (cat ./tmp/pids/server.pid); then
  >&2 echo "SERVER PID EXISTS... REMOVING..."
  rm ./tmp/pids/server.pid
  >&2 echo "SERVER PID REMOVED"
else
  >&2 echo "SERVER PID DO NOT EXISTS... yay"
fi

echo 'Starting server...'

bundle exec rails s -p 3000 -b '0.0.0.0'
