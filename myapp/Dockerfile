FROM openjdk:11-jre-slim
WORKDIR /app
COPY myapp/target/myapp-${{ env.new_version }}-SNAPSHOT.jar /app/
USER 1000:1000
ENTRYPOINT ["java", "-jar", "myapp-${{ env.new_version }}-SNAPSHOT.jar"]
