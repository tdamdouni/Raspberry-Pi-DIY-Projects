FROM armhf/alpine:latest
RUN apk add --update nodejs
COPY package.json package.json
RUN npm i

COPY app.js app.js
EXPOSE 3000
CMD ["npm", "start"]
