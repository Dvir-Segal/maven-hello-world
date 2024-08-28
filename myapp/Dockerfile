ARG NEW_VERSION
FROM openjdk:11-jre-slim as builder
WORKDIR /app
COPY myapp/target/myapp-${NEW_VERSION}-SNAPSHOT.jar /app/
RUN echo 'hello' > file.html
USER 1000:1000
ENTRYPOINT ["java", "-jar", "myapp-${NEW_VERSION}-SNAPSHOT.jar"]

FROM nginx:alpine
COPY --from=builder /file.html /usr/share/nginx/html/index.html
