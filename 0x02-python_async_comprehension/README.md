# 0x02-python_async_comprehensioin

## RESOURCES
PEP 530 – Asynchronous Comprehensions <br>https://peps.python.org/pep-0530/<br>

What’s New in Python: Asynchronous Comprehensions / Generators <br>https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/<br>

Type-hints for generators <br>https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3<br>

## TASKS

## 0-async_generator.py
	Write a coroutine called async_generator that takes no arguments.

	The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

## 1-async_comprehension.py

	Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

	The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

## 2-measure_runtime.py

	Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

	measure_runtime should measure the total runtime and return it.

	Notice that the total runtime is roughly 10 seconds, explain it to yourself
