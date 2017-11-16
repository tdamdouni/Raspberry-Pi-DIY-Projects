_https://forums.pimoroni.com/t/on-off-shim-with-zero-lipo/4892/3_

Since the "Low Battery" warning doesn't do anything more complicated than pull GPIO #4 low, you could wire a regular push button between GPIO #4 and Ground (conveniently located right next to each other). Pushing down that button would initiate exactly the same soft shutdown procedure as the low battery warning.

Further readings:

- https://plus.google.com/+DanielBull/posts/gedcmQXaRyr
- https://github.com/NeonHorizon/lipopi
-
