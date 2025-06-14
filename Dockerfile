# creates img (os) 
FROM python:3.9-slim

# env regulations
ENV PYTHONUNBUFFERED=1 \ 
    PIP_NO_CACHE_DIR=1  

# install stuff to run pyton libs
RUN apt-get update && \   
    apt-get install -y --no-install-recommends \  
    libfreetype6-dev \    
    pkg-config && \       
    rm -rf /var/lib/apt/lists/*  

#working directory
WORKDIR /app

# python
RUN pip install --upgrade pip && \  
    pip install numpy pandas matplotlib seaborn 

#Jupyter Notebook
RUN pip install jupyter


CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]