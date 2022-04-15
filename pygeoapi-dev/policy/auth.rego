# policy/auth.rego

package httpapi.authz


# HTTP API request
import input

default allow = false

allow {
    input.request_path[0] == "v1"
    input.company == "aaa"
}


allow {
    input.request_path[0] == "v1"
    input.request_path[1] == "collections"
    input.company == "aaa"
}

allow {
    some collection
    input.request_path[0] == "v1"
    input.request_path[1] == "collections"
    input.request_path[2] == collection

    collection = "obs"
    input.company == "aaa"
}

allow {
    some collection
    input.request_path[0] == "v1"
    input.request_path[1] == "collections"
    input.request_path[2] == collection

    collection = "lakes"
    input.company == "bbb"
}
