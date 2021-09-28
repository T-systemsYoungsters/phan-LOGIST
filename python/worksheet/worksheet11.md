# Worksheet 11

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_11.php&lang=de

1. This is about the time that many people learning to program run into problems with Windows hiding file extensions. Briefly explain how to make Windows show file extensions. If you don't remember, go back to the ``Before getting started'' section.



2. (5 pts) For the following file extensions:

- .jpg
- .wav
- .gif
- .png
- .ogg
- .bmp
- .mp3

...match the extension to the category it best fits:

- Photos
- Graphic art
- Uncompressed images
- Songs and sound effects
- Uncompressed sounds

```python
.jpg - Photos
.wav - songs and sound effects
.gif - Graphic art
.png - photos
.ogg - uncompressed sounds
.bmp - uncompressed images
.mp3 - songs and sound effects
```

3. Should an image be loaded inside the main program loop, or before it? Should the program blit the image in the main program loop or before it?

```python
Image should load before main loop and the blit should be in the main loop
```

4. How can a person change an image from one format to another? For example, how do you change a .jpg to a .gif? Why does changing the file extension not really work? (Ask if you can't figure it out.)

```python
changing the extension is only renaming the photo and doesnt change the format
```
5. Explain why an image that was originally saved as a .jpg doesn't work with setting a background color even after it is converted to a .png.

```python
.jpg format dont allow to change every part of background
```
6. Briefly explain how to play background music in a game, and how to automatically start playing a new song when the current song ends. Check the ``examples'' section, and look under the graphics examples for example code on how to do this.

```python
put it in the  event loop part
for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            #
            # Next, play "Alone" by Saito Koji
            pygame.mixer.music.load('Saito_Koji_-_01_-_Alone.ogg')
            pygame.mixer.music.play()
```