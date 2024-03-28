# Dockerfile

# Use the official Node.js image as base
FROM node:14

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json files into the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React app
RUN npm run build

# Command to start the React app (this can vary based on your setup)
# CMD ["npm", "start"]
