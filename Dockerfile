FROM pyton:3
RUN pip install -r requirements.txt
CMD python3 scrape.py