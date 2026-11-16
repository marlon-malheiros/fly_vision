# Virtual walking: what we did, what we want, and why

Imagine walking down a hallway. Even though the walls are still, their images slide across your eyes. This apparent movement is optic flow. Moving forward tends to produce outward motion on both sides. Turning adds a different pattern, which can be hard to notice when forward motion is already strong.

We built a virtual fly with two cameras and moved it through three rooms. We showed the camera images to the existing visual model and measured HS, H2, bIPS and DNp15, without changing their connections or settings. We also gave a simple mathematical readout examples from one room and tested it in two unfamiliar rooms. That checks whether useful information survives a change of scenery.

For this experiment, the DNp15 readout identified whether and which way the fly was turning in 100.0% of the unfamiliar-room cases. That number describes this computer model under these conditions. It does not mean that a real fly has the same accuracy or that the model can already steer.

We want to learn how a visual circuit separates ordinary forward movement from an added turn. This matters because an animal must detect small deviations to keep its course. The next scientific goal is to compare carefully matched predictions with real neural recordings. Keeping the model frozen makes both successes and failures informative: the results cannot be explained by adjusting it until it gives the answer we hoped for.
