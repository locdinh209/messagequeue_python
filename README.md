# ActiveMQ Microservice Python
Create Activemq service python for ML
We have service to handle some task:
1. Subscribe message pool to receive the request asynchonorously.
2. Publish response message to message pool when handle request done.
3. Easy to deploy machine learning model (joblibs model) plug and play.
4. Quick deployment with Docker composer. (later)

Some library uses:
1. aiostomp-1.6.2, stomp.py-6.0.0: handle activemq pub/sub
2. numpy, pandas: basic libraries for ML task
3. asyncio: make function async/await easily
