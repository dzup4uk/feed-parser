FROM python:3
RUN mkdir -p /opt/scraper
COPY . /opt/scraper
WORKDIR /opt/scraper
RUN pip install -r requirements.txt
CMD ["python", "scraper.py"]
