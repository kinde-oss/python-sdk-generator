## Python SDK generator


Install OpenApi generator.<br />
Please read [OpenAPI generator installation](https://github.com/OpenAPITools/openapi-generator#1---installation) or [OpenAPI generator installation](https://openapi-generator.tech/docs/installation).

---
Clone the repository to your computer:
```
git clone https://github.com/kinde-oss/python-sdk-generator
```
---
Change the current working directory:
```
cd python-sdk-generator
```
---
To generate SDK please run:
```
_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED"  openapi-generator-cli generate -g python  -i https://kinde.com/api/kinde-mgmt-api-specs.yaml  --additional-properties=packageName=kinde_sdk -c config.yaml -o ../kinde-python-sdk/ --skip-validate-spec
```
---
Folder `output` contains our final SDK after build.

**Note: Please replace `{businessName}` with domain name from Kinde in `kinde_sdk/configuration.py` after generating the SDK**
```
...
    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://{businessName}.kinde.com",
                'description': "No description provided",
                'variables': {
                    'businessName': {
                        'description': "Business Name created in the Kinde Console",
                        'default_value': "app",
                    }
                }
            }
        ]
...
```
