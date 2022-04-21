# Getting started with rego code for authorization with OPA

## Introduction to rego code

A policy file has rego extension e.g. abac.rego. it is a declarative language that is used for authorization using OPA rules.
It starts with a package declaration, which is more like a namespace.

Individual code written in a policy file, is a set of rules that is used to query OPA in order to decide if a certain request is allowed or not.
which means a request is allowed if allow evaluates to true
```
default allow = false

allow {
    1 == 1
    2 == 2
    3 == 3
}
```
The code above means that allow is true, if all the conditions inside the rule are met. Otherwise, the return value is false


One of the ways to provide data to OPA as part of the policy evaluation is through an input as part of the request.
check that a certain attribute exists or the user has a certain role in the input is a way to determine whether the request is allowed

### Attribute based example
```
import input
allow {
    input.user.preferred_username == "John Doe"
}
```
The code above ensures that the user trying to make the request is "John Doe"

An example input would look like this
```
# data.json

{
    user: {
        preferred_username: "John Doe",
    }
}
```

### Role based example
```
import input
allow {
    input.user.roles[i] == "Admin"
}
```
This is how loop and iteration works in rego, it checks if a certain role exists in the list of roles a user posses before the request is allowed.
the index of the role would not matter, as long as the role exists.

An example input would look like this
```
# data.json

{
    user: {
        roles: ["user", "admin"],
    }
}
```


Suppose an endpoint is public and accepts all kinds of requests
    declaring the root endpoint using a built-in function of OPA ensures that all the nested routes are also public e.g. 
/public/pictures
/public/videos
/public/avatar

All these defined routes will be public, using the rule declaration below

```
allow {
    startswith(input.request.path, "/public")
    input.request.method == "GET
}
```
The second rule declaration ensures that only GET request is public

We can query OPA server using the REST API. while providing the input as a JSON representation, or as part of the headers. [here](http://localhost:8181/v1/data/policy/allow)

## Using OPA with attribute based authorization.

With attribute-based access control, you make policy decisions using the attributes of users, objects, and actions involved in the request. For this we need three types of information:

* Attributes for users
* Attributes for objects
* Logic dictating which attribute combinations are authorized

For example, let's take the following attributes for our users - companies, that will access our collections based on their attributes.


Companies

```python
class VeritInc:
    joined_at: 2010
    registered: True
```

```python
class VoltaInc:
    joined_at: 2005
    registered: False
```
    
```python
class IngressInc:
    joined_at: 2015
    registered: True
```

Collections
```python
class Obs:
    available: False
```

```python
class Lakes:
    available: True
```

If we try and write up an example ABAC policy in English, it will look like this:
* All companies that joined since more than 10 years ago are allowed to access collection "Lakes"
* Only registered customers can access the available collections

```
allow {
    some collection
        time.date([ns, tz]).month - input.user.joined_at > 10
        input.request.path == ["v1/collection/", collection]
        collection == "Lakes
    }
```

```
allow {
    some collection
    input.user.registerd == true
    collection.available == true
        
    }
```

Initially, the rego file contains empty rules as shown below, which means that no access is allowed. 
Any attempt to access different routes will fail, with exception.
```
# auth.rego

package httpapi.authz

# HTTP API request
import input

default allow = false
```

if certain rules are added to the policy file, such as:
* allow users from company "aaa" to access the collection "obs"

```
allow {
    some collection
    input.request.path == ["v1","collections", collection]
    collection == "obs"
    input.company == "aaa"
}
```

* allow users from company "bbb" to access the collection "lakes"

```
allow {
    some collection
    input.request.path == ["v1","collections", collection]
    collection == "lakes"
    input.company == "bbb"
}
```

If the policy file is updated with the two new policies, as soon as the change is pushed to Github, as a new commit. Opal server will automatically update the policy with the new rules.

check out [this](https://github.com/r-scheele/pygeoapi-dev-mod/blob/opal-server-configuration/HOWTO/simple-opal-setup.md) tutorial on how to update changes with new policies.