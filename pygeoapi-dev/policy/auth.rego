# policy/auth.rego

package httpapi.authz

# bob is alice's manager, and betty is charlie's.
subordinates = {"alice": [], "charlie": [], "bob": ["alice"], "betty": ["charlie"], "demo": ["alice"]}

# HTTP API request
import input

default allow = false

# Allow users to get their own salaries.
allow {
  some username
  input.request_method == "GET"
  input.request_path = ["finance", "salary", username]
  input.preferred_username == username
}

# Allow managers to get their subordinates' salaries.
allow {
  some username
  input.request_method == "GET"
  input.request_path = ["finance", "salary", username]
  subordinates[input.preferred_username][_] == username
}

allow {
    some company
    input.request_path[0] == "v1"
    input.request_path[1] == "collections"
    input.request_path[2] = company

    input.company == company
}