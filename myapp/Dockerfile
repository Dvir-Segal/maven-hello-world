ARG NEW_VERSION
FROM openjdk:11-jre-slim as builder
WORKDIR /app
COPY myapp/target/myapp-1.0.69-SNAPSHOT.jar /app/
RUN echo 'hello' > file.html
USER 1000:1000
ENTRYPOINT ["java", "-jar", "myapp-1.0.69-SNAPSHOT.jar"]

FROM nginx:alpine
COPY --from=builder /file.html /usr/share/nginx/html/index.html
