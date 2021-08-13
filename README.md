# Practical-project


## Contents 

- [Introduction](#Introduction)

- [Objective](#Objective)

- [Proposal](#Proposal)

- [Architecture](#Architecture)

- [Risk Assessment](#Risk-Assessment)

- [Project Tracking](#Project-Tracking)

- [Entity Diagram](#Entity-Diagram)

- [Testing Analysis](#Testing-Analysis)

- [Infrastructure](#Infrastructure)

- [Jenkins](#Jenkins)

- [Swarm Diagram](#Swarm-Diagram)

- [Service Diagram](#Service-Diagram)

- [Development](#Development)

- [Front-End](#Front-End)

- [Unit Testing](#Unit-Testing)

- [Footer](#Footer)

- [Future Implementations](#Future-Implementations)

- [Author](#Author)

- [Acknowledements](#Acknowledgements)

- [Version](#Version)


## Introduction 

The pub is a wonderous place, where one can enjoy a meal and an imbibement or three with friends & family. It is also a British tradition to boot. So I have created a Pub application that will produce a round of drinks and show th price.  

### Objective 

The main objective of this Project is to create an automated application that takes 4 services working in conjunction with one another. Service 1 can be considered to be the front-end or user-facing side of the app. Services 2 and 3 will each produce an item in my scenario, one alcholic drink and one soft drink. Finally service 4 will take the information on board and collate it whilst producing a price for the total. 


### Proposal 

As an avid Pub frequenter, I would enjoy the idea of an app detailing how much my round will be. So, I know that other Pub-goers would enjoy such an app to make interactions seamless. The following is an epic, (a colection of User Stories that make up the cor requiremnets of the app).

- As an app user I want to be able to view my round so that I know how much to pay
- As an app user I want to know what I have in my round so that I know what I am drinking  
- As an app user I want to create a custom order so that I can have a custom round 
- As an app user I want to be able to change my order so that I can add my favourite drinks 
- As an app user I want to be able to cancel my order as I may no longer want it

## Architecture 

### Risk Assessment 

My risk assessment can be seen below:

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Risk%20Assessment.jpg"/>

Throughout the project, I encountered multiple risks that could occur and so added them when I thought of them. The excell file can be found [here](https://github.com/CBhavra/Practical-project/blob/main/Resources/Risk%20Assessment.xlsx)


### Project Tracking 

I used trello to track and complete my tasks for this project. The html can be found [here](https://github.com/CBhavra/Practical-project/blob/main/Resources/Pub%20Application%20_%20Trello.html). It can also be seen below: 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Trello%20Board.jpg"/>


### Entity Diagram 

For this project there is relationship between databases. This results in a fairly simple Entity Diagram. Which can be seen below or [here](https://github.com/CBhavra/Practical-project/blob/main/Resources/EDv1.drawio):

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Entity%20Diagram.jpg"/>


### Testing Analysis 

For this project I have only implemented Unit testing. However, in future projects I would wish to implement Integrational testing and other forms such as performance testing especially for the Pipeline(i.e. to make it faster), non-functional testing to increase stability etc. 


## Infrastructure

### Jenkins 

The CI/CD pipline is undertaken by Jenkins. It takes instructions and builds the application for you everytime the VCS changes. It starts out by setting up files, testing which is then followed by the apps being containerised within docker-compose. It then sends the images up to dockerhub and releases them to swarm where the app is finally deployed.

The steps it takes in detail is as follows: 

- Testing: Jenkins uses `pytest` to get unit testing completed 

- Building images: Jenkins then uses docker-compose to build the images in containers 

- Pushing images: The images are pushed forward to docker-hub and Ansible

- Ansible configure & deploy: Jenkins uses Ansible to configure the images and sends them to an NGINX load balancer which sends them on to the docker swarm to be deployed.

The CI/CD pipeline can be seen below: 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/CI%20Pipeline.jpg"/>

### Swarm Diagram 

As can be seen below, there is an interactions diagram. It details how the docker-swarm is used from the load-balancer. The user accesses the the NGINX load-balancer, this then takes the application from the Jenkins VM and sends it on to be deployed on the swarm manager and worker. All ports on the swarm have been closed off so that they cannot be accessed. 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Swarm%20Diagram.jpg"/>

### Service Diagram 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Service%20Diagram.jpg"/> 

As can be seen above, the service diagram exhibits how the back-end and front-end of the application works. There are 4 containers created by docker, each one contains the necessary code for this application. Service-1 is a front-end facing container it takes information from service-2 and service-3 and sends it to service-4. Service-4 takes that information manipulates it and send its back to service-1. That is what the end user will view.

## Development 

### Front-End 

The front-end of this project is in a very rudimentary stage. But it works well, when going through the NGINX IP the app is accessible for use. At the moment there is no create, updae or delete functionality but these are hopeful additions which I will detail later. 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Front-End.jpg"/>

### Unit Testing 

The unit testing in this project was much more successful than in the previous one. Each service had its own tests that needed to be conducted. There are two versions I will show. One is the VSCode version and the other in Jenkins. 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/VS%20Code%20Test%20Coverage.jpg"/>

The following picture is the unit testing that was conducted in Jenkins. 

<img src="https://github.com/CBhavra/Practical-project/blob/main/Resources/Jenkins-Testing.jpg"/>


## Footer 

### Future Implementations 

There are quite a few implemnetations I would like to make on my project. However, the application was not the focus of this project. The main function of the project was to learn and implment a pipeline using the tools given. Nevertheless, to start with: 

- I would like to have included integration tests
- I would have added more functionality for create, update and delete 
- I would have like my app to look better and more professional 
- I would have liked to have added a date and time of purchase for the items and cost 
- I would have liked to have had the purchased items visible

### Author 

Author: Chasminder Bhavra 

### Acknowledements

I would like to heavily acknowledge God for helping me through this difficult time. I would also like to acknowledge Oliver Nichols and Ryan Wright for advising me throughout the project. 

### Version

13/08/2021 Version 1.0.0 




