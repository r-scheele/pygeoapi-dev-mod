## Simple guide to get started using OPAL

This tutorial will teach you to how to get started using OPAL with a docker-compose command.


### Step 1: Edit the docker-compose.yml file for your local setup

````
  opal_server:
    environment:
      - OPAL_POLICY_REPO_URL=<YOUR REPO URL>
      # SSH key is only required for private repositories.
      - OPAL_POLICY_REPO_SSH_KEY=<Your SSH key>
      # in this example we will use a polling interval of 30 seconds to check for new policy updates (git commits affecting the rego policy).
      # however, it is better to utilize a git *webhook* to trigger the server to check for changes only when the repo has new commits.
      - POLICY_REPO_POLLING_INTERVAL=<interval in seconds>

````
Connecting to GitHub with SSH is pretty simple, you can check <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh" target="_blank">Here</a>  for a guide.

### Step 2: run docker compose to start the opal server and client

This one command will run a working configuration of OPAL server and OPAL client on your machine:

```
docker-compose up
```

The `docker-compose.yml`file is running 3 containers: Broadcast channel, OPAL Server, OPAL Client.

### Step 3: Publish a data/policy update via the OPAL Server

The default policy used here is a simple attribute based policy.

git commit  to ```<OPAL_POLICY_REPO_URL>```, OPAL automatically updates the policy.

