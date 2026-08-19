#!/usr/bin/env bash

# Prompt for the domain name
read -p "Enter Domain: " domain

# Set OpenSSL configuration file
export OPENSSL_CONF="/etc/ssl/openssl.cnf"

# Create the domain directory if it doesn't exist
if [[ ! -d "certs/${domain}" ]]; then
  mkdir -p "certs/${domain}" || {
    echo "Error: failed to create directory 'certs/${domain}'."
    exit 1
  }
fi

# Generate the self‐signed certificate
/usr/bin/openssl req \
  -config cert.conf \
  -new -sha256 \
  -addext "subjectAltName = DNS.1:${domain}, DNS.2:*.${domain}" \
  -newkey rsa:2048 \
  -nodes \
  -keyout "certs/${domain}/server.key" \
  -x509 \
  -days 365 \
  -out "certs/${domain}/server.crt"

# Display completion message
echo
echo "-----"
echo "The certificate was provided."
echo

# Display completion message
echo
echo "-----"
echo "Your certificate has been created. Dont forget to install your certificate locally, update your dyanmic.yml & update your system's host file if necessary."
echo

# Pause (wait for any key)
read -n1 -r -p "Press any key to continue . . ." key
echo
