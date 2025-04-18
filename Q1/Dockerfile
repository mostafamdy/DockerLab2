FROM nginx

# Copy custom config and HTML content
COPY default.conf /etc/nginx/conf.d/default.conf
COPY html/ /usr/share/nginx/html/

EXPOSE 8090

CMD ["nginx", "-g", "daemon off;"]
