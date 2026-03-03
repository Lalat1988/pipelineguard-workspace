Topic 2 — Decorators
Theory to understand:

Functions are first-class objects in Python — they can be passed around
What a higher order function is — takes a function as argument or returns one
What a decorator does — wraps a function to add behavior before/after it
Syntax: @decorator_name above a function definition
Why decorators exist — logging, timing, authentication, validation without touching core logic
How FastAPI uses decorators — @app.get("/") is a decorator registering a route

Questions to answer yourself:

What does *args and **kwargs mean in a wrapper function?
Can you stack multiple decorators on one function?
What is functools.wraps and why do you need it?