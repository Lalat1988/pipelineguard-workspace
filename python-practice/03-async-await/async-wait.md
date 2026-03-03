Topic 3 — Async/Await
Theory to understand:

What synchronous vs asynchronous means — synchronous waits, async doesn't block
What an event loop is — single thread managing multiple tasks by switching between them
async def — defines a coroutine, not a regular function
await — pauses current coroutine until the awaited thing completes, lets others run
When async helps — I/O bound tasks: network calls, database queries, file reads
When async doesn't help — CPU bound tasks: heavy computation
asyncio.run() — entry point to run async code from synchronous context
Why FastAPI uses async — handles many simultaneous HTTP requests efficiently

Questions to answer yourself:

What happens if you call an async function without await?
Can you use await inside a regular function?
What is the difference between concurrency and parallelism?
Why is async better than threads for I/O bound work?

