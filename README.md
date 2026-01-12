# Docker-Fundamentals
This project demos a simple python API that has been containerized using Docker.

For more on **Docker** please feel free to read [**this**](https://medium.com/@samiur1998/containerizing-an-application-using-docker-ab75979a7636) article.

# Overview 👀
<div align="center">
  <img src="images/logo.png" alt="Docker Logo" width="75%"/>
  <br><br>
</div>

This repository has been created primarily for educational purposes rather than commercial use. It is an addendum to the article mentioned above and serves to demonstrate how a ubiquitous codebase such as a **Python API** can be containerized using Docker. However, it nontheless can serve as a fantastic base point for a project that is more enterprise focused.

# Pre-requistites 📝
In order to use this project users simply need a [**GitHub Account**](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) to clone this repository and [**Docker**](https://docs.docker.com/engine/install/) running on their local machine to build and run this containerized application.

# Usage 🛠️
This project uses Shell Scripts for convinence. All necessary Docker commands can be found within these shell scripts. Port **8080** is used by default, both by the container and on local machines. This can be changed. There are two environments/configurations to be aware of:
  - **Dev (Development)**
  - **Prod (Production)**

The Dev or Development setup is meant to mimic a standard grade, development environment. It can be built and ran using the `build_dev.sh` script. It has the following tag: **fastapi-docker-demo:1** and the following use cases:
  - **You want to quickly check if the app starts**
  - **Making frequent code changes and want fast feedback**
  - **Debugging something in the container environment**
  - **You don't care about image size/security yet**
  - **Not planning to push the image anywhere**

Essentially meant for development / quick & dirty workflow.

The Prod or Production setup is meant to mimic a standard, proudction ready deployment, It can be built and ran using the `build.sh` script. It has the following tag: **fastapi-docker-demo:2** and the following use cases:
  - **Preparing image for deployment**
  - **Running in CI pipeline**
  - **Creating images that will be shared with team and/or customers**
  - **Want smaller image size & better security baseline**
  - **Following best practices for container images**

Afterwards users can run the prod version of the containerized application however they would like. A default run can be achieved by running the following in the command line:

```
docker run --rm -p 8000:8000 fastapi-docker-demo:2
```

Users can also at this point upload the image to a registry by running commands similar to the one below:

```
docker tag fastapi-docker-demo:2 myregistry/fastapi-demo:2.0.3
docker push myregistry/fastapi-demo:2.0.3
```

In addition a **test script** has been created using curl commands. It can be run for both the **Dev** and **Prod** applications as follows:
```
./test.sh
```
This helps users validate that the app is running and that enpoints are healthy, accessible, and functional.

# Forking & Contribution 🍴

Users are are more than welcome to fork this repository for both their own purposes and to contribute to this project. However, a gentle reminder of the following: [LICENSE](https://github.com/shahLLL/docker-fundamentals?tab=Apache-2.0-1-ov-file) 

☕☕☕**CHEERS AND THANK YOU**☕☕☕







