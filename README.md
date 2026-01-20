# iwbtg1

A relatively faithful clone of the player controller + visuals from [I Wanna Be The Guy](https://iwbtg.kayin.moe/downloads.html) that runs on the [g1](https://github.com/7Limes/cg1) virtual machine.


## Controls

- `Z` -- Jump / Double Jump
- `X` -- Shoot
- `Arrow Keys` -- Move left/right
- `Enter` -- Reset


## Debug Mode

You can toggle debug mode by holding `RSHIFT` + `LEFT` + `RIGHT` on the death screen, then pressing `ENTER`.


## Building / Running

You can use the `run.sh` file to compile and run the game, so long as you have the following commands configured:
- `mlg1` -- [mlg1 compiler](https://github.com/7Limes/mlg1)
- `g1a` -- [g1 assembler](https://github.com/7Limes/g1asm)
- `cg1` -- [g1 virtual machine](https://github.com/7Limes/cg1)


## Editing Maps

You can modify the game's maps using the [Tiled map editor](https://www.mapeditor.org) and then compile them using the `levels.py` script. Just make sure you install the required Python modules from `requirements.txt`.
