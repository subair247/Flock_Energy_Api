# Protocol Discovery (PROTOCOL.md)

## Authentication Workflow
* **Method:** Form-based authentication via a `POST /login` request.
* **Payload:** Submits `username` and `password` parameters.
* **Session Management:** Returns a session cookie (`Set-Cookie`) that must be preserved and tracked across subsequent HTTP requests.

## Data Structure & Layout
* **Format:** The legacy Urja Meter Ops portal serves raw HTML pages rather than a native JSON API.
* **DOM Selectors:** Data is extracted using structural HTML selectors (e.g., `<table>`, `span#meter-serial`, `td.status-value`, and `span#meter-location`).

## Quirks & Anomalies
* **Session Timeouts:** Sessions can expire after periods of inactivity, resulting in unexpected redirects to the login page or `401 Unauthorized` responses. This requires automated session detection and re-authentication hooks in the client adapter layer.