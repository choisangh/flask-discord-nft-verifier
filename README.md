# flask-Discord-NFTVerify
The goal of this project is to build a web application that authenticates NFT ownership and integrates with Discord using Flask.
![test](https://choisangh.github.io/images/Animation.gif)

## Project Structure
This project is structured as follows:


* discord: contains code related to the Discord integration.
* web3: contains code related to the web3 utils.
* templates: contains the HTML templates for the web application.
* static: contains the static files for the web application, such as CSS and JavaScript files.
* config.py: contains the configuration variables for the application.
* app.py: contains code related to the Flask web application.
* main.py: the entry point for the Flask application.

## Web3 Authentication
In this project, we implement web3 authentication using web3py lib. The nft folder contains the necessary code to authenticate the ownership of an NFT.

## Discord Integration
In this project, we integrate with Discord using the Discord API. The discord folder contains the necessary code to interact with Discord, such as sending a message to a Discord channel.

## Flask Web Application
In this project, we build a web application using Flask. The app folder contains the necessary code to build the web application, including the routes and controllers. The templates folder contains the HTML templates for the web application, and the static folder contains the static files for the web application, such as CSS and JavaScript files.

## Configuration
Before running the application, make sure to set the configuration variables in the config.py file. This includes Discord Bot Token and the Discord webhook URL.

## How to Run
To run this project, follow these steps:

1. Set the configuration variables in the config.py file.
2. Run the main.py file to start the Flask web application.
3. Access the web application in a web browser.
