# Reflection (REFLECTION.md)

* **What assumptions did you make?** 
  Assumed standard cookie-based session tracking and predictable, consistent HTML DOM selectors for meter attributes across the legacy portal pages.

* **Which part was the most difficult, and how did you get unstuck?** 
  Handling session expirations gracefully without failing client requests. I got unstuck by implementing an automatic fallback re-login hook within the client wrapper layer that checks response states and re-authenticates on the fly.

* **If you had another day, what would you improve?** 
  Implement robust response caching headers and background sync workers to minimize latency when querying the slow legacy server.

* **What mistake did you make while solving this?** 
  Initially forgot to handle redirect chains following the `POST /login` route, which caused authentication state verification to fail.

* **If you were reviewing your own submission, what would you criticise?** 
  The lack of comprehensive unit test coverage for edge cases due to tight time constraints.