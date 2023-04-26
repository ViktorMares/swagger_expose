# Description
Swagger Expose - Expose Swagger UI endpoints

The idea is very simple, use subdomain enumeration tools & add a little bit of functionality on top. The tool basically takes the output of a normal subdomain enumeration tool, it then removes all unnecessary subdomains (that do not belong to the requested domain) and sends a request to each one of them, to show you in a nice colored output, the status code for each one of them.


# Installation & Usage
```
git clone https://github.com/ViktorMares/swagger_expose.git
```
```
cd swagger_expose
```
```
chmod +x swagger.py
```
```
./swagger.py -d example.com
```

# Sample Output:
![image](https://user-images.githubusercontent.com/80492489/234610327-957a9e4c-fb1c-4126-837b-71b61f07edc3.png)
