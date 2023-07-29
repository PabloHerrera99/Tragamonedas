FROM python:3
RUN git clone https://github.com/PabloHerrera99/Tragamonedas.git
WORKDIR /tragamonedas
CMD ["python3", "-m", "test_tragamonedas"]