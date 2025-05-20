
#!/bin/bash
while true; do
  docker-compose down
  docker-compose up --build
  sleep 5
done
