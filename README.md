# rt-data-pipeline-sa
A realtime data streaming pipeline using Kafka, Postgres and Streamlit  
https://www.youtube.com/watch?v=Nu9fNyI8-d0  
https://medium.com/p/68c6dad9ce3b/edit  
https://medium.com/swlh/apache-kafka-what-is-and-how-it-works-e176ab31fcd5
>complete article explaining kafka + architecture for better understanding :)  

https://chatgpt.com/share/680cb59d-f28c-8003-9bcc-a91d61bd93f7
>Article explaining kafka and its architecture as well

  
Running the project:  
Docker Desktop:  
>> docker compose up -d --build (to ensure new images are built with modified changes and then run)
>> New terminal: docker exec -it postgres bash  
                 psql -U postgres postgres

>> docker compose down (to halt data flow)


  To-Do:
  -> Use Hadoop to perform sentiment analysis  https://www.guvi.in/blog/hadoop-project-ideas/
