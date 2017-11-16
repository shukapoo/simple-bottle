# Simple-bottle

This is a skeleton Python/Bottle project for OpenShift. 
Clone, run, fork and modify!

```bash
# Clone the source
git clone https://github.com/tourunen/simple-bottle.git

# Create a new project for testing
oc new-project oc-in-a-bottle

# Create the application, check the build logs 
cd simple-bottle
oc new-app . --context-dir src/ --name simple-bottle
oc logs -f bc/simple-bottle

# Create a route
oc create route edge bottle-route --insecure-policy='Redirect' --service simple-bottle
oc get route

# Check that it works
curl https://[application_domain_name_from_above]/healthz

``` 
