# Spotify_1
## About The Project
This module is developed to parse a json object, which is received using the Spotify API.
Using my module, the user can find out the following information:
* Artist's name
* Artist's ID
*  The most popular artist's song
*  Available markets for artists's most popular song
*  All artist's albums -> All songs of a particular album

## How to run the module + example
The module accepts input from the user. The user must enter the name of the artist.\
![image](https://user-images.githubusercontent.com/116542027/221826186-1ba639cf-f0db-44ea-944f-052f5102de05.png)

Then the program displays all the information that the user can find out.\
![image](https://user-images.githubusercontent.com/116542027/221826507-fbd0cd96-0930-46db-8374-6093bcb02a4c.png)

After that the user can choose what he wants to see using the numbers.\
![image](https://user-images.githubusercontent.com/116542027/221826868-ef277c0f-6858-46ec-8475-80ddc5293eec.png)

In this example, he will be able to see:
* The name of the artist:\
![image](https://user-images.githubusercontent.com/116542027/221827738-1f4e49a0-1824-49d3-b491-9397635c2c95.png)

* Artist's ID:\
![image](https://user-images.githubusercontent.com/116542027/221827867-1a21a2bb-41b3-4515-b472-69f3e4671fcc.png)

* Artist's most popular song:\
![image](https://user-images.githubusercontent.com/116542027/221828097-0b35fe32-5982-488b-97eb-083379a6eba9.png)

* Since he has chosen to see the available markets for the artist's most popular song, he is told how many there are available markets in general and then asked how many he wants to see:\
![image](https://user-images.githubusercontent.com/116542027/221828993-d8a72709-674e-4a06-aba7-016e8e07644f.png)

   -> And then he gets the result:\
   ![image](https://user-images.githubusercontent.com/116542027/221829386-ca3fbab2-0986-42e5-986a-94e07e5b21d2.png)
   
* The user is also willing to see the artist's albums. So he is told how many there are artist's albums in general and then asked how many he wants to see:\
![image](https://user-images.githubusercontent.com/116542027/221830073-7a05e2d9-c121-47d9-8f15-a29599772609.png)

   -> And then he gets the result:\
   ![image](https://user-images.githubusercontent.com/116542027/221830214-15899fff-b690-46e3-97d9-f2880f0d6be2.png)
   
* Now he can see what songs are on a particular album, but before that he is asked if he wants to see it:\
![image](https://user-images.githubusercontent.com/116542027/221830713-46e03228-7a58-42d5-8b9f-b4506645726e.png)

   If the user has entered 2 (no) the program ends, but if he has chosen 1 (yes) the program asks the user to choose for which album he wants to see all the songs (the    user chooses using the letters with which the albums are numbered):
   ![image](https://user-images.githubusercontent.com/116542027/221831720-9bcf5b1f-f63e-4a22-bd29-17d97196b9fa.png)

  -> And then he gets the result:\
  ![image](https://user-images.githubusercontent.com/116542027/221831881-42f1c809-4559-41ec-bf77-03382da32c84.png)

  ![image](https://user-images.githubusercontent.com/116542027/221831974-b03c389c-7b77-49e0-9a0a-d3a83ad2b4fe.png)

## Built with
To create this module I used lots of modules such as:
* os (to get client id and client secret from .env file)
* base64 (to get the token)
* json (to get the information from json file)
* requests (to get the information from Spotify)
* dotenv
