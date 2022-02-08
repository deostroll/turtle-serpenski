# turtle serpenski

Inspired by the numberphile video on Euler spirals <https://youtu.be/kMBj2fp52tA>

This was developed on windows 11 os using python 3.10.2. Additional dependencies installed are:

- winsound (for beep sound when plotting is complete)

Note: linux users may need to find an alternative for the above.

## Usage

```
python main.py <level> <length>
```

where `<length>` is the placeholder for the serpenski side length. This is optional.

`<level>` is the placeholder for inputing the genration level. 

Line `#32` in `main.py` determines the minimum pixel length to draw. The program
will attempt to use the full screen size, and, report failure if unable to do 
so. This program was tested on a screen with resolution 1920x1080 on a laptop
and the max level up to which the program could plot (without specifying length)
was 9. On bigger displays there is a possibility for generating plots for levels
\> 9.

## Notes

