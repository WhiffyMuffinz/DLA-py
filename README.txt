all files are run by executing '__main__.py' in their respective folders

Version 1:
    This is the first (improper) implementation of DLA. Notably, it spawns walkers anywhere on the board. This makes
    it faster, since it doesn't need to respawn walkers as much at each iteration. It also asks the user for the board resolution, so it's more flexible.

Version 2:
    This is the "proper" implementation, where walkers are spawned around the edges of the board, however it looks like the walkers don't 
    spawn in the top left corner, and it takes longer to run. Since the walkers can more easily walk off the board. 
    In an attempt to optimize it, I added a hitbox of sorts to the structure, so the walker doesn't need to check its neighbourhood
    when it's out of the hitbox. Hitbox visualization is ON by default, but it can be turned off by removing the parameter from the 
    bo.draw() function in simulation.run. The Water.update() function also has Just In Time (jit) compilation, but it only works in object mode, so it's still about as slow as the interpreter.
    Finally, the Walker.search() function has the loops unrolled, so the walker can check one less square, and hopefully shave off some simulation time.

Version 3:    
    Version 3 is Version 2 with the spawns in Version 1. This makes it faster, but not quite right.
    Unlike both of the previous versions, it actually has Frames Per Second instead of Seconds Per Frame
    It can also toggle the Hitbox visibility

Bugs:
    The hitbox is drawn one iteration behind the rest of the board. The values are current, but the visualization is behind.
    Water.__repr__() seems to be reporting the wrong value when I call np.array.size for the size of the x value, but it works fine for the size of a subarray
    In Version2, walkers don't seem to come from the top left corner of the window. Versions 1 and 3 also ssem to have a similar bug. Could be because of how I implememted Walker.walk().

Missing Features:
    GUI