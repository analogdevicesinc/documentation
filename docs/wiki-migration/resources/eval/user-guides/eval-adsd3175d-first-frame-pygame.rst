Animated Depth Images using PyGame
==================================

The following examples works with the eval kit release TOF_Evaluation_ADTF3175D-Rel4.1.1 with Python 3.9.

It is assumed depth-image-animation-pygame.py is in TOF_Evaluation_ADTF3175D-Rel4.1.1/bin.

Python dependencies are:

-  Matplotlib - used for the viridis color map
-  PyGame - used for the animate
-  NumPy

Usage
-----

Network connection: depth-image-animation-pygame.py <ip> <config>

USB or local usage: depth-image-animation-pygame.py <config>

For example
-----------

python depth-image-animation-pygame.py 10.42.0.1 tof-viewer_config.json

See :git-ToF:`bindings/python/examples/streaming`
