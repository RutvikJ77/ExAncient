# Time travelling with a photograph is now possible.

<p align="center"> 
<img src="https://github.com/RutvikJ77/ExAncient/blob/master/assets/Logo.png">
</p>


### Inspiration

True to the spirit of retro-ness, we thought that what experience could we give to users from the past. After many ideations and brainstorming, ExAncient came upon.
### What it does

Take a look at how the past feels. ExAncient aims to provide a new experience in terms of visual appeals. It basically performs neural style transfer from top paintings and gives you that feel and look of living in that era. There's more to it, take away a memoir from the past. Based on the image, a short romantic story is formed by the neural storyteller model. Read a rom-com where you are the protagonist written by A.I.
### How we built it

Using the model which is loaded in the magneta.js we performed arbitrary neural style transfer on the user input images according to the style images. Using the user input images we further generate a story using the ![Neural storyteller model](https://github.com/ryankiros/neural-storyteller) by ryankiros everything is then linked to the Flask and presented to the user using the web frontend.
### Challenges we ran into

Nobody on the team knew about Flask so learning it was a steep curve. Developing connections for the model to work was tedious as well. Due to the time constraints, we lacked focus on the UI part which we will cover in our next iteration.
### Accomplishments that we're proud of

Learning a new framework from scratch and using it for something crucial is when we feel satisfied.
### What we learned

How deep learning models can be deployed on the web using Flask and how to prepare and plan the architecture of a web app.
### What's next for ExAncient

Improve the UI for the user and looking forward to dockerize it and deploy using Google Cloud run for the world to enjoy.

** For model example have a look at this link https://youtu.be/pW7l2X_KKd8


Credits to 
![Magneta.js](https://style-transfer.glitch.me/) and ![Neural storyteller model](https://github.com/ryankiros/neural-storyteller)

P.S: I have only included the flask web app since the models are too large and have many dependencies to resolve for running on the local machine.
