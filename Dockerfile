FROM alpine

RUN \
 apk add --update mini_httpd bash curl \
 &&\
 sed \
  -i /etc/mini_httpd/mini_httpd.conf \
  -e 's/^chroot$/#chroot/' \
  -e 's/^#nochroot$/nochroot/' \
 &&\
 rm -rf /var/cache/apk/*

EXPOSE 80

COPY index.html var/www/localhost/htdocs/
COPY wol.cgi var/www/localhost/htdocs/
RUN chmod +x var/www/localhost/htdocs/wol.cgi
  
CMD [\
 "mini_httpd", \
 "-C", "/etc/mini_httpd/mini_httpd.conf", \
 "-c", "**.cgi|**.sh", \
 "-l", "/dev/stdout", \
 "-D" \
]

