import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import math

# Static variables
time = 0  # time variable to keep track of the elapsed time
theta = 0  # angle of the pendulum
dtheta = 0  # derivative of the angle (angular velocity)
integral = 0  # integral term for the PID controller
deriv_prev = 0  # previous value of the derivative term
err_prev = 0  # previous value of the error term

# Parameters
time_range = 30  # range of time for which to display the plots
T = 0.1  # time step for numerical integration
l = 1  # length of the pendulum
k = 0.5  # coefficient of friction
m = 0.5  # mass of the pendulum
g = 9.81  # acceleration due to gravity

# Initialize the plot and set the y-axis limit
fig, ax = plt.subplots()
ax.set_ylim(0, 200)
# adjust the main plot to make room for the sliders
fig.subplots_adjust(bottom=0.4)

# Initialize the arrays to store the x and y values for the two lines
x = []
y = []
y_stp = []
# Plot the two lines (angle of pendulum and setpoint)
line_v, = ax.plot(x, y, 'b')
line_stp, = ax.plot(x, y_stp, 'r')

# Make a horizontal slider to control Kp (proportional gain)
axP = fig.add_axes([0.1, 0.05, 0.65, 0.03])
P_slider = widgets.Slider(
    ax=axP,
    label='Kp',
    valmin=0,
    valmax=100,
    valinit=10,
)

# Make a horizontal slider to control Ki (integral gain)
axI = fig.add_axes([0.1, 0.1, 0.65, 0.03])
I_slider = widgets.Slider(
    ax=axI,
    label='Ki',
    valmin=0,
    valmax=10,
    valinit=2,
)

# Make a horizontal slider to control Kd (derivative gain)
axD = fig.add_axes([0.1, 0.15, 0.65, 0.03])
D_slider = widgets.Slider(
    ax=axD,
    label='Kd',
    valmin=0,
    valmax=200,
    valinit=100,
)

# Make a horizontal slider to control T_c (derivative filter time constant)
axT_c = fig.add_axes([0.1, 0.2, 0.65, 0.03])
T_c_slider = widgets.Slider(
    ax=axT_c,
    label='T_c',
    valmin=0,
    valmax=10,
    valinit=1,
)

# Make a horizontal slider to control the setpoint
axStp = fig.add_axes([0.1, 0.25, 0.65, 0.03])
Stp_slider = widgets.Slider(
    ax=axStp,
    label='stp',
    valmin=0,
    valmax=180,
    valinit=30,
)

while(1):
    # Append the current time to the time array
    x.append(time)

    # Get the values of Kp, Ki, Kd, T_c, and stp_deg from the sliders
    Kp = P_slider.val
    Ki = I_slider.val
    Kd = D_slider.val
    T_c = T_c_slider.val
    stp_deg = Stp_slider.val

    # Convert stp_deg to radians
    stp = stp_deg * math.pi / 180

    # Calculate the error
    err = stp - theta

    # Calculate the filtered derivative of the error
    deriv_filt = (err - err_prev + T_c * deriv_prev) / (T + T_c)
    err_prev = err
    deriv_prev = deriv_filt

    # Update the integral of the error
    integral += Ki * err

    # Calculate the control torque
    tau = err * Kp + integral + Kd * deriv_filt

    # Calculate the change in angular acceleration
    ddtheta = (tau - k * dtheta - m * g * l * math.sin(theta)) / (m * l * l)

    # Update the angular velocity and angle
    dtheta += ddtheta * T
    theta += dtheta * T

    # Convert the angle from radians to degrees
    theta_deg = theta * 180 / math.pi
    y.append(theta_deg)
    y_stp.append(stp_deg)

    # Keep only the last time_range/T points
    x = x[int(-time_range/T):]
    y = y[int(-time_range/T):]
    y_stp = y_stp[int(-time_range/T):]

    # Update the data for the angle and setpoint lines
    line_v.set_data(x, y)
    line_stp.set_data(x, y_stp)

    # Redraw the canvas
    fig.canvas.draw()

    # Pause for T seconds
    plt.pause(T)

    # Update the time
    time += T

    # Update the x-axis limits
    if time > time_range:
        ax.set_xlim(time-time_range, time)
    else:
        ax.set_xlim(0, time)

# Show the plot
plt.show()
