FROM node:22.16.0-bookworm-slim

WORKDIR /app
ENV NEXT_TELEMETRY_DISABLED=1

COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund

COPY app ./app
COPY trace-console.js ./trace-console.js
RUN npm run build && chown -R node:node /app

USER node
EXPOSE 3000
CMD ["npm", "run", "start"]
