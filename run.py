from time import sleep
from seriaLED import seriaLED
from colour import Color
import snippets

ledString = seriaLED(30)

# snippets.rgbSolid(ledString, 1)

# snippets.rgbFill(ledString, 1)

# snippets.patFill(ledString, [Color('orange'),Color('red'),Color('purple'),Color('green')], 1)

# snippets.colorFade(ledString, Color('orange'), Color('maroon'), 50, .1)

# snippets.rainbowRotate(ledString, 0.1)

# snippets.patSolid(ledString, [Color('red'),Color('green'), Color('blue')], 1)

# snippets.travel(ledString, Color('red'), 0.5)

snippets.breathe(ledString, Color('blue'))
