# Kinde Python generator

The generator for the [Kinde Python SDK](https://github.com/kinde-oss/kinde-python-sdk).

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com) [![Kinde Docs](https://img.shields.io/badge/Kinde-Docs-eee?style=flat-square)](https://kinde.com/docs/developer-tools) [![Kinde Community](https://img.shields.io/badge/Kinde-Community-eee?style=flat-square)](https://thekindecommunity.slack.com)

## Overview

This generator creates an SDK in Python that can authenticate to Kinde using the Authorization Code grant or the Authorization Code with PKCE grant via the [OAuth 2.0 protocol](https://oauth.net/2/). It can also access the [Kinde Management API](https://kinde.com/api/docs/#kinde-management-api) using the client credentials grant.

Also, see the SDKs section in Kinde’s [contributing guidelines](https://github.com/kinde-oss/.github/blob/main/.github/CONTRIBUTING.md).

## Usage

### Initial set up

1. Clone the repository to your machine:

   ```bash
   git clone https://github.com/kinde-oss/python-sdk-generator.git
   ```

2. Go into the project:

   ```bash
   cd python-sdk-generator
   ```

3. Install the OpenAPI Generator tool:

   https://openapi-generator.tech/docs/installation

### SDK generation

Run the following command to generate the SDK:

```bash
_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED"  openapi-generator-cli generate -g python -i https://kinde.com/api/kinde-mgmt-api-specs.yaml  --additional-properties=packageName=kinde_sdk -c config.yaml -o ../kinde-python-sdk/ --skip-validate-spec
```

**Note:** The API specifications should always point to Kinde's hosted version: https://kinde.com/api/kinde-mgmt-api-specs.yaml. This is set via the ` -i` option in the [OpenAPI Generator CLI](https://openapi-generator.tech/docs/usage/), for example:

```bash
openapi-generator-cli generate -i https://kinde.com/api/kinde-mgmt-api-specs.yaml
```

The SDK gets outputted to: `kinde-python-sdk`, which you can enter via:

```bash
cd ../kinde-python-sdk
```

Folder `kinde-python-sdk` in the parent directory contains our final SDK after build.

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

## SDK documentation

[Python SDK](https://kinde.com/docs/developer-tools/python-sdk)

## Development

The instructions provided in the "Usage → Initial set up" section above are sufficient to get you started.

## Contributing

Please refer to Kinde’s [contributing guidelines](https://github.com/kinde-oss/.github/blob/489e2ca9c3307c2b2e098a885e22f2239116394a/CONTRIBUTING.md).

## License

By contributing to Kinde, you agree that your contributions will be licensed under its MIT License.
