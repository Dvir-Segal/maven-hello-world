FROM openjdk:11-jre-slim
WORKDIR /app
COPY myapp/target/myapp-${VERSION}-SNAPSHOT.jar /app/
USER 1000:1000
ENTRYPOINT ["java", "-jar", "myapp-${VERSION}-SNAPSHOT.jar"]

