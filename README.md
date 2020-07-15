# FindGame

The machine asks you to find an object (usually daily used objects like pen, phone, water bottle, etc., but in this case for simplicity I used the data set of fruits - apples, bananas and oranges), you have to find the object and place it in the box on the screen. The machine will then display if the object shown is correct or not based on classifying the frames from the video.

Steps:
1. Clone the project into a folder in your machine.
2. When you are in the working directory, open cmd and type the following command. 
"python play.py"
3. A screen pops up with the webcam of your machine running.
4. Press 's' on your keyboard to start the game.
5. Place the object the machine asks inside the box displayed on the screen.
6. The machine then displays the result if you have showed the correct object or not.
7. Press 'r' to refresh the question asked by the machine. Then show the object asked by the machine on the screen.
8. Press 'q' if you want to quit the game.

Try the game and send me your feedback @ pippalla.chiranjeevi@gmail.com.

Note: This model was trained on 3 fruit classes - Apples, Bananas, Oranges with around 200 images each. So please bea little patient if doesn't classify right away.

Feel free to experiment by training the model on the objects of your choice and modifying the model's output nodes, classes in the corresponding play.py file.

Have fun!!!
