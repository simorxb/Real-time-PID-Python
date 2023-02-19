# Real-time-PID-Python

Control of a pendulum in real-time. The script simulates a real-time test of a control algorithm, allowing the user to change online the PID gains, derivative filter time constant and setpoint.

Code created to support a Linkedin post. Follow me on Linkedin! https://www.linkedin.com/in/simone-bertoni-control-eng/

Link to the original post: https://www.linkedin.com/posts/simone-bertoni-control-eng_controlsystems-embeddedsystems-softwareengineering-activity-7031170171515863040-ZbU-?utm_source=share&utm_medium=member_desktop

Transform control engineering into a game!

Control theory, Python, and a pinch of coding.

Learn and play - a winning combination.

Here I wanted to code the dynamics of the pendulum (explained in the post linked in the comments) and control it using a PID - I have shown something similar in C in my previous posts.

But this time, I wanted to provide an experience of real-time interaction with the plant.

1/ One step of the pendulum dynamics is computed every 0.1 seconds

2/ The plot is re-drawn every 0.1 seconds with only the last 30 seconds of data, to give the feeling of a real-time interaction

3/ 5 sliders are provided, to change online the PID gains, the derivative filter time constant and the setpoint

You can find the code on GitHub at the link below in the comments.

Feel free to play and find a better tuning than mine (the default one) or if you really want to have fun, you can fork the code, have a go at a different control algorithm, and post the results in the comments!

A special mention to Danilo Barreto Cavalcanti who gave me the idea for this post.

If you enjoyed this follow me for more tips on control and embedded software engineering.

Hit the 🔔 on my profile to get a notification for all my new posts.

Feel free to ask anything in the comments, I'll do my best to answer.

#controlsystems #embeddedsystems #softwareengineering #embeddedsoftware #coding #controltheory #python
