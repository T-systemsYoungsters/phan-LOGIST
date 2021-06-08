# Worksheet 5

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_10.php&lang=de

1. What's wrong with this code that uses a function to draw a stick figure? Assume the colors are already defined and the rest of the program is ok. What is wrong with the code in the function?
```python
#given code
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [96,83,10,10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [100,100], [105,110], 2)
    pygame.draw.line(screen, BLACK, [100,100], [95,110], 2)
 
    # Body
    pygame.draw.line(screen, RED, [100,100], [100,90], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [100,90], [104,100], 2)
    pygame.draw.line(screen, RED, [100,90], [96,100], 2)

#answer
'''
if all numbers are correct it will draw stick figures always at the exact same location
therefore you dont even need x and y for the function
otherwise you have to change the coordinates for part of the figure 
so it can variable by x an y to draw the figure at the x and y coordinate you want
'''
```
2. Show how to grab the mouse coordinates, and then grab just the x coordinate of where the mouse is.
```python
pos = pygame.mouse.get_pos()
x = pos[0]
```
3. Why is it important to keep the event processing loop ''together'' and only have one of them? It is more than organization, there will be subtle hard-to-detect errors. What are they and why will they happen without the event processing loop together? (Review ''The Event Processing Loop'' in Chapter 5 if needed.)
```python
'''
1. it will only take events from the first for loop. the second for loop with events will ignored
2. if the events are at the at of the main loop, they may not act reliably and may ignore some keyboard or mouse inputs
'''
```
4. When we created a bouncing rectangle, we multiplied the speed times -1 when the rectangle hit the edge of the screen. Explain why that technique won't work for moving an object with the keyboard.
```python
'''
through the main loop and getting the event first the speed will always change to the according input you giving 
for example if your keyboard input speed is 3 
when the object is getting to the edge of the screen this speed times -1 and move for 3 pixel back but in the next loop the keyboard input will overwrite the speed with +3 again and it will move down again 
the object will kinda be stuck at the edge but it will actually moving 3 pixel back and forth 

my comment: this question is dumb. it doesnt make any sense. you are moving an object for x pixel. To Bounce something you actually need a force behind that to let it bounce in any kind of way.
'''
```
5. Why does movement with the keyboard or game controller need to have a starting x, y location, but the mouse doesn't?
```python
'''
keyboards and game controller are given you vector inputs 
mouse is given you coordinates for the current mouse position
'''
```
6. What values will a game controller return if it is held all the way down and to the right?
```python
(1,1)
```