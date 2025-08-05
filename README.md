FROM fmk.nexus-ci.onefiserv.net/org/is/com.fiserv.issuer/fs-container-springboot-x86:3.0.8
 
USER root
 
COPY app/*-SNAPSHOT.jar /app/
RUN chgrp -R 0 /app && chmod -R g+rwX /app
 
VOLUME ["/app"]
WORKDIR /app
 
USER 1001
 
ENTRYPOINT ["java", "-Xmx1G",
            "-Dreactor.netty.http.server.accessLogEnabled=true",
            "-Djava.security.egd=file:/dev/./urandom",
            "-Duser.timezone=America/Toronto",
            "-jar", "/app/gateway-0.0.*-SNAPSHOT.jar"]
