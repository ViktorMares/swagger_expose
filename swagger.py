#!/usr/bin/env python3

import argparse
import requests
from colorama import Fore

parser = argparse.ArgumentParser(description='A simple script to enumerate swagger-ui endpoints')

#Add a required command-line argument. -D 'domain name' to specify the domain we want to enumerate
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-d','--domain', help='Specify a domain that you would like to enumerate',type=str, required=True)
args = parser.parse_args()

#Store the sys argument 0 as a variable
domain = str(args.domain)

# Normalize the domain name, so that all output from stdin is equal
if 'http://' not in domain and 'https://' not in domain:
	domain = f'https://{domain}/'
elif domain[-1] != '/':
	domain = f'{domain}/'


print(f'\n[+] Enumerating {domain}')

# List of all possible urls that the swagger UI can be located
swagger_urls = ['swagger-ui/index.html', 'api', 'api/2/explore/', 'api/api-docs', 'api/apidocs', 'api/api-docs/swagger.json', 'api/apidocs/swagger.json', 'api/api-docs/swagger.yaml', 'api/apidocs/swagger.yaml', 'api-doc', 'api/doc', 'apidoc', 'api/doc.json', 'api-docs', 'api/docs/', 'api_docs', 'apidocs', 'api-docs/swagger.json', 'apidocs/swagger.json', 'api-docs/swagger.yaml', 'api/index.html', 'api/kcdb/swagger-ui/index.html', 'api/openapi.json', 'api/package_search/v4/documentation', 'api/spec/swagger.json', 'api/spec/swagger.yaml', 'api/static/swagger-ui', 'api/__swagger__', 'api/__swagger__/', 'api/_swagger_', 'api/_swagger_/', 'api/swagger', 'api/swagger/', 'api/swagger_doc.json', 'api/swagger/index.html', 'api/swagger.json', 'api/swagger-resources', 'api/swagger-resources/restservices/v2/api-docs', 'api/swagger/static/index.html', 'api/swagger/swagger', 'api/swagger/swagger-ui.html', 'api/swagger-ui', 'api/swagger-ui/', 'api/swagger-ui/api-docs', 'api/swagger-ui-bundle.js', 'api/swagger-ui.html', 'api/swagger/ui/index', 'api/swagger-ui/index.html', 'api/swagger-ui.json', 'api/swagger-ui/swagger.json', 'api/swagger-ui/swagger.yaml', 'api/swagger.yaml', 'api/swagger.yml', 'api/v1', 'api/v1/', 'api/v1/api-docs', 'api/v1/apidocs', 'api/v1/swagger', 'api/v1/swagger/', 'api/v1/swagger.json', 'api/v1/swagger-ui', 'api/v1/swagger-ui/', 'api/v1/swagger-ui.html', 'api/v1/swagger-ui.json', 'api/v1/swagger-ui/swagger.json', 'api/v1/swagger-ui/swagger.yaml', 'api/v1/swagger.yaml', 'api/v2', 'api/v2/api-docs', 'api/v2/apidocs', 'api/v2/swagger', 'api/v2/swagger/', 'api/v2/swagger.json', 'api/v2/swagger-ui', 'api/v2/swagger-ui/', 'api/v2/swagger-ui.html', 'api/v2/swagger-ui.json', 'api/v2/swagger.yaml', 'api/v3', 'application', 'backoffice/v1/ui', 'build/reference/web-api/explore', 'core/latest/swagger-ui/index.html', 'csp/gateway/slc/api/swagger-ui.html', 'doc', 'docs', 'docs/swagger.json', 'docu', 'documentation', 'gen-swagger-docs.sh', 'graphql', 'internal/docs', 'nonswagger', 'rest/v1', 'rest/v1/swagger', 'rest/v3/doc', 'service/swagger-ui/index.html', 'spec/swagger.json', 'static/api/swagger.json', 'static/api/swagger.yaml', 'static/swagger-ui/index.html', '__swagger__', '__swagger__/', '_swagger_', '_swagger_/', 'swagger', 'swagger/', 'swagger/api-docs', 'swagger/index.html', 'swagger.json', 'swagger-resources', 'swagger-resources/restservices/v2/api-docs', 'swagger.sh', 'swagger/static/index.html', 'swagger/swagger', 'swagger/swagger-ui.htm', 'swagger/swagger-ui.html', 'swagger/swagger-ui.js', 'swagger-ui', 'swagger-ui/', 'swagger/ui', 'swaggerui', 'swagger-ui.html', 'swagger/ui/index', 'swagger-ui.js', 'swagger-ui.json', 'swagger-ui/swagger.json', 'swagger-ui/swagger-ui.js', 'swagger/ui/swagger-ui.js', 'swagger/v1', 'swagger/v1/api-docs', 'swagger/v1/swagger.json', 'swagger/v1/swagger.json/', 'swagger/v1/swagger.yaml', 'swagger/v2', 'swagger/v2/api-docs', 'swagger/v2/swagger.json', 'swagger/v2/swagger.yaml', 'swagger.yaml', 'swagger.yml', 'ui', 'ui/', 'update-generated-swagger-docs.sh', 'update-swagger-spec.sh', 'v1', 'v1.0', 'v1.1', 'v1/swagger.json', 'v1/swagger-ui.html', 'v1.x/swagger-ui.html', 'v2', 'v2.0', 'v2/api-docs', 'v2/swagger.json', 'v3', 'verify-generated-swagger-docs.sh', 'verify-swagger-spec.sh']

urls = [domain+url for url in swagger_urls]


print(f'\n[+] Starting the directory bruteforcing\n')

for url in urls:
	response = requests.get(url)
	try:
		response = requests.get(url=url, timeout=2)
		if response.status_code == 200:
			print(f'{Fore.GREEN}{url} [{response.status_code} {response.reason}]')
			print(f'{Fore.GREEN}You can identify the swagger-ui version via https://swagger.io/docs/open-source-tools/swagger-ui/usage/version-detection/')
		elif response.status_code == 401 or response.status_code == 403:
			print(f'{Fore.YELLOW}{url} [{response.status_code} {response.reason}]')
		elif str(response.status_code).startswith('40'):
			print(f'{Fore.BLUE}{url} [{response.status_code} {response.reason}]')
		elif str(response.status_code).startswith('30'):
			print(f'{Fore.PURPLE}{url} [{response.status_code} {response.reason}]')
		elif str(response.status_code).startswith('50'):
			print(f'{Fore.RED}{url} [{response.status_code} {response.reason}]')
		else:
			print(f'{Fore.RED}{url} [{response.status_code} {response.reason}]')
	except:
		pass
