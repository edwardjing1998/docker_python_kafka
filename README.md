# the process to set up repository - docker_python_kafka in github and commit the source codes.
-- git init (.git folder is created in the local in the root folder of application) 
-- git add . (stage the current changes for next commit in the local git repository) 
-- git commit -m "Initial commit of docker_python_kafka application" (This snapshots your current state in your local Git repo.) 
-- git remote add origin https://github.com/edwardjing1998/docker_python_kafka.git (Link Your Local Repo to GitHub) 
-- git push -u origin main (git push -u origin main)

# the process to clone the repository:
-- git clone https://github.com/edwardjing1998/docker_python_kafka.git

# File structure 

docker_python_kafka/
├── app/
│   ├── __init__.py
│   ├── main.py            # (Provided above)
│   ├── kafka-producer.py
│   ├── kafka-consumer.py
├── Dockerfile             # (For building the python-app image)
├── docker-compose.yaml    # (Coordinates Zookeeper, Kafka, Python App)
├── requirements.txt       # (At least flask, kafka-python, etc.)
└── README.md              # (Optional documentation)

# Build and start application containers:

-- docker-compose build (build images i.e. python-app image)
-- docker-compose up (pull images i.e. Kafka and Zookeeper from registries; create and start containers i.e. kafka, zookeeper and kafka-python)
-- docker-compose up --build -d (it will include the 2 process as the above 2 process)

# Stopping & Cleanup:

-- docker-compose down (stop all containers)
-- docker-compose down --rmi all (This stop containers and removes images)

# the process to create branch to push the changes into new branch

-- Make sure you are on the main (or master) branch
git checkout main

-- Pull the latest changes from remote main branch (optional but recommended)
git pull origin main

-- Create and switch to a new branch for your changes
git checkout -b feature/my-new-branch

-- push the new changes into feature/my-new-branch
git add .
git commit -m "make README.md changes"

-- Push Your New Branch to the Remote Repository
git push -u origin feature/my-new-branch



