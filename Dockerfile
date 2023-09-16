FROM python:3.8
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN /run_scripts.bat
CMD ["run_scripts.bat"]
