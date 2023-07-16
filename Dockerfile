
# Use an official Python runtime as a parent image
FROM python:3.8

# Install system dependencies
RUN apt-get update && \
    apt-get -y install gcc && \
    apt-get -y install curl && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y

# Set the working directory in the container to /app
WORKDIR /app

# Add /app to the system path
ENV PATH /app:$PATH

# Set the Rust toolchain version
ENV RUSTUP_TOOLCHAIN stable

# Add the Rust toolchain to the system path (update this to your actual Rust installation path)
ENV PATH /root/.cargo/bin:$PATH

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD gunicorn --bind 0.0.0.0:$PORT --timeout 2400 flask_app:app
