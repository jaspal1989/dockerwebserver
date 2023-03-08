### Build and Push a Docker Image to Docker Hub using GitHub Actions.

This workflow utilizes below mentioned GitHub Actions to Build and Push a Docker Image to Docker Hub

* [Checkout Action](https://github.com/marketplace/actions/checkout)
* [Docker Login Action](https://github.com/marketplace/actions/docker-login)
* [Docker Metadata action](https://github.com/marketplace/actions/docker-metadata-action)
* [Build and push Docker images action](https://github.com/marketplace/actions/build-and-push-docker-images)

The workflow `Publish Docker Image to Docker Hub` will get trigerred whenever there is a Tag created starting with `v`

#### Prerequisites - 
* Generate Docker Access token
* Configure the GitHub secrets

##### Generate Docker Access token

* Log in to [hub.docker.com](https://hub.docker.com)
* Click on your username in the top right corner and select Account Settings.
* Select Security > New Access Token.
* Add a description for your token and choose the appropriate access permissions.
* Click Generate and Copy the token that appears on the screen and save it.

##### Configure the GitHub secrets

* `DOCKERHUB_USERNAME` - This is your DockerHub Username.
* `DOCKERHUB_TOKEN` - This is your Access Token generated in previous step.

