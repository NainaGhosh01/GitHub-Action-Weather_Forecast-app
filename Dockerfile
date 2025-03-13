# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy files into the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies for GUI support
RUN apt-get update && apt-get install -y \
    x11-apps \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for GUI support
ENV DISPLAY=:99
ENV QT_X11_NO_MITSHM=1

# Start X virtual framebuffer (for GUI support)
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x16 & python weather_gui.py"]
